#!/usr/bin/env python3
"""Convert all 20 textbook chapters to miratuku-news-v2 report style."""
import re, os, glob

CHAPTERS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "chapters")

# The CSS template matching miratuku-news-v2 reports (genius-childhood-patterns.html etc.)
REPORT_CSS = """
:root {
  --bg: #FFFFFF;
  --bg-alt: #FAFAF8;
  --card: #FFFFFF;
  --text: #121212;
  --text-secondary: #555555;
  --text-muted: #6B6B6B;
  --border: #D9D9D9;
  --border-light: #EEEEEE;
  --surface: #F7F7F5;
  --accent: #CC1400;
  --accent-muted: rgba(204,20,0,0.06);
  --accent-blue: #1565c0;
  --accent-green: #2e7d32;
  --accent-orange: #e65100;
  --serif: 'Noto Serif JP', serif;
  --sans: 'Noto Sans JP', sans-serif;
}
[data-theme="dark"] {
  --bg: #0D0D0D;
  --bg-alt: #141414;
  --card: #1A1A1A;
  --text: #E0E0E0;
  --text-secondary: #AAAAAA;
  --text-muted: #777777;
  --border: #333333;
  --border-light: #222222;
  --surface: #1E1E1E;
  --accent: #FF4444;
  --accent-muted: rgba(255,68,68,0.08);
  --accent-blue: #64b5f6;
  --accent-green: #66bb6a;
  --accent-orange: #ffb74d;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: var(--sans);
  background: var(--bg);
  color: var(--text);
  font-size: 15px;
  line-height: 1.9;
  -webkit-font-smoothing: antialiased;
}
.theme-toggle {
  position: fixed; top: 16px; right: 16px; z-index: 100;
  width: 36px; height: 36px; border-radius: 50%;
  border: 1px solid var(--border); background: var(--card);
  cursor: pointer; display: flex; align-items: center; justify-content: center;
  font-size: 16px;
}
.print-btn {
  position: fixed; top: 16px; right: 60px; z-index: 100;
  padding: 6px 14px; border-radius: 6px;
  border: 1px solid var(--border); background: var(--card);
  cursor: pointer; font-size: 0.72rem; color: var(--text-muted);
  font-family: var(--sans);
}
.report-header {
  background: var(--bg-alt);
  border-bottom: 1px solid var(--border-light);
  padding: 48px 24px 40px;
}
.report-header-inner {
  max-width: 740px;
  margin: 0 auto;
}
.report-back {
  font-size: 0.75rem;
  color: var(--text-muted);
  text-decoration: none;
  display: inline-block;
  margin-bottom: 24px;
}
.report-back:hover { color: var(--accent); }
.report-meta-top {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}
.report-badge {
  display: inline-block;
  padding: 2px 8px;
  background: var(--accent);
  color: #fff;
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.04em;
}
.report-date {
  font-size: 0.75rem;
  color: var(--text-muted);
  letter-spacing: 0.03em;
}
.report-title {
  font-family: var(--serif);
  font-size: 1.65rem;
  font-weight: 700;
  line-height: 1.4;
  margin-bottom: 12px;
}
.report-subtitle {
  font-size: 0.88rem;
  color: var(--text-secondary);
  line-height: 1.7;
  max-width: 640px;
}
.article {
  max-width: 740px;
  margin: 0 auto;
  padding: 48px 24px 80px;
}
.section-num {
  display: block;
  font-family: var(--serif);
  font-size: 0.72rem;
  color: var(--accent);
  font-weight: 700;
  letter-spacing: 0.06em;
  margin-bottom: 4px;
}
h2.article-h2 {
  font-family: var(--serif);
  font-size: 1.25rem;
  font-weight: 700;
  line-height: 1.4;
  margin: 56px 0 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--border-light);
}
h2.article-h2:first-of-type { margin-top: 0; }
h3.article-h3 {
  font-family: var(--serif);
  font-size: 1.02rem;
  font-weight: 700;
  line-height: 1.5;
  margin: 40px 0 14px;
}
.article p {
  margin-bottom: 18px;
  font-size: 0.92rem;
  line-height: 1.9;
  text-align: justify;
}
.pullquote {
  margin: 32px 0;
  padding: 20px 24px;
  border-left: 3px solid var(--accent);
  background: var(--accent-muted);
  font-family: var(--serif);
  font-size: 0.95rem;
  line-height: 1.8;
}
.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.78rem;
  margin: 20px 0;
}
.data-table th {
  background: var(--surface);
  padding: 8px 10px;
  text-align: left;
  font-weight: 600;
  border-bottom: 2px solid var(--border);
  font-size: 0.72rem;
  color: var(--text-secondary);
}
.data-table td {
  padding: 8px 10px;
  border-bottom: 1px solid var(--border-light);
  vertical-align: top;
  line-height: 1.5;
}
.data-table tr:hover td { background: var(--accent-muted); }
.insight-box {
  margin: 24px 0;
  padding: 18px 20px;
  border-left: 3px solid var(--accent-orange);
  background: rgba(230,81,0,0.03);
}
[data-theme="dark"] .insight-box { background: rgba(255,183,77,0.04); }
.insight-label {
  font-family: var(--serif);
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--accent-orange);
  margin-bottom: 8px;
}
.callout, .callout-concept, .callout-case, .callout-person, .callout-practice {
  margin: 24px 0;
  padding: 18px 20px;
  border-left: 3px solid var(--accent-blue);
  background: rgba(21,101,192,0.04);
  font-size: 0.88rem;
  line-height: 1.8;
}
.callout-title, .callout h4 {
  font-family: var(--serif);
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--accent-blue);
  margin-bottom: 8px;
}
.chapter-nav {
  max-width: 740px;
  margin: 0 auto;
  padding: 0 24px 40px;
  display: flex;
  justify-content: space-between;
  gap: 16px;
}
.chapter-nav a {
  font-size: 0.8rem;
  color: var(--accent);
  text-decoration: none;
  padding: 8px 16px;
  border: 1px solid var(--border);
  border-radius: 6px;
}
.chapter-nav a:hover {
  background: var(--accent-muted);
  border-color: var(--accent);
}
.report-footer {
  max-width: 740px;
  margin: 0 auto;
  padding: 0 24px 60px;
  border-top: 1px solid var(--border);
}
.report-footer p {
  font-size: 0.75rem;
  color: var(--text-muted);
  line-height: 1.7;
  margin-top: 16px;
}
svg { max-width: 100%; height: auto; }
@media print {
  .theme-toggle, .print-btn, .chapter-nav, .report-back { display: none; }
  body { font-size: 10pt; line-height: 1.6; }
  .report-header { padding: 24px; }
  .article { padding: 24px; }
  h2.article-h2 { page-break-after: avoid; }
  .pullquote, .insight-box, .callout, svg { page-break-inside: avoid; }
}
@media (max-width: 600px) {
  .report-title { font-size: 1.3rem; }
  .chapter-nav { flex-direction: column; }
}
"""

CHAPTER_TITLES = {
    1: ("なぜ未来を考えるのか", "不確実な時代の航海術"),
    2: ("未来学の80年史", "RANDからアンティシペーションまで"),
    3: ("未来は「予測」できるか", "フューチャーズ・コーンと認識論"),
    4: ("環境スキャニングと弱いシグナル", "変化の兆しを捉える"),
    5: ("シナリオプランニング入門", "不確実性と向き合う"),
    6: ("デルファイ法と集合知", "専門家の知恵を集める"),
    7: ("システム思考とレバレッジポイント", "複雑さを理解する"),
    8: ("因果階層分析（CLA）", "深層構造を掘り下げる"),
    9: ("創造的手法", "未来を「つくる」"),
    10: ("スリーホライズン", "変化の時間構造を読む"),
    11: ("バックキャスティングとビジョニング", "望ましい未来から逆算する"),
    12: ("メガトレンドと不確実性", "大きな流れを掴む"),
    13: ("四つの汎用的未来像", "あらゆる未来を分類する"),
    14: ("将来世代への責任", "世代間公正の思想"),
    15: ("誰のための未来か", "権力・公正・脱植民地"),
    16: ("持続可能な未来", "惑星限界と社会的転換"),
    17: ("テクノロジーと人間の未来", "AI・バイオ・ポストヒューマン"),
    18: ("企業フォーサイト", "組織に未来思考を埋め込む"),
    19: ("政策フォーサイトと市民参加", "社会の未来を共に考える"),
    20: ("あなたの未来力を鍛える", "フューチャーズリテラシーへ"),
}

PART_NAMES = {
    1: "Part I 未来学への招待", 2: "Part I 未来学への招待", 3: "Part I 未来学への招待",
    4: "Part II 未来を探る手法", 5: "Part II 未来を探る手法", 6: "Part II 未来を探る手法",
    7: "Part II 未来を探る手法", 8: "Part II 未来を探る手法", 9: "Part II 未来を探る手法",
    10: "Part III フレームワーク", 11: "Part III フレームワーク",
    12: "Part III フレームワーク", 13: "Part III フレームワーク",
    14: "Part IV 未来と社会", 15: "Part IV 未来と社会",
    16: "Part IV 未来と社会", 17: "Part IV 未来と社会",
    18: "Part V 実践する未来学", 19: "Part V 実践する未来学", 20: "Part V 実践する未来学",
}


def extract_body_content(html):
    """Extract the main prose content from a chapter HTML, stripping old headers/nav/css."""
    # Remove everything before the main content
    # Try to find article/main content area
    body_match = re.search(r'<body[^>]*>(.*)</body>', html, re.DOTALL)
    if not body_match:
        return ""
    body = body_match.group(1)

    # Remove old theme toggle, print buttons, nav elements
    body = re.sub(r'<button[^>]*class="theme-toggle"[^>]*>.*?</button>', '', body, flags=re.DOTALL)
    body = re.sub(r'<button[^>]*class="print-btn"[^>]*>.*?</button>', '', body, flags=re.DOTALL)
    body = re.sub(r'<button[^>]*onclick="window\.print\(\)"[^>]*>.*?</button>', '', body, flags=re.DOTALL)

    # Remove old header sections (various patterns)
    body = re.sub(r'<header[^>]*>.*?</header>', '', body, flags=re.DOTALL)
    body = re.sub(r'<div[^>]*class="[^"]*chapter-header[^"]*"[^>]*>.*?</div>\s*</div>', '', body, flags=re.DOTALL)
    body = re.sub(r'<div[^>]*class="[^"]*chapter-hero[^"]*"[^>]*>.*?</div>\s*</div>', '', body, flags=re.DOTALL)

    # Remove old navigation
    body = re.sub(r'<nav[^>]*class="[^"]*chapter-nav[^"]*"[^>]*>.*?</nav>', '', body, flags=re.DOTALL)
    body = re.sub(r'<div[^>]*class="[^"]*chapter-nav[^"]*"[^>]*>.*?</div>', '', body, flags=re.DOTALL)

    # Remove old footer
    body = re.sub(r'<footer[^>]*>.*?</footer>', '', body, flags=re.DOTALL)

    # Remove script tags
    body = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.DOTALL)

    # Try to extract just the article content
    article_match = re.search(r'<(?:div|main|article)[^>]*class="[^"]*(?:article|content|chapter-content|chapter-body)[^"]*"[^>]*>(.*?)(?:</div>|</main>|</article>)\s*(?:<(?:nav|div|footer)|\Z)', body, re.DOTALL)
    if article_match:
        return article_match.group(1).strip()

    # Fallback: return cleaned body
    body = body.strip()
    return body


def build_chapter(num, body_content):
    """Build a complete chapter HTML in miratuku-news-v2 report style."""
    title, subtitle = CHAPTER_TITLES[num]
    part = PART_NAMES[num]

    prev_link = ""
    next_link = ""
    if num > 1:
        prev_title = CHAPTER_TITLES[num-1][0]
        prev_link = f'<a href="ch{num-1:02d}.html">&larr; {prev_title}</a>'
    else:
        prev_link = '<a href="https://yuyanishimura0312.github.io/miratuku-news-v2/textbook.html">&larr; 目次に戻る</a>'

    if num < 20:
        next_title = CHAPTER_TITLES[num+1][0]
        next_link = f'<a href="ch{num+1:02d}.html">{next_title} &rarr;</a>'
    else:
        next_link = '<a href="https://yuyanishimura0312.github.io/miratuku-news-v2/textbook.html">目次に戻る &rarr;</a>'

    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>第{num}章 {title} | 未来を読む力</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@400;700&display=swap" rel="stylesheet">
<style>{REPORT_CSS}</style>
</head>
<body>
<button class="theme-toggle" onclick="document.documentElement.dataset.theme=document.documentElement.dataset.theme==='dark'?'':'dark'" aria-label="テーマ切替">&#9681;</button>
<button class="print-btn" onclick="window.print()">Print / PDF</button>

<header class="report-header">
<div class="report-header-inner">
<a href="https://yuyanishimura0312.github.io/miratuku-news-v2/textbook.html" class="report-back">&larr; 未来を読む力 — 目次</a>
<div class="report-meta-top">
<span class="report-badge">TEXTBOOK</span>
<span class="report-date">{part}</span>
</div>
<h1 class="report-title">第{num}章 {title}</h1>
<p class="report-subtitle">{subtitle}</p>
</div>
</header>

<div class="article">
{body_content}
</div>

<div class="chapter-nav">
{prev_link}
{next_link}
</div>

<footer class="report-footer">
<p>「未来を読む力 — 現代未来学の理論と実践」NPO法人ミラツク 編<br>
Futures Studies Knowledge DB（448研究者・99手法・507概念）に基づく</p>
</footer>

</body>
</html>'''


def process_chapter(num):
    filepath = os.path.join(CHAPTERS_DIR, f"ch{num:02d}.html")
    if not os.path.exists(filepath):
        print(f"  ch{num:02d}.html: MISSING")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    body = extract_body_content(html)
    if not body or len(body) < 500:
        print(f"  ch{num:02d}.html: WARNING - body too short ({len(body)} chars), keeping original content area")
        # Fallback: try to keep everything between first <p> and last </p>
        body_match = re.search(r'<body[^>]*>(.*)</body>', html, re.DOTALL)
        if body_match:
            body = body_match.group(1)
            # Strip known non-content elements
            body = re.sub(r'<button[^>]*>.*?</button>', '', body, flags=re.DOTALL)
            body = re.sub(r'<header[^>]*>.*?</header>', '', body, flags=re.DOTALL)
            body = re.sub(r'<nav[^>]*>.*?</nav>', '', body, flags=re.DOTALL)
            body = re.sub(r'<footer[^>]*>.*?</footer>', '', body, flags=re.DOTALL)
            body = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.DOTALL)
            body = body.strip()

    new_html = build_chapter(num, body)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

    # Count Japanese chars
    text = re.sub(r'<[^>]+>', '', body)
    ja_chars = len([c for c in text if ord(c) > 0x3000])
    print(f"  ch{num:02d}.html: converted ({ja_chars}字)")


if __name__ == "__main__":
    print("Converting all 20 chapters to miratuku-news-v2 report style...")
    os.makedirs(CHAPTERS_DIR, exist_ok=True)
    for i in range(1, 21):
        process_chapter(i)
    print("\nDone. All chapters converted.")
