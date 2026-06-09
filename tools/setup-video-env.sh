#!/bin/bash
# Paperclip 视频生成 - 环境变量配置
# 使用方式: source tools/setup-video-env.sh

# Kling API 凭据 (JWT认证)
export KLING_AK="ADdJ3CK4ggafndth4edyfrabrK9YK9kA"
export KLING_SK="FN3KYRe3Npd8KK3bFtenCHpJDgMDJB8J"

# Python包装器兼容
export KLING_ACCESS_KEY="$KLING_AK"
export KLING_SECRET_KEY="$KLING_SK"

echo "✅ 视频生成环境变量已配置"
echo "   API: openapi.klingai.com (JWT auth)"
echo "   工具: node tools/video-generate.mjs --prompt \"...\""
echo "   或:   python video_generator.py --prompt \"...\""
