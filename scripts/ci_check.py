#!/usr/bin/env python3
"""GIBO 知识库 CI 校验：死链检测 + 命名合规 + FrontMatter 校验 + Markdown lint。
自包含（仅依赖 Python 标准库），可在 GitHub Actions 或本地运行。
用法：python scripts/ci_check.py [file ...]
  不传参则扫描全仓 .md。传入文件列表则只检查这些文件（用于 PR/push 增量）。
"""
import os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ERRORS, WARNINGS = [], []

LINK_RE = re.compile(r'\[[^\]]*\]\(((?:[^()]|\([^()]*\))*)\)')
IMG_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.S)
REQUIRED_FM = ['lang', 'category', 'summary', 'updated']

def is_external(u):
    return u.startswith('http://') or u.startswith('https://') or u.startswith('//') or u.startswith('mailto:')

# 强校验范围：受管文档（faq/ 子树、仓库根级 .md、scripts/）。
# 其余目录（products/、whitepapers/、solutions/、assets/ 等历史内容）仅 WARN，避免 CI 因遗留文件恒红。
# CI 工作流以"增量（仅本次改动文件）"方式调用本脚本，进一步保证只校验本次变更。
def is_strict(md_path):
    rel = md_path.relative_to(ROOT)
    parts = rel.parts
    if 'assets' in parts:
        return False
    if rel.name.endswith('-backup.md'):
        return False
    if 'faq' in parts:
        return True
    if parts[0] == 'scripts':
        return True
    if len(parts) == 1:  # 仓库根级文档
        return True
    return False

ALLOWED_UPPER = {'README.md','LLMS.md','NAMING-CONVENTION.md','GLOSSARY.md',
                 'MAINTENANCE.md','ROLE-DESCRIPTIONS.md','LICENSE.txt','LICENSE',
                 'NAV.md','CONTRIBUTING.md'}

def strip_code(text):
    # 移除围栏代码块（```...```）与行内代码（`...`），其中的链接/图片按代码处理，
    # 不参与死链校验（避免文档示例中的 ![...](...) 被误判为死链）。
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    text = re.sub(r'`[^`\n]*`', '', text)
    return text

# 受管内容区：这些目录下的图片强制带 alt（见 docs-style-guide 第 8 节）。
# 根级元文档（GLOSSARY/NAMING-CONVENTION/translation-glossary 等）与历史资产不强制，避免噪声。
ALT_MANAGED_ZONES = {'faq', 'products', 'product-spec', 'whitepapers', 'solutions'}
def is_alt_managed(md_path):
    rel = md_path.relative_to(ROOT)
    return bool(set(rel.parts) & ALT_MANAGED_ZONES)

def check_links(md_path, text):
    base = md_path.parent
    text = strip_code(text)
    strict = is_strict(md_path)
    for m in LINK_RE.finditer(text):
        u = m.group(1).strip()
        if not u or u.startswith('#'):
            continue
        if is_external(u):
            continue  # 外部链接不在 CI 内网校验，避免抖动
        target = u.split('#')[0].split('?')[0]
        if not target:
            continue
        if target.startswith('/'):
            p = (ROOT / target.lstrip('/')).resolve()
        else:
            p = (base / target).resolve()
        if not p.exists():
            msg = f"[死链] {md_path.relative_to(ROOT)} -> {u}"
            (ERRORS if strict else WARNINGS).append(msg)
    # 图片缺 alt（仅受管内容区告警，跳过代码块）
    if is_alt_managed(md_path):
        for m in IMG_RE.finditer(strip_code(text)):
            if m.group(1).strip() == '':
                WARNINGS.append(f"[图无alt] {md_path.relative_to(ROOT)} -> {m.group(2)}")

def check_naming(md_path):
    rel = md_path.relative_to(ROOT)
    strict = is_strict(md_path)
    for part in rel.parts:
        if ' ' in part:
            (ERRORS if strict else WARNINGS).append(f"[命名] 含空格: {rel}")
            return
        if re.search(r'[A-Z]', part):
            if part not in ALLOWED_UPPER:
                (ERRORS if strict else WARNINGS).append(f"[命名] 含大写字母: {rel}")
                return

def check_fm(md_path, text):
    if '/faq/' not in str(md_path):
        return
    m = FM_RE.match(text)
    if not m:
        ERRORS.append(f"[FM] 缺 FrontMatter: {md_path.relative_to(ROOT)}")
        return
    fm = m.group(1)
    for key in REQUIRED_FM:
        if not re.search(rf'^{key}\s*:', fm, re.M):
            ERRORS.append(f"[FM] 缺字段 {key}: {md_path.relative_to(ROOT)}")

def check_md_lint(md_path, text):
    for i, line in enumerate(text.splitlines(), 1):
        if line != line.rstrip():
            WARNINGS.append(f"[lint] 行尾空格 {md_path.relative_to(ROOT)}:{i}")

def main():
    args = sys.argv[1:]
    if args:
        files = [Path(a).resolve() for a in args if a.endswith('.md')]
        # 跳过已删除（不存在）的文件，避免 PR/删除场景下误报读取失败
        files = [f for f in files if f.exists()]
    else:
        files = sorted(ROOT.rglob('*.md'))
        files = [f for f in files if '.git' not in f.parts and 'archive' not in f.parts]
    for f in files:
        try:
            text = f.read_text(encoding='utf-8')
        except Exception as e:
            WARNINGS.append(f"[读取失败] {f.relative_to(ROOT)}: {e}")
            continue
        check_links(f, text)
        check_naming(f)
        check_fm(f, text)
        check_md_lint(f, text)
    print(f"扫描文件: {len(files)}")
    print(f"ERROR: {len(ERRORS)}  WARNING: {len(WARNINGS)}")
    for e in ERRORS[:200]:
        print("  ✗", e)
    if WARNINGS:
        for w in WARNINGS[:60]:
            print("  ⚠", w)
    if ERRORS:
        print("\nCI 校验未通过，请修复上述 ERROR。")
        sys.exit(1)
    print("\nCI 校验通过 ✓")
    sys.exit(0)

if __name__ == '__main__':
    main()
