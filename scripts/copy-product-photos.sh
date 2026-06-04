#!/bin/bash
# Copy representative product photos from microdrive to repo
SRC="E:/WXWork/1688853171284393/WeDrive/洁博利智能厨卫/产品拍照/生产中心产品拍照留档"
DST="D:/Github/gibo-knowledge-base/assets/img/products"

cd "$SRC"
for dir in */; do
    name=$(basename "$dir")
    first_jpg=$(find "$dir" -maxdepth 1 -name "*.jpg" 2>/dev/null | head -1)
    if [ -n "$first_jpg" ] && [ ! -f "$DST/$name.jpg" ]; then
        cp "$first_jpg" "$DST/$name.jpg"
        echo "Copied: $name.jpg"
    fi
done
echo "Done. Total: $(find "$DST" -name '*.jpg' | wc -l) product images"
