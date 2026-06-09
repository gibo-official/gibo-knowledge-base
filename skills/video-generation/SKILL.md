---
name: video-generation
required: false
description: Teach agents how to generate AI videos using the Paperclip video generation tool. Supports Kling AI (可灵AI) and Runway Gen APIs for text-to-video and image-to-video generation.
---

# 视频生成

使用这个技能通过 Paperclip 视频生成工具创建 AI 视频内容。该技能支持多个视频生成API提供商，默认使用**可灵AI（Kling）**——中国区可用的高性能视频生成服务。

## 支持的提供商

| 提供商 | ID | 特点 | 中国可用 |
|--------|-----|------|---------|
| 可灵AI (Kling) | `kling` | 快手旗下，支持中文/英文提示词，最高1080p，10秒 | ✅ |
| Runway Gen | `runway` | Gen-3 Alpha模型，高清输出 | ⚠️ 需网络环境 |

## 工作原理

视频生成是**异步过程**：
1. 提交视频生成请求 → 获取任务ID
2. API在服务器端处理（通常30秒到3分钟）
3. 轮询任务状态，直到完成
4. 获取生成的视频URL

## 工具位置

视频生成脚本位于工作区的 `tools/video-generate.mjs`。Agent 通过 Bash 执行此脚本。

## 使用方法

### 前置条件

确保 `KLING_AK` 和 `KLING_SK` 环境变量已设置（通过 Paperclip 密钥管理或环境配置）。
API 端点: `https://openapi.klingai.com`（使用 JWT Bearer Token 认证）
注意：Kling 账户需要有足够的积分余额才能生成视频。

### 基本用法

**1. 文本生成视频（推荐用于品牌宣传片）**
```bash
node tools/video-generate.mjs \
  --provider kling \
  --prompt "高端智能卫浴品牌宣传视频，现代简约风格，产品特写与空间展示交替，金色调性，30岁中国城市家庭使用场景" \
  --duration 10
```

**2. 指定模型和参数**
```bash
node tools/video-generate.mjs \
  --provider kling \
  --model kling-v1-6 \
  --resolution 1080p \
  --duration 10 \
  --prompt "智能水龙头产品展示，科技感，金属质感特写，水流效果，光线反射"
```

**3. 图片生成视频（更可控）**
```bash
node tools/video-generate.mjs \
  --provider kling \
  --image "https://example.com/product.jpg" \
  --prompt "产品在厨房环境中使用，缓慢旋转展示，暖色调" \
  --duration 5
```

**4. 不等待直接返回（提交后做其他事）**
```bash
node tools/video-generate.mjs \
  --prompt "品牌视频" \
  --no-wait
# 返回: {"success":true,"taskId":"task_xxx","polling":true}
```

**5. 查询已有任务**
```bash
node tools/video-generate.mjs \
  --query-task "task_xxx"
```

### 视频生成提示词最佳实践

| 要素 | 说明 | 示例 |
|------|------|------|
| 品牌名称 | 明确提到品牌 | "GIBO品牌智能卫浴" |
| 场景描述 | 详细描述场景 | "现代浴室，大理石纹理，柔和灯光" |
| 情绪调性 | 描述目标氛围 | "高端、优雅、温馨" |
| 视觉风格 | 镜头运动方式 | "缓慢推近，环绕展示产品细节" |
| 目标受众 | 使用场景中的人 | "30岁中国城市家庭日常使用" |

## 提示词示例库

### 品牌宣传视频
> "GIBO智能卫浴品牌宣传片，现代轻奢风格浴室环境，智能水龙头特写展示金属质感与水流设计，年轻夫妇在卫浴空间享受智能生活，暖色调灯光，缓慢平移镜头，电影质感，15秒短视频风格"

### 产品展示视频
> "智能感应水龙头360度旋转展示，拉丝不锈钢表面反光优雅，水流从出水口流出的慢动作，极简背景突出产品，科技感光线，产品细节清晰可见"

### 场景演示视频
> "GIBO品牌浴室空间全景，从左到右缓慢移动，展示马桶、花洒、洗手台全套产品，温馨家居风格，清晨自然光线，干净整洁现代设计"

## 输出格式

成功时，工具通过 stdout 返回 JSON：
```json
{
  "success": true,
  "videoUrl": "https://cdn.klingai.com/videos/xxxx.mp4",
  "taskId": "task_xxxx",
  "duration": 10,
  "resolution": "1080p"
}
```

失败时，工具通过 stderr 输出错误信息，stdout 返回错误 JSON：
```json
{
  "success": false,
  "error": "错误描述",
  "taskId": "task_xxxx"
}
```

## 处理流程（Agent工作流）

当需要生成视频时，遵循以下步骤：

1. **确认需求**：了解视频类型（品牌宣传、产品展示、场景演示等）
2. **编写提示词**：参考上面的最佳实践编写详细提示词
3. **执行工具**：调用视频生成脚本，等待完成
4. **检查结果**：验证视频URL是否可用
5. **交付**：将视频URL提供给相关人员或记录到文档中

## 已知限制

- 单个视频最长10秒（Kling API限制）
- 处理时间通常在30秒到3分钟不等
- 需要稳定的网络连接访问API
- API密钥通过环境变量管理，确保在执行前已配置
