# 3500Words

高考英语词汇课堂抽背 App（**HarmonyOS 7 ArkTS** + **Android Kotlin** + **Windows 桌面**）。

共享词库：`content/curated/`  
Unit 目录（每 Unit 50 词）：`content/catalog/units.json`  
抽题/判分契约：`docs/QUIZ_SPEC.md`  
抽查分段：前 25 / 后 25 / 整 Unit

## Windows 桌面版

直接读仓库 `content/curated/`（与手机端内容一致，无需再同步拷贝）：

```bat
desktop\run.bat
```

浏览器打开 http://127.0.0.1:8765/ 即可抽背。

## 内容升级入口（长期保留）

缺 Unit 的练习材料时：**不凭空写入 `curated`**。你补文档后，按同一条流水线晋升：

```text
老师 Unit 词汇练习.docx
  → tools/extract_docx.py     → content/raw/unit_XX.jsonl
  → tools/ai_enrich.py        → content/review/（补答案草稿）
  → 人工抽检 / promote 脚本     → content/curated/unit_XX.json
  → tools/validate_content.py
  → scripts/sync_content_to_apps.ps1   # 安卓/鸿蒙；桌面直读 curated
```

约定：
- **目录范围**仍看 `content/catalog/units.json`（50 词 / `1-25`·`26-50`）
- **检测内容**必须来自老师练习考点（zh2en 词组、cloze、word_form、pattern、phrase_cluster 拆题），不是词表释义
- `manifest.hasContent=true` 只对已抽检单元；未补材料的 Unit 保持待入库
- 旧的词典式 AI 草稿若需对照：`content/review/ai_dictionary_draft/`（不作为上架源）

## 快速开始

```powershell
# 从老师文档提取原始条目（可重复跑；新 Unit 会追加/覆盖对应 raw）
python tools/extract_docx.py --docx "C:\Users\WHO\Downloads\Unit词汇练习提取.docx"

# 生成 review 草稿（可接 LLM；默认离线 stub）
python tools/ai_enrich.py

# 校验已抽检词库
python tools/validate_content.py

# 同步到双端（先清空再拷贝，避免旧 unit 残留）
powershell -ExecutionPolicy Bypass -File scripts/sync_content_to_apps.ps1
```

## 工程

- `android/` — Kotlin + Jetpack Compose MVP（用 Android Studio 打开）
- `harmony/` — ArkTS + ArkUI（用 DevEco Studio 打开；遵守 ArkTS skill）
- `desktop/` — Windows 本地抽背（Python 小服务 + 网页 UI）
- `content/` — 词库流水线（`curated` 为各端真源；`raw`/`review` 为升级入口）
- `docs/` — 产品与规格（含 `QUIZ_SPEC.md`）
- `tools/` — `extract_docx.py` / `ai_enrich.py` / `promote_lib.py` / `validate_content.py`

## 契约回归

```powershell
python tools/run_grade_fixtures.py
python tools/validate_content.py
```

## 当前进度

- Phase 0：共享 schema / Unit42 金标 / 提取与校验脚本 — 完成
- Phase 1 MVP：双端抽背主路径骨架 — 完成（需本机 IDE 编译运行）
- 内容：老师 docx 已晋升 **Unit 42–45、47–55、57–59**；**1–41 / 46 / 56 / 60** 待你补材料后走升级入口
