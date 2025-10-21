#!/usr/bin/env python3
import argparse
import os
import sys
import subprocess

try:
    import markdown
except ImportError:
    print("錯誤：需要安裝 python-markdown。執行：pip install markdown", file=sys.stderr)
    sys.exit(2)

HTML_TEMPLATE = """<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{title}</title>
  <style>
    body{{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial;margin:2rem auto;max-width:900px;padding:1rem;color:#222}}
    pre{{background:#f7f7f7;padding:1rem;border-radius:6px;overflow:auto}}
    code{{background:#f0f0f0;padding:.1rem .3rem;border-radius:4px}}
    hr{{border:none;border-top:1px solid #eee;margin:2rem 0}}
  </style>
</head>
<body>
{body}
</body>
</html>
"""

def title_from_markdown(md_text, fallback):
    for line in md_text.splitlines():
        line = line.strip()
        if line.startswith('#'):
            return line.lstrip('#').strip()
    return fallback

def convert(md_path, out_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    title = title_from_markdown(md_text, os.path.basename(md_path))
    html_body = markdown.markdown(md_text, extensions=['fenced_code', 'tables', 'toc'])
    html = HTML_TEMPLATE.format(title=title, body=html_body)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    return out_path

def open_with_browser(path):
    browser = os.environ.get('BROWSER')
    if not browser:
        print("未設定 $BROWSER，無法自動開啟。")
        return
    try:
        subprocess.Popen([browser, path])
    except Exception as e:
        print(f"開啟失敗：{e}")

def main():
    p = argparse.ArgumentParser(description="把 Markdown 轉成 HTML")
    p.add_argument("markdown", help="來源 Markdown 檔案路徑")
    p.add_argument("-o", "--output", help="輸出 HTML 檔案（預設為同名 .html）")
    p.add_argument("--open", action="store_true", help="轉換後用 $BROWSER 開啟輸出檔案")
    args = p.parse_args()

    md_path = args.markdown
    if not os.path.isfile(md_path):
        print(f"找不到檔案：{md_path}", file=sys.stderr)
        sys.exit(1)

    out_path = args.output or os.path.splitext(md_path)[0] + ".html"
    try:
        out = convert(md_path, out_path)
        print(f"已輸出：{out}")
        if args.open:
            open_with_browser(out)
    except Exception as e:
        print(f"轉換失敗：{e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()