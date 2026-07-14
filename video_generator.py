#!/usr/bin/env python3
"""
Video Generation API Wrapper for Paperclip Platform
Supports: Kling AI (primary), Runway Gen-3 (fallback)
Uses only Python standard library (no external dependencies)

Usage:
    python video_generator.py --prompt "A brand video about smart sensor faucets" --duration 5
    python video_generator.py --prompt "..." --model kling --output ./output/video/
"""

import os
import sys
import json
import time
import hashlib
import hmac
import base64
import uuid
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional, Dict, Any

# ─── Configuration ───────────────────────────────────────────────

KLING_ACCESS_KEY = os.environ.get("KLING_ACCESS_KEY", "")
KLING_SECRET_KEY = os.environ.get("KLING_SECRET_KEY", "")
RUNWAY_API_KEY = os.environ.get("RUNWAY_API_KEY", "")

DEFAULT_OUTPUT_DIR = Path("./output/video")
DEFAULT_MODEL = "kling"
DEFAULT_DURATION = 5


# ─── HTTP Helper ─────────────────────────────────────────────────

def _http_request(method: str, url: str, headers: dict = None,
                  body: bytes = None, timeout: int = 30) -> Dict:
    """Simple HTTP request using standard library"""
    if headers is None:
        headers = {}

    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read().decode('utf-8')
            return json.loads(data)
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8') if e.fp else str(e)
        return {"code": e.code, "message": error_body}
    except urllib.error.URLError as e:
        return {"code": -1, "message": f"Connection error: {e.reason}"}


# ─── JWT Helper ──────────────────────────────────────────────────

def _b64url_encode(data: bytes) -> str:
    """Base64url encode without padding"""
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')


def _generate_kling_jwt(access_key: str, secret_key: str) -> str:
    """Generate JWT token for Kling API (HS256)"""
    header = _b64url_encode(json.dumps({"alg": "HS256", "typ": "JWT"}).encode('utf-8'))
    payload_data = {
        "iss": access_key,
        "exp": int(time.time()) + 1800,
        "nbf": int(time.time()) - 5,
    }
    payload = _b64url_encode(json.dumps(payload_data, separators=(',', ':')).encode('utf-8'))
    signature = hmac.new(
        secret_key.encode('utf-8'),
        f"{header}.{payload}".encode('utf-8'),
        hashlib.sha256
    ).digest()
    sig_b64 = _b64url_encode(signature)
    return f"{header}.{payload}.{sig_b64}"


# ─── Kling API Client ────────────────────────────────────────────

class KlingClient:
    """Kling AI Video Generation API Client"""

    BASE_URL = "https://openapi.klingai.com"

    def __init__(self, access_key: str, secret_key: str):
        self.access_key = access_key
        self.secret_key = secret_key

    def _get_auth_headers(self) -> Dict[str, str]:
        """Generate JWT Bearer auth headers for Kling API"""
        token = _generate_kling_jwt(self.access_key, self.secret_key)
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

    def generate_video(
        self,
        prompt: str,
        model_name: str = "kling-v1-6",
        duration: int = 5,
        mode: str = "pro",
        resolution: str = "720p",
        **kwargs,
    ) -> Dict[str, Any]:
        """Submit video generation task"""
        path = "/v1/videos/text2video"
        url = f"{self.BASE_URL}{path}"

        payload = {
            "model_name": model_name,
            "prompt": prompt,
            "duration": duration,
            "mode": mode,
            "resolution": resolution,
            "cfg": kwargs.get("cfg", 0.5),
        }

        body = json.dumps(payload).encode('utf-8')
        headers = self._get_auth_headers()

        result = _http_request("POST", url, headers=headers, body=body, timeout=30)

        if result.get("code", 0) != 0:
            err_code = result.get("code", "unknown")
            err_msg = result.get("message", "Unknown error")
            raise Exception(f"Kling API error ({err_code}): {err_msg}")

        return result.get("data", {})

    def query_task(self, task_id: str) -> Dict[str, Any]:
        """Query video generation task status"""
        path = f"/v1/videos/{task_id}"
        url = f"{self.BASE_URL}{path}"

        headers = self._get_auth_headers()
        result = _http_request("GET", url, headers=headers, timeout=15)

        if result.get("code", 0) != 0:
            err_code = result.get("code", "unknown")
            err_msg = result.get("message", "Unknown error")
            raise Exception(f"Kling query error ({err_code}): {err_msg}")

        return result.get("data", {})

    def wait_for_completion(self, task_id: str, poll_interval: int = 5,
                            timeout: int = 600) -> Dict[str, Any]:
        """Poll until video generation completes"""
        start = time.time()
        while time.time() - start < timeout:
            data = self.query_task(task_id)
            status = data.get("status", "")

            if status == "succeed":
                return data
            elif status == "failed":
                reason = data.get('fail_reason', 'Unknown')
                raise Exception(f"Video generation failed: {reason}")

            elapsed = int(time.time() - start)
            status_msg = data.get("task_status_msg", "processing")
            print(f"  [{elapsed}s] Status: {status} - {status_msg}")
            time.sleep(poll_interval)

        raise TimeoutError(f"Video generation timed out after {timeout}s")


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

    def generate_video(self, prompt: str, model: str = "gen3a_turbo",
                       duration: int = 5) -> Dict[str, Any]:
        """Submit video generation task"""
        url = f"{self.BASE_URL}/generations"
        payload = json.dumps({
            "model": model,
            "prompt": prompt,
            "duration": duration,
        }).encode('utf-8')

        result = _http_request("POST", url, headers=self.headers,
                               body=payload, timeout=30)

        if "id" not in result:
            raise Exception(f"Runway API error: {result}")
        return result

    def query_task(self, generation_id: str) -> Dict[str, Any]:
        """Query task status"""
        url = f"{self.BASE_URL}/generations/{generation_id}"
        return _http_request("GET", url, headers=self.headers, timeout=15)

    def wait_for_completion(self, generation_id: str, poll_interval: int = 10,
                            timeout: int = 600) -> Dict[str, Any]:
        """Poll until complete"""
        start = time.time()
        while time.time() - start < timeout:
            data = self.query_task(generation_id)
            status = data.get("status", "")

            if status == "SUCCEEDED":
                return data
            elif status == "FAILED":
                raise Exception("Runway generation failed")

            print(f"  [{int(time.time()-start)}s] Status: {status}")
            time.sleep(poll_interval)

        raise TimeoutError(f"Generation timed out")


# ─── Video Download Helper ───────────────────────────────────────

def _download_file(url: str, local_path: Path, timeout: int = 120) -> bool:
    """Download file from URL to local path"""
    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
            local_path.parent.mkdir(parents=True, exist_ok=True)
            with open(local_path, "wb") as f:
                f.write(data)
        return True
    except Exception as e:
        print(f"  ⚠️ Download failed: {e}")
        return False


# ─── Unified Video Generator ─────────────────────────────────────

class VideoGenerator:
    """Unified interface for video generation"""

    def __init__(self, model: str = DEFAULT_MODEL):
        self.model = model

        if model == "kling":
            if not KLING_ACCESS_KEY or not KLING_SECRET_KEY:
                raise ValueError(
                    "ERROR: KLING_ACCESS_KEY and KLING_SECRET_KEY must be set.\n"
                    "  export KLING_ACCESS_KEY='your_access_key'\n"
                    "  export KLING_SECRET_KEY='your_secret_key'"
                )
            self.client = KlingClient(KLING_ACCESS_KEY, KLING_SECRET_KEY)
        elif model == "runway":
            if not RUNWAY_API_KEY:
                raise ValueError(
                    "ERROR: RUNWAY_API_KEY must be set.\n"
                    "  export RUNWAY_API_KEY='your_runway_key'"
                )
            self.client = RunwayClient(RUNWAY_API_KEY)
        else:
            raise ValueError(f"Unsupported model: {model}. Choose 'kling' or 'runway'.")

    def generate(self, prompt: str, duration: int = DEFAULT_DURATION,
                 output_dir: str = str(DEFAULT_OUTPUT_DIR),
                 **kwargs) -> Dict[str, Any]:
        """
        Generate video and save result

        Returns:
            Dict with task status, video URL, local file path
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        print(f"\n{'='*50}")
        print(f"🎬 Video Generator - {self.model.upper()}")
        print(f"{'='*50}")
        print(f"  Prompt:   {prompt[:80]}{'...' if len(prompt)>80 else ''}")
        print(f"  Duration: {duration}s")

        # Submit generation
        print(f"\n  🚀 Submitting task...")
        if self.model == "kling":
            task = self.client.generate_video(
                prompt=prompt, duration=duration, **kwargs)
            task_id = task.get("task_id", "")
            print(f"  Task ID:  {task_id}")

            # Wait
            print(f"  ⏳ Generating (may take 2-10 min)...")
            result = self.client.wait_for_completion(task_id)

            videos = result.get("videos", result.get("task_result", {}).get("videos", []))
            if not videos:
                raise Exception("No videos in API response")

            video_url = videos[0].get("url", "")
        else:
            task = self.client.generate_video(prompt=prompt, duration=duration)
            gen_id = task.get("id", "")
            print(f"  Gen ID:   {gen_id}")
            print(f"  ⏳ Generating...")
            result = self.client.wait_for_completion(gen_id)
            video_url = result.get("output", [{}])[0].get("url", "")

        # Download
        local_file = None
        if video_url:
            safe_name = "".join(c for c in prompt[:40] if c.isalnum() or c in " _-").strip()
            timestamp = int(time.time())
            local_file = output_path / f"video_{timestamp}_{safe_name[:30]}.mp4"

            print(f"  📥 Downloading...")
            success = _download_file(video_url, local_file)
            if success:
                size = local_file.stat().st_size
                print(f"  ✅ Saved: {local_file} ({size/1024:.0f} KB)")
            else:
                print(f"  ⚠️ Could not download video")
                local_file = None
        else:
            print(f"  ⚠️ No video URL in response")

        return {
            "task_id": task_id if self.model == "kling" else gen_id,
            "status": "completed",
            "video_url": video_url,
            "local_path": str(local_file) if local_file else None,
        }


# ─── CLI Entry Point ─────────────────────────────────────────────

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate AI video using Kling or Runway API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic text-to-video (Kling)
  python video_generator.py --prompt "sensor faucet product demo"

  # Longer duration
  python video_generator.py --prompt "brand commercial" --duration 10

  # Use Runway (requires RUNWAY_API_KEY)
  python video_generator.py --prompt "product animation" --model runway

  # Custom output directory
  python video_generator.py --prompt "factory tour" --output ./videos
        """
    )

    parser.add_argument("--prompt", "-p", required=True,
                       help="Video description prompt")
    parser.add_argument("--duration", "-d", type=int, default=5,
                       choices=[5, 10],
                       help="Video duration in seconds (5 or 10)")
    parser.add_argument("--model", "-m", default="kling",
                       choices=["kling", "runway"],
                       help="API provider (default: kling)")
    parser.add_argument("--output", "-o", default="./output/video",
                       help="Output directory (default: ./output/video)")

    args = parser.parse_args()

    try:
        generator = VideoGenerator(model=args.model)
        result = generator.generate(
            prompt=args.prompt,
            duration=args.duration,
            output_dir=args.output,
        )

        print(f"\n{'='*50}")
        print("✅ Generation Complete")
        print(f"{'='*50}")
        print(f"  Task ID:    {result.get('task_id', 'N/A')}")
        print(f"  Status:     {result.get('status', 'N/A')}")
        print(f"  Video URL:  {result.get('video_url', 'N/A')}")
        print(f"  Local Path: {result.get('local_path', 'N/A')}")

        # Create a lightweight result JSON for agent consumption
        result_file = Path(args.output) / f"result_{result.get('task_id', 'unknown')}.json"
        result_file.parent.mkdir(parents=True, exist_ok=True)
        with open(result_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"  Result:     {result_file}")
        print()

    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()