# 3500Words

高考英语词汇课堂抽背 App（**HarmonyOS 7 ArkTS** + **Android Kotlin**）。

共享词库：`content/curated/`  
Unit 目录（每 Unit 50 词）：`content/catalog/units.json`  
抽题/判分契约：`docs/QUIZ_SPEC.md`  
抽查分段：前 25 / 后 25 / 整 Unit

## 快速开始

```powershell
# 从老师文档提取原始条目
python tools/extract_docx.py --docx "C:\Users\WHO\Downloads\Unit词汇练习提取.docx"

# 生成 review 草稿（可接 LLM；默认离线 stub）
python tools/ai_enrich.py

# 校验已抽检词库
python tools/validate_content.py

# 同步到双端
powershell -ExecutionPolicy Bypass -File scripts/sync_content_to_apps.ps1
```

## 工程

- `android/` — Kotlin + Jetpack Compose MVP（用 Android Studio 打开）
- `harmony/` — ArkTS + ArkUI（用 DevEco Studio 打开；遵守 ArkTS skill）
- `content/` — 词库流水线（`curated` 为双端真源）
- `docs/` — 产品与规格（含 `QUIZ_SPEC.md`）

## 契约回归

```powershell
python tools/run_grade_fixtures.py
python tools/validate_content.py
```

## 当前进度

- Phase 0：共享 schema / Unit42 金标 / 提取与校验脚本 — 完成
- Phase 1 MVP：双端抽背主路径骨架 — 完成（需本机 IDE 编译运行）
- 内容：docx 已提取到 `content/raw` + `content/review`；仅 Unit42 已人工金标入 `curated`
