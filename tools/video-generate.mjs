#!/usr/bin/env node

/**
 * video-generate.mjs - Paperclip平台视频生成工具
 *
 * 支持多个视频生成API提供商：
 * - 可灵/Kling AI (默认) - 中国区可用的AI视频生成服务
 * - Runway Gen (备选)
 *
 * 使用方法:
 *   node tools/video-generate.mjs --provider kling --prompt "品牌宣传视频" [options]
 *
 * 环境变量:
 *   KLING_AK - Kling AI Access Key
 *   KLING_SK - Kling AI Secret Key
 *   RUNWAY_API_KEY - Runway API Key
 */

import crypto from 'node:crypto';

// ============================================================
// 配置
// ============================================================
const PROVIDERS = {
  kling: {
    name: '可灵 AI (Kling)',
    baseUrl: 'https://openapi.klingai.com',
    models: {
      'kling-v1': 'Kling 1.0 (基础版)',
      'kling-v1-5': 'Kling 1.5 (增强版)',
      'kling-v1-6': 'Kling 1.6 (最新版)',
    },
    defaultModel: 'kling-v1-6',
    resolutions: ['720p', '1080p'],
    durations: [5, 10],
    supportsImageToVideo: true,
    maxPromptLength: 2000,
    needsAkSk: true,
  },
  runway: {
    name: 'Runway Gen',
    baseUrl: 'https://api.runwayml.com/v1',
    models: {
      'gen-3-alpha': 'Gen-3 Alpha',
      'gen-2': 'Gen-2',
    },
    defaultModel: 'gen-3-alpha',
    resolutions: ['720p', '1080p'],
    durations: [5, 10],
    supportsImageToVideo: true,
    maxPromptLength: 1000,
    needsAkSk: false,
  },
};

// ============================================================
// 工具函数
// ============================================================

/** 生成 Kling API 的 JWT 认证 Token */
function generateKlingToken(ak, sk) {
  const header = { alg: 'HS256', typ: 'JWT' };
  const payload = {
    iss: ak,
    exp: Math.floor(Date.now() / 1000) + 1800, // 30分钟有效期
    nbf: Math.floor(Date.now() / 1000) - 5,
  };

  const base64url = (obj) => Buffer.from(JSON.stringify(obj))
    .toString('base64url')
    .replace(/=+$/, '');

  const headerEncoded = base64url(header);
  const payloadEncoded = base64url(payload);
  const signature = crypto
    .createHmac('sha256', sk)
    .update(`${headerEncoded}.${payloadEncoded}`)
    .digest('base64url');

  return `${headerEncoded}.${payloadEncoded}.${signature}`;
}

/** 带重试和超时的 fetch */
async function fetchWithRetry(url, options, retries = 3, timeoutMs = 30000) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), timeoutMs);

  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      const response = await fetch(url, {
        ...options,
        signal: controller.signal,
      });
      const body = await response.text();
      let parsed;
      try { parsed = JSON.parse(body); } catch { parsed = body; }

      if (!response.ok) {
        throw new Error(`[${response.status}] ${JSON.stringify(parsed)}`);
      }
      return parsed;
    } catch (err) {
      if (attempt === retries) throw err;
      await new Promise(r => setTimeout(r, 1000 * attempt));
    } finally {
      clearTimeout(timeout);
    }
  }
}

/** 等待视频生成任务完成 */
async function pollTask(provider, taskId, credentials, maxWaitMs = 300000) {
  const startTime = Date.now();
  let lastStatus = '';

  while (Date.now() - startTime < maxWaitMs) {
    let result;

    if (provider === 'kling') {
      const token = generateKlingToken(credentials.ak, credentials.sk);
      result = await fetchWithRetry(
        `${PROVIDERS.kling.baseUrl}/v1/videos/${taskId}`,
        { headers: { Authorization: `Bearer ${token}` } },
        2, 10000
      );
    } else if (provider === 'runway') {
      result = await fetchWithRetry(
        `${PROVIDERS.runway.baseUrl}/text_to_video/${taskId}`,
        { headers: { Authorization: `Bearer ${credentials.apiKey}` } },
        2, 10000
      );
    }

    const status = result?.data?.status || result?.status || 'unknown';
    if (status !== lastStatus) {
      lastStatus = status;
      console.error(`[进度] 任务状态: ${status}`);
    }

    if (status === 'succeed' || status === 'completed') {
      const videos = result?.data?.videos || result?.data?.task_result?.videos || [];
      const videoUrl = videos[0]?.url || result?.data?.video?.url || '';
      return {
        success: true,
        taskId,
        videoUrl,
        duration: result?.data?.duration || null,
        resolution: result?.data?.resolution || null,
        raw: result,
      };
    }

    if (status === 'failed') {
      return {
        success: false,
        taskId,
        error: result?.data?.message || result?.data?.fail_reason || '视频生成失败',
        raw: result,
      };
    }

    // 等待后轮询（前30秒每2秒，之后每5秒）
    const waitMs = Date.now() - startTime < 30000 ? 2000 : 5000;
    await new Promise(r => setTimeout(r, waitMs));
  }

  return {
    success: false,
    taskId,
    error: `等待超时 (${maxWaitMs / 1000}秒)`,
  };
}

// ============================================================
// 主逻辑
// ============================================================

async function main() {
  const args = parseArgs();

  if (args.help || !args.prompt) {
    printUsage();
    process.exit(args.help ? 0 : 1);
  }

  const provider = args.provider || 'kling';
  const providerConfig = PROVIDERS[provider];
  if (!providerConfig) {
    console.error(JSON.stringify({ error: `不支持的提供商: ${provider}`, providers: Object.keys(PROVIDERS) }));
    process.exit(1);
  }

  // 获取认证凭据
  let credentials;
  try {
    credentials = getCredentials(provider);
  } catch (err) {
    console.error(JSON.stringify({ error: err.message }));
    process.exit(1);
  }

  // 检查参数
  if (args.prompt.length > providerConfig.maxPromptLength) {
    console.error(JSON.stringify({ error: `提示词过长（${args.prompt.length}/${providerConfig.maxPromptLength}字符）` }));
    process.exit(1);
  }

  // 发起视频生成请求
  try {
    console.error(`[开始] 使用 ${providerConfig.name} 生成视频...`);
    console.error(`[参数] 模型: ${args.model || providerConfig.defaultModel}`);
    console.error(`[参数] 分辨率: ${args.resolution || '1080p'}`);
    console.error(`[参数] 时长: ${args.duration || 10}秒`);
    console.error(`[参数] 提示词: ${args.prompt}`);
    if (args.negativePrompt) console.error(`[参数] 负面提示词: ${args.negativePrompt}`);

    let taskResult;

    if (provider === 'kling') {
      taskResult = await callKlingApi(args, credentials);
    } else if (provider === 'runway') {
      taskResult = await callRunwayApi(args, credentials);
    }

    if (!taskResult.success) {
      console.error(JSON.stringify({ error: `提交任务失败: ${taskResult.error}` }));
      process.exit(1);
    }

    console.error(`[提交] 任务ID: ${taskResult.taskId}`);

    // 如果启用了等待，轮询直到完成
    if (args.wait !== false) {
      console.error('[等待] 正在等待视频生成完成...');
      const result = await pollTask(provider, taskResult.taskId, credentials, (args.maxWait || 300) * 1000);

      if (result.success) {
        console.error('[完成] 视频生成成功！');
        const output = {
          success: true,
          videoUrl: result.videoUrl,
          taskId: result.taskId,
          duration: result.duration,
          resolution: result.resolution,
        };
        // 输出JSON结果到stdout（供Agent解析）
        console.log(JSON.stringify(output));
      } else {
        console.error(`[失败] ${result.error}`);
        console.log(JSON.stringify({ success: false, taskId: result.taskId, error: result.error }));
      }
    } else {
      // 不等待，直接返回任务ID
      console.log(JSON.stringify({
        success: true,
        taskId: taskResult.taskId,
        polling: true,
        message: '任务已提交，请稍后查询',
      }));
    }
  } catch (err) {
    console.error(`[错误] ${err.message}`);
    console.log(JSON.stringify({ success: false, error: err.message }));
    process.exit(1);
  }
}

/** 调用Kling AI API */
async function callKlingApi(args, credentials) {
  const token = generateKlingToken(credentials.ak, credentials.sk);
  const headers = {
    Authorization: `Bearer ${token}`,
    'Content-Type': 'application/json',
  };

  const body = {
    model_name: args.model || 'kling-v1-6',
    prompt: args.prompt,
    cfg: args.cfg ?? 0.5,
    duration: args.duration || 10,
    mode: args.mode || 'pro',
    resolution: args.resolution || '1080p',
  };

  if (args.negativePrompt) body.negative_prompt = args.negativePrompt;
  if (args.image) {
    // image_to_video
    body.image = args.image;
    body.image_tailor = args.imageTailor || null;
  }

  const endpoint = args.image
    ? `${PROVIDERS.kling.baseUrl}/v1/videos/img2video`
    : `${PROVIDERS.kling.baseUrl}/v1/videos/text2video`;

  const result = await fetchWithRetry(endpoint, {
    method: 'POST',
    headers,
    body: JSON.stringify(body),
  }, 3, 60000);

  const taskId = result?.data?.task_id;
  if (!taskId) {
    return { success: false, error: JSON.stringify(result) };
  }

  return { success: true, taskId };
}

/** 调用Runway API */
async function callRunwayApi(args, credentials) {
  const headers = {
    Authorization: `Bearer ${credentials.apiKey}`,
    'Content-Type': 'application/json',
  };

  const body = {
    model: args.model || 'gen-3-alpha',
    prompt_text: args.prompt,
    resolution: args.resolution || '1080p',
    duration: args.duration || 10,
  };

  if (args.negativePrompt) body.negative_prompt = args.negativePrompt;

  const endpoint = `${PROVIDERS.runway.baseUrl}/text_to_video`;

  const result = await fetchWithRetry(endpoint, {
    method: 'POST',
    headers,
    body: JSON.stringify(body),
  }, 3, 60000);

  const taskId = result?.id || result?.task_id;
  if (!taskId) {
    return { success: false, error: JSON.stringify(result) };
  }

  return { success: true, taskId };
}

/** 解析命令行参数 */
function parseArgs() {
  const args = {};
  const raw = process.argv.slice(2);

  for (let i = 0; i < raw.length; i++) {
    switch (raw[i]) {
      case '--provider': args.provider = raw[++i]; break;
      case '--prompt': args.prompt = raw[++i]; break;
      case '--negative-prompt': args.negativePrompt = raw[++i]; break;
      case '--model': args.model = raw[++i]; break;
      case '--resolution': args.resolution = raw[++i]; break;
      case '--duration': args.duration = parseInt(raw[++i]); break;
      case '--cfg': args.cfg = parseFloat(raw[++i]); break;
      case '--mode': args.mode = raw[++i]; break;
      case '--image': args.image = raw[++i]; break;
      case '--max-wait': args.maxWait = parseInt(raw[++i]); break;
      case '--no-wait': args.wait = false; break;
      case '--help': args.help = true; break;
      case '--list-providers': args.listProviders = true; break;
      case '--query-task': args.queryTask = raw[++i]; break;
    }
  }

  return args;
}

/** 获取认证凭据 */
function getCredentials(provider) {
  if (provider === 'kling') {
    const ak = process.env.KLING_AK;
    const sk = process.env.KLING_SK;
    if (!ak || !sk) {
      throw new Error(
        '需要设置 KLING_AK 和 KLING_SK 环境变量。\n' +
        '获取方式: 登录 https://console.klingai.com 获取 Access Key 和 Secret Key'
      );
    }
    return { ak, sk };
  }

  if (provider === 'runway') {
    const apiKey = process.env.RUNWAY_API_KEY;
    if (!apiKey) {
      throw new Error(
        '需要设置 RUNWAY_API_KEY 环境变量。\n' +
        '获取方式: 登录 https://runwayml.com 生成 API Key'
      );
    }
    return { apiKey };
  }

  throw new Error(`不支持的提供商: ${provider}`);
}

/** 打印使用说明 */
function printUsage() {
  console.error(`
Paperclip 视频生成工具
======================
使用方法: node tools/video-generate.mjs --prompt "描述" [选项]

必要参数:
  --prompt TEXT            视频内容描述

可选参数:
  --provider NAME          提供商: kling (默认), runway
  --model NAME             模型版本 (默认: kling-v1-6 / gen-3-alpha)
  --resolution RES        分辨率: 720p, 1080p (默认: 1080p)
  --duration SEC           视频时长: 5, 10 (默认: 10)
  --cfg VALUE              CFG scale 0-1 (默认: 0.5)
  --mode MODE              生成模式: pro (默认)
  --negative-prompt TEXT   负面提示词
  --image URL              图片URL (图片生成视频)
  --max-wait SEC           最大等待时间 (默认: 300)
  --no-wait                不等待完成，直接返回任务ID
  --query-task TASK_ID     查询已有任务状态
  --list-providers         列出支持的提供商

环境变量:
  KLING_AK                 可灵 Access Key
  KLING_SK                 可灵 Secret Key
  RUNWAY_API_KEY           Runway API Key

示例:
  # 基本文本生成视频
  node tools/video-generate.mjs --prompt "A brand promotional video of a smart bathroom"

  # 指定模型和分辨率
  node tools/video-generate.mjs --prompt "产品展示动画" --model kling-v1-6 --resolution 1080p

  # 不等待异步执行
  node tools/video-generate.mjs --prompt "品牌宣传片" --no-wait

  # 查询任务状态
  node tools/video-generate.mjs --query-task "task_xxxxxxxx"
`);
}

// 列出提供商
function listProviders() {
  console.log(JSON.stringify(PROVIDERS, null, 2));
}

// 如果直接查询任务，特殊处理
async function queryExistingTask(taskId, provider, credentials) {
  const result = await pollTask(provider, taskId, credentials);
  if (result.success) {
    console.log(JSON.stringify({ success: true, videoUrl: result.videoUrl, taskId }));
  } else {
    console.log(JSON.stringify({ success: false, taskId, error: result.error }));
  }
}

// 入口
main().catch(err => {
  console.error(JSON.stringify({ error: err.message }));
  process.exit(1);
});
