# ClaudeCodeTraining

民泊運営会社向け Claude Code 研修用の **会社専用 Claude** 雛形リポジトリ。

このリポジトリを各メンバーが手元に取り込むと、`CLAUDE.md` ／ スキル ／ MCP 設定が同期され、全員が同じ前提で Claude Code を使えるようになります。

## ディレクトリ構成

```
ClaudeCodeTraining/
├── CLAUDE.md                 # 全員共通の事業ルール・用語・禁則
├── .mcp.json                 # MCPサーバー接続定義（Google Drive など）
├── .claude/
│   ├── settings.json         # 権限・環境変数・MCP有効化など共通設定
│   └── skills/               # 共通スキル
│       └── property-name-check.md
├── data/
│   ├── master/               # 物件マスタ・勘定科目マスタ
│   │   ├── properties.csv
│   │   └── accounts.csv
│   └── samples/              # 演習用サンプルデータ（架空）
│       └── reservations_2026-04.csv
└── scripts/                  # Python ユーティリティ
```

## 使い始め方

1. このリポジトリを `git clone` で手元に取り込む
2. VSCode で開く
3. Claude Code 拡張から会話を開始すると、`CLAUDE.md` とスキルが自動で読み込まれる

## サンプル予約データについて

`data/samples/` 配下は **架空の予約データ** です。物件名・ゲスト名・金額はすべて研修用に生成されたもので、実在しません。

## 注意事項

- 本番の宿泊者情報・財務情報は **絶対にこのリポジトリに置かないでください**
- スキルやルールの追加は Pull Request を経由してマージしてください
