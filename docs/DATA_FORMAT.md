# 数据格式

## 目录

- `content/catalog/` — **Unit 权威目录**（`3500.txt` → `units.json`，60 Unit × 50 词）
- `content/raw/` — docx 提取的原始条目（可无答案）
- `content/review/` — AI 补答案草稿，待人工抽检
- `content/curated/` — 已抽检、可上架词库（双端唯一真源）；`manifest.json` 列出全部 60 Unit
- `content/schemas/` — JSON Schema
- `content/fixtures/` — 判分回归用例

### Unit 切分规则

1. 严格按目录：Unit N = `(rangeFrom—rangeTo)`，约 50 个中心词
2. 抽查时粗分为两小份：`1-25` / `26-50`
3. 考点条目应带 `segment` 字段；老师材料里的「Unit xx 1-25 / 26-50」直接映射

## Unit 文件

路径：`content/curated/unit_42.json`

```json
{
  "unitId": "42",
  "name": "Unit 42",
  "order": 42,
  "items": [ /* QuizItem */ ]
}
```

## 流水线

```text
docx → tools/extract_docx.py → raw
    → tools/classify_items.py → typed raw
    → tools/ai_enrich.py → review
    → 人工抽检
    → tools/validate_content.py → curated
    → scripts/sync_content_to_apps.ps1 → android assets + harmony rawfile
```

## 自定义导入 CSV（Phase3）

列：`unitId,type,prompt,answerPrimary,answerAlts,hint,relatedGroupId`

`answerAlts` 用 `;` 分隔。
