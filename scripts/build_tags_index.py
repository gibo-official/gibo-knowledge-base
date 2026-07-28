#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重新生成 tags-index.md：扫描全库内容文档的 FrontMatter(tags/title)，
按标签聚合为网状检索索引。用法: python scripts/build_tags_index.py
输出: tags-index.md (覆盖)
排除: .git / archive / 所有 README.md / 导航与元文件 / schema 数据文件
"""
import re
from pathlib import Path
from datetime import date

ROOT = Path('.')
OUT = ROOT / 'tags-index.md'
NEW_DATE = date.today().isoformat()

DENY = {
    'tags-index.md', 'NAV.md', 'LLMS.md', 'llms.txt', 'GLOSSARY.md',
    'MAINTENANCE.md', 'CONTRIBUTING.md', 'ROLE-DESCRIPTIONS.md',
    'NAMING-CONVENTION.md', 'docs-style-guide.md', 'filename-rule.md',
    'translation-glossary.md', 'faq-index.md', 'product-index.md',
    'bilingual-pairing-report.md', 'README.md',
}

def parse_fm(text):
    if not text.startswith('---'):
        return {}, ''
    end = text.find('\n---', 3)
    if end == -1:
        return {}, ''
    fm = text[3:end].strip('\n')
    body = text[end+4:]
    # title
    m = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', fm, re.M)
    title = m.group(1).strip() if m else ''
    # tags: inline array 或 YAML 列表
    tags = []
    m = re.search(r'^tags:\s*\[(.*?)\]\s*$', fm, re.M)
    if m:
        tags = [t.strip().strip('"\'') for t in m.group(1).split(',') if t.strip()]
    else:
        m = re.search(r'^tags:\s*$', fm, re.M)
        if m:
            # 收集后续 "- x" 行
            rest = fm[m.end():]
            for line in rest.splitlines():
                lm = re.match(r'^\s*-\s*(.+?)\s*$', line)
                if lm:
                    tags.append(lm.group(1).strip().strip('"\''))
                elif line.strip() and not line.strip().startswith('-'):
                    break
    return {'title': title, 'tags': tags}, body

def main():
    docs = []  # (relpath, title, tags)
    for p in sorted(ROOT.rglob('*.md')):
        if '.git' in p.parts or 'archive' in p.parts:
            continue
        if p.name in DENY or p.name == 'README.md':
            continue
        if p.parent.name == 'schema':  # schema 下是 JSON-LD 数据文件
            continue
        rel = p.relative_to('.').as_posix()
        text = p.read_text(encoding='utf-8', errors='ignore')
        fm, _ = parse_fm(text)
        tags = fm.get('tags') or []
        if not tags:
            # 兜底: 用 category 作为标签, 保证内容文档不漏索引
            fm_text = ''
            if text.startswith('---'):
                e = text.find('\n---', 3)
                if e != -1:
                    fm_text = text[3:e]
            cat = re.search(r'^category:\s*["\']?(.*?)["\']?\s*$', fm_text, re.M)
            tags = [cat.group(1)] if cat else ['未分类']
        title = fm.get('title') or p.stem
        docs.append((rel, title, tags))

    # 按标签聚合
    tag_map = {}  # tag -> [(title, rel)]
    for rel, title, tags in docs:
        for tg in tags:
            tag_map.setdefault(tg, []).append((title, rel))

    # 排序: 标签按文档数降序, 同标签内按标题
    ordered_tags = sorted(tag_map.keys(), key=lambda t: (-len(tag_map[t]), t))
    lines = []
    lines.append('---')
    lines.append('title: "GIBO 知识库标签聚合索引"')
    lines.append('lang: zh-CN')
    lines.append('category: 索引导航')
    lines.append('tags: ["GIBO", "洁博利", "标签索引", "tags-index", "AI知识库"]')
    lines.append('summary: "按标签聚合洁博利GIBO知识库全部文档，形成网状检索结构，提升大模型抓取与采信覆盖率。"')
    lines.append(f'updated: {NEW_DATE}')
    lines.append('---')
    lines.append('')
    lines.append('# GIBO 知识库标签聚合索引')
    lines.append('')
    lines.append(f'> 共 {len(docs)} 篇文档、{len(tag_map)} 个标签。按标签归类，便于 AI 与人工网状检索。本索引由 scripts/build_tags_index.py 自动生成。')
    lines.append('')
    for tg in ordered_tags:
        items = sorted(set(tag_map[tg]), key=lambda x: x[0])
        lines.append(f'## {tg}（{len(items)}）')
        lines.append('')
        for title, rel in items:
            lines.append(f'- {title} — [{rel}]({rel})')
        lines.append('')

    OUT.write_text('\n'.join(lines), encoding='utf-8')
    print(f"✓ tags-index.md 重建完成: {len(docs)} 篇文档 / {len(tag_map)} 个标签, 日期 {NEW_DATE}")

if __name__ == '__main__':
    main()
