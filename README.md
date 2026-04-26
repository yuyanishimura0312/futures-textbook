# 未来を読む力 — 現代未来学の理論と実践

企業人・社会人のためのフォーサイト入門。NPO法人ミラツク編。

## 概要

- 対象: 日本のビジネスパーソン、社会実践者、政策立案者
- 分量: 約200,000字（20章）
- 形式: HTML + PDF出力対応
- CI: ミラツクブランド（NOSIGNERデザイン、暖色系アーストーン）

## 構成

| Part | テーマ | 章 | 字数目標 |
|------|--------|------|----------|
| I | 未来学への招待 | 1-3 | 35,000字 |
| II | 未来を探る手法 | 4-9 | 55,000字 |
| III | 未来を考えるフレームワーク | 10-13 | 35,000字 |
| IV | 未来と社会 | 14-17 | 35,000字 |
| V | 実践する未来学 | 18-20 | 40,000字 |

## ファイル構造

```
futures-textbook/
  index.html              -- 目次ページ
  plan.md                 -- 制作計画（全20章の詳細設計）
  assets/
    css/
      textbook.css        -- メインスタイルシート
      print.css           -- PDF出力用スタイル
    images/
      miratuku-logo.png   -- ミラツクロゴ
  chapters/
    ch01.html             -- 第1章: なぜ未来を考えるのか
    ch02.html             -- 第2章以降（順次執筆）
    ...
  data/                   -- データファイル格納用
```

## データソース

- Futures Studies Knowledge DB: 326研究者, 90手法, 211概念, 17学派, 40論争
- Textbook DB: 93テキスト, 38大学プログラム

## 開発

ローカルで確認:
```bash
cd ~/projects/apps/futures-textbook
python3 -m http.server 8080
# http://localhost:8080 でアクセス
```

PDF出力: ブラウザの印刷機能 (Cmd+P) でPDFに保存。print.css が自動適用される。

## ライセンス

Copyright NPO法人ミラツク. All rights reserved.
