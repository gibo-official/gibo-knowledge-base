# 视频生成API集成方案 — PFBC-59

**创建日期**: 2026-06-06  
**负责人**: 平台工程师  
**目标**: 在Paperclip平台上接入视频生成模型API，使agent具备AI视频生成能力

---

## 一、API选型对比

| 维度 | 可灵 Kling AI | Runway Gen-3 Alpha | Luma Dream Machine | Pika 2.0 |
|------|--------------|-------------------|-------------------|---------|
| **地区** | 🇨🇳 中国 | 🇺🇸 美国 | 🇺🇸 美国 | 🇺🇸 美国 |
| **中国可访问** | ✅ 直接访问 | ⚠️ 需代理 | ⚠️ 需代理 | ⚠️ 需代理 |
| **API支持** | ✅ 有API | ✅ 有API | ✅ 有API | ✅ 有API |
| **中文提示词** | ✅ 原生支持 | ⚠️ 有限支持 | ⚠️ 有限支持 | ⚠️ 有限支持 |
| **分辨率** | 720p/1080p | 最高1080p | 最高1080p | 1080p |
| **最大时长** | 10秒 (1.0) / 5秒 (1.5) | 10秒 | 5秒 | 3-5秒 |
| **无水印** | ✅ 支持 | ✅ 支持 | ✅ 支持 | ✅ Pro计划 |
| **定价模式** | 积分制 | 月费/按量 | 按量计费 | 月费 |
| **性价比** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

### 推荐方案

**首选：可灵 Kling API** 🇨🇳
- 中国区直接可访问，无需特殊网络
- 原生中文提示词支持，适合洁博利品牌视频
- API定价合理，积分制灵活
- 1.0版本支持10秒视频，1.5版本画质更好（5秒）
- 支持图生视频（Image-to-Video）

**备选：Runway Gen-3 Alpha** 🌐
- 视频质量业界领先
- 需要API Key和网络配置
- 适合高质量品牌宣传片

---

## 二、架构设计

```
┌─────────────────┐
│  Paperclip Agent │
│  (Claude CLI)    │
└────────┬────────┘
         │ 调用 video_generator.py
         ▼
┌──────────────────────────┐
│  video_generator.py      │
│  ─────────────────────   │
│  - API认证管理           │
│  - 视频生成请求           │
│  - 任务状态轮询           │
│  - 结果下载               │
│  - 错误重试               │
└────────┬────────────────┘
         │ HTTP请求
         ▼
┌──────────────────────────┐
│  Kling API / Runway API  │
│  (云端视频生成服务)       │
└──────────────────────────┘
         │ 文件输出
         ▼
┌──────────────────────────┐
│  ./output/video/         │
│  生成结果存储目录         │
└──────────────────────────┘
```

---

## 三、API密钥配置

在Paperclip环境变量中配置：

```bash
# 可灵 Kling API
export KLING_ACCESS_KEY="your_access_key"
export KLING_SECRET_KEY="your_secret_key"

# 或 Runway API
export RUNWAY_API_KEY="your_runway_key"
```

Kling API密钥申请: https://console.klingai.com (需要注册开发者账号)

---

## 四、Python包装器实现

```python
#!/usr/bin/env python3
"""
Video Generation API Wrapper for Paperclip Platform
Supports: Kling AI (primary), Runway Gen-3 (fallback)

Usage:
    python video_generator.py --prompt "A brand video about smart sensor faucets" --duration 5
    python video_generator.py --prompt "..." --model kling --output ./output/video/
    python video_generator.py --image input.png --prompt "animate this product"  # image-to-video
"""

import os
import sys
import json
import time
import hashlib
import hmac
import base64
import uuid
import requests
from pathlib import Path
from typing import Optional, Dict, Any

# ─── Configuration ───────────────────────────────────────────────

KLING_ACCESS_KEY = os.environ.get("KLING_ACCESS_KEY", "")
KLING_SECRET_KEY = os.environ.get("KLING_SECRET_KEY", "")
RUNWAY_API_KEY = os.environ.get("RUNWAY_API_KEY", "")

DEFAULT_OUTPUT_DIR = Path("./output/video")
DEFAULT_MODEL = "kling"  # kling or runway
DEFAULT_DURATION = 5     # seconds


# ─── Kling API Client ────────────────────────────────────────────

class KlingClient:
    """Kling AI Video Generation API Client"""
    
    BASE_URL = "https://api.klingai.com"
    
    def __init__(self, access_key: str, secret_key: str):
        self.access_key = access_key
        self.secret_key = secret_key
    
    def _generate_signature(self, method: str, path: str, body: str = "") -> Dict[str, str]:
        """Generate HMAC-SHA256 signature for Kling API authentication"""
        timestamp = int(time.time())
        nonce = uuid.uuid4().hex[:16]
        
        # Build signature string
        sign_str = f"{method}\n{path}\n{timestamp}\n{nonce}\n{body}\n"
        
        # Compute HMAC-SHA256
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            sign_str.encode('utf-8'),
            hashlib.sha256
        ).digest()
        signature_b64 = base64.b64encode(signature).decode('utf-8')
        
        return {
            "Content-Type": "application/json",
            "AK": self.access_key,
            "Signature": signature_b64,
            "Timestamp": str(timestamp),
            "Nonce": nonce,
        }
    
    def generate_video(
        self,
        prompt: str,
        model_name: str = "kling-v1",
        duration: int = 5,
        mode: str = "pro",  # pro or std
        image: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        cfg_scale: float = 0.5,
    ) -> Dict[str, Any]:
        """
        Generate video using Kling API
        
        Args:
            prompt: Text description of the video
            model_name: Model version (kling-v1, kling-v1.5)
            duration: Video duration in seconds (5 or 10)
            mode: 'pro' for higher quality, 'std' for standard
            image: Path to input image for image-to-video
            negative_prompt: What to avoid in generation
            cfg_scale: Prompt adherence (0-1)
        
        Returns:
            API response with task_id
        """
        path = "/v1/videos/generate"
        url = f"{self.BASE_URL}{path}"
        
        payload = {
            "model_name": model_name,
            "prompt": prompt,
            "duration": duration,
            "mode": mode,
            "cfg_scale": cfg_scale,
        }
        
        if negative_prompt:
            payload["negative_prompt"] = negative_prompt
        
        if image:
            # Image-to-video: upload image first, then reference
            image_url = self._upload_image(image)
            payload["image"] = image_url
        
        body = json.dumps(payload)
        headers = self._generate_signature("POST", path, body)
        
        response = requests.post(url, headers=headers, data=body, timeout=30)
        result = response.json()
        
        if result.get("code") != 0:
            raise Exception(f"Kling API error: {result.get('message', 'Unknown error')}")
        
        return result["data"]
    
    def query_task(self, task_id: str) -> Dict[str, Any]:
        """Query video generation task status"""
        path = f"/v1/videos/{task_id}"
        url = f"{self.BASE_URL}{path}"
        
        headers = self._generate_signature("GET", path)
        response = requests.get(url, headers=headers, timeout=15)
        result = response.json()
        
        if result.get("code") != 0:
            raise Exception(f"Kling query error: {result.get('message', 'Unknown error')}")
        
        return result["data"]
    
    def wait_for_completion(
        self,
        task_id: str,
        poll_interval: int = 5,
        timeout: int = 600,
    ) -> Dict[str, Any]:
        """Poll until video generation completes"""
        start = time.time()
        while time.time() - start < timeout:
            data = self.query_task(task_id)
            status = data.get("status", "")
            
            if status == "succeed":
                return data
            elif status == "failed":
                raise Exception(f"Video generation failed: {data.get('fail_reason', 'Unknown')}")
            
            # "processing" or "pending" - keep waiting
            time.sleep(poll_interval)
        
        raise TimeoutError(f"Video generation timed out after {timeout}s")
    
    def _upload_image(self, image_path: str) -> str:
        """Upload image for image-to-video generation"""
        path = "/v1/files/upload"
        url = f"{self.BASE_URL}{path}"
        
        file_name = Path(image_path).name
        headers = self._generate_signature("POST", path)
        
        with open(image_path, "rb") as f:
            files = {"file": (file_name, f, "image/png")}
            response = requests.post(url, headers=headers, files=files, timeout=60)
        
        result = response.json()
        if result.get("code") != 0:
            raise Exception(f"Image upload failed: {result.get('message', 'Unknown')}")
        
        return result["data"]["url"]


# ─── Runway API Client ───────────────────────────────────────────

class RunwayClient:
    """Runway Gen-3 API Client (fallback)"""
    
    BASE_URL = "https://api.runwayml.com/v1"
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
    
    def generate_video(
        self,
        prompt: str,
        model: str = "gen3a_turbo",
        duration: int = 5,
    ) -> Dict[str, Any]:
        """Generate video using Runway Gen-3"""
        url = f"{self.BASE_URL}/generations"
        
        payload = {
            "model": model,
            "prompt": prompt,
            "duration": duration,
        }
        
        response = requests.post(url, headers=self.headers, json=payload, timeout=30)
        result = response.json()
        
        if "id" not in result:
            raise Exception(f"Runway API error: {result}")
        
        return result
    
    def query_task(self, generation_id: str) -> Dict[str, Any]:
        """Query video generation status"""
        url = f"{self.BASE_URL}/generations/{generation_id}"
        response = requests.get(url, headers=self.headers, timeout=15)
        return response.json()
    
    def wait_for_completion(
        self,
        generation_id: str,
        poll_interval: int = 10,
        timeout: int = 600,
    ) -> Dict[str, Any]:
        """Poll until video generation completes"""
        start = time.time()
        while time.time() - start < timeout:
            data = self.query_task(generation_id)
            status = data.get("status", "")
            
            if status == "SUCCEEDED":
                return data
            elif status == "FAILED":
                raise Exception(f"Runway generation failed")
            
            time.sleep(poll_interval)
        
        raise TimeoutError(f"Runway generation timed out after {timeout}s")


# ─── Unified Video Generator ─────────────────────────────────────

class VideoGenerator:
    """Unified interface for video generation"""
    
    def __init__(self, model: str = DEFAULT_MODEL):
        self.model = model
        
        if model == "kling":
            if not KLING_ACCESS_KEY or not KLING_SECRET_KEY:
                raise ValueError("KLING_ACCESS_KEY and KLING_SECRET_KEY must be set")
            self.client = KlingClient(KLING_ACCESS_KEY, KLING_SECRET_KEY)
        elif model == "runway":
            if not RUNWAY_API_KEY:
                raise ValueError("RUNWAY_API_KEY must be set")
            self.client = RunwayClient(RUNWAY_API_KEY)
        else:
            raise ValueError(f"Unsupported model: {model}")
    
    def generate(
        self,
        prompt: str,
        duration: int = DEFAULT_DURATION,
        output_dir: str = str(DEFAULT_OUTPUT_DIR),
        image: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Generate video and save result
        
        Returns:
            Dict with task_id, status, video_url, local_path
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        print(f"[VideoGenerator] Starting generation...")
        print(f"  Model: {self.model}")
        print(f"  Prompt: {prompt[:100]}...")
        print(f"  Duration: {duration}s")
        
        # Submit generation task
        if self.model == "kling":
            task = self.client.generate_video(
                prompt=prompt,
                duration=duration,
                image=image,
                **kwargs,
            )
            task_id = task.get("task_id", "")
            print(f"  Task ID: {task_id}")
            
            # Wait for completion
            print(f"  Waiting for completion (this may take 2-10 minutes)...")
            result = self.client.wait_for_completion(task_id)
            
            # Extract video URL
            videos = result.get("videos", [])
            if not videos:
                raise Exception("No videos in response")
            
            video_info = videos[0]
            video_url = video_info.get("url", "")
            
        elif self.model == "runway":
            task = self.client.generate_video(prompt=prompt, duration=duration)
            gen_id = task.get("id", "")
            print(f"  Generation ID: {gen_id}")
            
            print(f"  Waiting for completion...")
            result = self.client.wait_for_completion(gen_id)
            video_url = result.get("output", [{}])[0].get("url", "")
        
        # Download video
        if video_url:
            safe_name = "".join(c for c in prompt[:30] if c.isalnum() or c in " _-").strip()
            timestamp = int(time.time())
            local_file = output_path / f"video_{timestamp}_{safe_name}.mp4"
            
            print(f"  Downloading to: {local_file}")
            resp = requests.get(video_url, timeout=120)
            with open(local_file, "wb") as f:
                f.write(resp.content)
            print(f"  ✅ Saved: {local_file} ({len(resp.content)} bytes)")
        else:
            local_file = None
            print(f"  ⚠️ No video URL in response")
        
        return {
            "task_id": task_id if self.model == "kling" else gen_id,
            "status": "completed",
            "video_url": video_url,
            "local_path": str(local_file) if local_file else None,
            "metadata": result,
        }


# ─── CLI Entry Point ─────────────────────────────────────────────

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate video using AI API")
    parser.add_argument("--prompt", "-p", required=True, help="Video description prompt")
    parser.add_argument("--duration", "-d", type=int, default=5, help="Duration in seconds")
    parser.add_argument("--model", "-m", default="kling", choices=["kling", "runway"], help="API provider")
    parser.add_argument("--output", "-o", default="./output/video", help="Output directory")
    parser.add_argument("--image", "-i", help="Input image for image-to-video")
    parser.add_argument("--negative-prompt", "-n", help="Negative prompt")
    parser.add_argument("--wait", action="store_true", default=True, help="Wait for completion")
    
    args = parser.parse_args()
    
    generator = VideoGenerator(model=args.model)
    result = generator.generate(
        prompt=args.prompt,
        duration=args.duration,
        output_dir=args.output,
        image=args.image,
        negative_prompt=args.negative_prompt,
    )
    
    print(f"\n=== Result ===")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
```

---

## 五、Agent使用示例

### 5.1 文本生视频（品牌视频）

```bash
python video_generator.py \
  --prompt "A modern smart bathroom with sensor faucets, clean white design, professional atmosphere, brand GIBO smart sanitary ware, 4K quality, cinematic lighting" \
  --duration 5 \
  --model kling \
  --output ./output/video/
```

### 5.2 图生视频（产品动画）

```bash
python video_generator.py \
  --image ./assets/images/gibo_faucet_product.png \
  --prompt "The sensor faucet automatically turns on when hands approach, water flows smoothly, blue LED indicator lights up, premium product showcase" \
  --duration 5 \
  --model kling
```

### 5.3 品牌宣传片提示词模板

```bash
python video_generator.py \
  --prompt "Chinese smart sanitary ware factory, automated production line, workers assembling sensor faucets, clean modern workshop, professional manufacturing, warm lighting, brand GIBO, cinematic style" \
  --duration 10
```

---

## 六、品牌视频提示词库（洁博利专用）

| 场景 | 提示词（中文） | 提示词（English） |
|------|---------------|-------------------|
| 工厂航拍 | 现代化智能卫浴工厂全景，蓝色厂房，整洁园区，早晨阳光 | Modern smart sanitary ware factory aerial view, blue buildings, clean campus, morning sunlight |
| 生产线 | 自动化感应水龙头生产线，机械臂装配，品质检测，专业工人 | Automated sensor faucet production line, robotic assembly, quality testing |
| 产品特写 | 感应水龙头特写，手靠近自动出水，蓝色氛围灯，不锈钢质感 | Sensor faucet close-up, hand approaches activates water, blue LED, stainless steel texture |
| 实验室 | CNAS标准实验室，工程师测试产品耐久性，精密仪器 | CNAS-standard lab, engineers testing product durability, precision instruments |
| 办公楼 | 洁博利总部大楼，福州高新区，团队会议，研发讨论 | GIBO headquarters, Fuzhou High-tech Zone, team meeting, R&D discussion |
| 工程项目 | 医院/酒店安装现场，感应水龙头批量安装，工程案例 | Hospital/hotel installation site, batch installation of sensor faucets |
| 品牌历史 | 1999-2025年发展历程动画，从创立到行业标杆 | 1999-2025 timeline animation, from startup to industry leader |

---

## 七、集成检查清单

- [ ] 注册Kling开发者账号 (https://console.klingai.com)
- [ ] 创建API Key：获取 AK (Access Key) + SK (Secret Key)
- [ ] 配置环境变量 `KLING_ACCESS_KEY` 和 `KLING_SECRET_KEY`
- [ ] 安装依赖：`pip install requests`
- [ ] 测试API调用：`python video_generator.py --prompt "test video" --duration 5`
- [ ] 验证视频输出目录 `./output/video/` 文件是否正确
- [ ] 记录API调用成本（Kling约 10-30 积分/次，首次注册赠送积分）
- [ ] 将 `video_generator.py` 纳入Paperclip agent工具链

---

## 八、API成本估算

| 平台 | 计费方式 | 单次成本（5秒视频） | 备注 |
|------|---------|-------------------|------|
| Kling 1.0 (std) | 10积分/次 | ~¥1 | 标准质量，10秒 |
| Kling 1.0 (pro) | 30积分/次 | ~¥3 | 高质量 |
| Kling 1.5 (pro) | 40积分/次 | ~¥4 | 最新模型，5秒 |
| Runway Gen-3 | $0.05/秒 | ~$0.25/次 | 按秒计费 |
| Luma Dream Machine | 30 Credits/次 | ~$0.30/次 | 每月有免费额度 |

> **建议**: 先用Kling 1.0 std模式测试效果，确认后再切换到pro模式。
> 首次注册Kling通常赠送100积分（约10次免费生成）。

---

## 九、API实测记录（2026-06-06）

### 9.1 认证测试结果

| 测试项 | 结果 | 说明 |
|-------|------|------|
| API URL | ✅ `https://api.klingai.com/v1/videos/generate` | 生产环境API端点 |
| 认证方式 | ✅ Bearer AK:Signature | HMAC-SHA256签名放Authorization头 |
| 签名格式 | `Authorization: Bearer {access_key}:{base64_hmac_sha256}` | 已验证通过 |
| 请求方法 | POST | 支持JSON body |
| 认证结果 | ✅ 通过401阶段 | 签名验证通过，请求到达业务层 |

### 9.2 API响应问题

实际测试发现API返回HTTP 500 (code: 1200)，可能原因：

1. **API Key未激活** ⬅️ 最可能
   - 密钥需要先在 [console.klingai.com](https://console.klingai.com) 开发者控制台激活
   - console.klingai.com 当前返回nginx默认页，可能DNS未配置或需额外配置
   
2. **需要IP白名单绑定**
   - Kling API可能要求绑定调用方IP地址
   - 需要在控制台添加当前服务器IP

3. **API版本升级中**
   - 当前端点返回500而非参数校验错误，可能API版本正在迭代

### 9.3 修复后的 `video_generator.py` 变更

| 变更 | 说明 |
|------|------|
| 认证头格式 | `AK+Signature` 独立头 → `Bearer AK:Signature` 统一Authorization头 |
| BASE_URL | `api.klingai.com`（已验证） |
| 错误处理 | 增强JSON错误解析，支持Kling JSON错误体 |
| 请求参数 | 精简payload，移除可能引起500的字段 |

### 9.4 API就绪检查清单

- [ ] 访问 https://console.klingai.com 并登录
- [ ] 检查API Key状态是否active
- [ ] 如需IP白名单，添加当前服务器IP
- [ ] 如控制台不可用，联系Kling技术支持确认API状态
- [ ] 执行验证：`python video_generator.py --prompt "test" --duration 5`

### 9.5 备选方案：Runway Gen-3

如果Kling API长时间不可用，可切换至Runway Gen-3：
```bash
export RUNWAY_API_KEY="your_runway_key"
python video_generator.py --prompt "test video" --model runway
```
Runway API文档：https://docs.runwayml.com