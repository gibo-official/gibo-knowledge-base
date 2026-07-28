#!/usr/bin/env python3
"""GIBO 知识库语义互链生成器。
基于标签共现 + 正文内容余弦相似 + 分类 + 标题重叠，为 zh / en 内容文档
注入"关联文档 / Related Documents"互链板块，消除信息孤岛。
- 仅同语言互链（zh<->zh, en<->en），符合"中英文分开维护"决策。
- 已含关联文档板块的文档保留人工策展链接，不覆盖。
- 链接使用相对路径，CI 死链校验可通过。

用法：python scripts/build_related_links.py [--dry-run] [--top N]
"""
import os, re, math, json, argparse
from pathlib import Path
from collections import Counter

ROOT = Path(r"D:/Github/gibo-knowledge-base")
REL_RE = re.compile(r'(关联文档|相关阅读|相关文档|Related Documents|Related Reading|相关文章)')
FOOTER_RE = re.compile(r'^>\s*\*{0,2}数据来源说明')

ZN_STOP = set("我们 你们 他们 她们 它们 自己 这个 那个 这些 那些 什么 怎么 可以 通过 进行 使用 一个 一种 以及 对于 由于 因此 就是 还是 因为 所以 如果 或者 并且 而且 然而 此外 同时 目前 已经 可能 应该 需要 一般 主要 常见 不同 各种 如下 以上 以下 之间 之后 之前 能够 方面 本文 本节 贵司 客户 其中 然后 这样 那样 一些 每个 各项 其它 各自 分别 例如 比如 具有 采用 实现 基于 根据 关于 用于 适用 满足 符合 简介 概述 支持 提供 包括 这种 时候".split())
EN_STOP = set("the a an and or of to in on for with is are was were be been being this that these those it its as at by from we you they he she our your their can will may should could would do does did has have had not no yes i'm we're etc into out up down over under between within without about more most other another such same any all each both few many much one two three".split())

def tokenize(text):
    toks = []
    for m in re.finditer(r'[A-Za-z0-9_]+', text):
        w = m.group().lower()
        if len(w) >= 2 and w not in EN_STOP:
            toks.append(w)
    for m in re.finditer(r'[一-鿿]+', text):
        s = m.group()
        if len(s) >= 2:
            for i in range(len(s) - 1):
                bg = s[i:i+2]
                if bg not in ZN_STOP:
                    toks.append('c:' + bg)
    return toks

def parse_fm(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        return {}, None
    fm = m.group(1)
    out = {'tags': [], 'category': '', 'title': ''}
    # tags (inline or block)
    lines = fm.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('tags:'):
            rest = line[len('tags:'):].strip()
            if rest.startswith('['):
                inner = rest.strip('[]')
                for mm in re.finditer(r'"([^"]*)"|\'([^\']*)\'|([^,\s]+)', inner):
                    t = mm.group(1) or mm.group(2) or mm.group(3)
                    if t:
                        out['tags'].append(t.strip())
            else:
                i += 1
                while i < len(lines) and re.match(r'\s*-\s+(.*)$', lines[i]):
                    t = re.match(r'\s*-\s+(.*)$', lines[i]).group(1).strip().strip('"\'')
                    if t:
                        out['tags'].append(t)
                    i += 1
                i -= 1
        elif line.startswith('category:'):
            out['category'] = line[len('category:'):].strip().strip('"\'')
        elif line.startswith('title:'):
            out['title'] = line[len('title:'):].strip().strip('"\'')
        i += 1
    return out, m.end()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--top', type=int, default=5)
    args = ap.parse_args()

    files = sorted(ROOT.glob('zh/**/*.md')) + sorted(ROOT.glob('en/**/*.md'))
    docs = []
    for f in files:
        rel = f.relative_to(ROOT)
        lang = rel.parts[0]
        text = f.read_text(encoding='utf-8')
        if REL_RE.search(text):
            continue  # 已有互链板块，保留人工策展
        fm, end = parse_fm(text)
        body = text[end:] if end else text
        body_clean = re.sub(r'```.*?```', '', body, flags=re.S)
        body_clean = re.sub(r'`[^`\n]*`', '', body_clean)
        toks = tokenize(body_clean)
        title = fm['title'] or (re.search(r'^#\s+(.+)$', body, re.M) or [None, f.stem]).group(1) if fm['title'] else (re.search(r'^#\s+(.+)$', body, re.M).group(1) if re.search(r'^#\s+(.+)$', body, re.M) else f.stem)
        title_tok = set(tokenize(title))
        docs.append({
            'path': f, 'rel': str(rel).replace('\\', '/'), 'lang': lang,
            'category': fm['category'], 'tags': set(fm['tags']),
            'title': title, 'title_tok': title_tok,
            'tokens': toks, 'cands': [],
        })

    by_lang = {'zh': [], 'en': []}
    for d in docs:
        by_lang.setdefault(d['lang'], []).append(d)

    # idf + tfidf
    df = Counter()
    for d in docs:
        for t in set(d['tokens']):
            df[t] += 1
    N = len(docs)
    for d in docs:
        tf = Counter(d['tokens'])
        vec = {}
        for t, c in tf.items():
            idf = math.log((N - df[t] + 0.5) / (df[t] + 0.5) + 1)
            vec[t] = c * idf
        norm = math.sqrt(sum(v * v for v in vec.values()))
        if norm > 0:
            vec = {t: v / norm for t, v in vec.items()}
        d['vec'] = vec

    # pairwise within language
    for lang, lst in by_lang.items():
        n = len(lst)
        for a in range(n):
            da = lst[a]
            for b in range(a + 1, n):
                db = lst[b]
                small, big = (da['vec'], db['vec']) if len(da['vec']) < len(db['vec']) else (db['vec'], da['vec'])
                dot = 0.0
                for t, v in small.items():
                    if t in big:
                        dot += v * big[t]
                shared = da['tags'] & db['tags']
                cat_match = 1 if da['category'] and da['category'] == db['category'] else 0
                title_ov = len(da['title_tok'] & db['title_tok'])
                score = 10 * len(shared) + 2 * cat_match + 1 * title_ov + 3 * dot
                has_strong = bool(shared) or cat_match or title_ov > 0
                eligible = has_strong or dot >= 0.10
                if eligible:
                    da['cands'].append((db['path'], db['title'], score, dot, len(shared)))
                    db['cands'].append((da['path'], da['title'], score, dot, len(shared)))

    # build links + inject
    injected = 0
    skipped_no_cand = 0
    samples = []
    for d in docs:
        d['cands'].sort(key=lambda x: (-x[2], -x[3]))
        top = d['cands'][:args.top]
        if not top:
            skipped_no_cand += 1
            continue
        base = d['path'].parent
        links = []
        for cp, ct, sc, dot, sh in top:
            rp = os.path.relpath(cp, base).replace('\\', '/')
            links.append((ct, rp))
        if args.dry_run:
            if len(samples) < 40:
                samples.append((d['rel'], d['lang'], [(ct, rp, round(dot,3), sh) for ct, rp, sc, dot, sh in top]))
            continue
        # inject blockquote
        block = ('> **关联文档**：' if d['lang'] == 'zh' else '> **Related Documents**: ') + \
                ' | '.join(f'[{ct}]({rp})' for ct, rp in links)
        text = d['path'].read_text(encoding='utf-8')
        lines = text.split('\n')
        footer_idx = None
        for i, l in enumerate(lines):
            if FOOTER_RE.match(l):
                footer_idx = i
                break
        # trim trailing blank lines helper
        def build(new_before, rest_lines):
            while new_before and new_before[-1].strip() == '':
                new_before.pop()
            new_before.append('')
            new_before.append(block)
            new_before.append('')
            return new_before + rest_lines
        if footer_idx is not None:
            new = build(lines[:footer_idx], lines[footer_idx:])
        else:
            new = build(lines[:], [])
        d['path'].write_text('\n'.join(new), encoding='utf-8')
        injected += 1

    print(f"docs considered (no existing related section): {len(docs)}")
    print(f"injected: {injected}  skipped(no candidates): {skipped_no_cand}")
    print(f"lang split -> zh:{len(by_lang['zh'])} en:{len(by_lang['en'])}")
    if args.dry_run:
        print("\n=== DRY RUN samples ===")
        for rel, lang, links in samples:
            print(f"\n[{lang}] {rel}")
            for ct, rp, dot, sh in links:
                print(f"   - ({'tag×'+str(sh) if sh else 'cos='+str(dot)}) {ct} -> {rp}")

if __name__ == '__main__':
    main()
