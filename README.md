# 未来を拓く力 — フューチャーズ・スタディーズ入門

ビジネスパーソンと実践者のための未来学テキストブック。NPO法人ミラツク発行。

## 概要

- 対象: 日本のビジネスパーソン、社会実践者、政策立案者
- 分量: 約200,000字（20章）
- 形式: HTML + PDF出力対応
- CI: ミラツクブランド（NOSIGNER デザイン）

## 構成

| Part | テーマ | 章 | 字数目標 |
|------|--------|------|----------|
| I | 未来学とは何か | 1-3 | 40,000字 |
| II | 未来学の認識論 | 4-6 | 30,000字 |
| III | 未来学の手法 | 7-13 | 60,000字 |
| IV | 未来学の倫理と実践 | 14-17 | 40,000字 |
| V | 未来学の最前線 | 18-20 | 30,000字 |

## ファイル構造

```
futures-textbook/
  index.html          -- 目次ページ
  plan.md             -- 制作計画
  assets/
    miratuku-logo.png  -- ミラツクロゴ
  chapters/
    ch01.html          -- 第1章
    ch02.html          -- 第2章（予定）
    ...
```

## データソース

- Futures Studies Knowledge DB: 168研究者, 69手法, 145概念, 17学派, 40論争
- Textbook DB: 93テキスト, 38大学プログラム（`~/projects/research/futures-studies-db/textbooks.db`）

## 開発

ローカルで確認:
```bash
cd ~/projects/apps/futures-textbook
python3 -m http.server 8080
# http://localhost:8080 でアクセス
```

## ライセンス

Copyright NPO法人ミラツク. All rights reserved.
