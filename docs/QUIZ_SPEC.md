# QUIZ_SPEC — 双端抽背契约

Android (Kotlin) 与 HarmonyOS (ArkTS) 必须按本规格实现判分与抽题，保证同一输入得到同一 verdict。

## 题型

| type | 说明 |
|------|------|
| `zh2en` | 中文提示 → 英文短语/句型 |
| `cloze` | 英文挖空（介词/搭配） |
| `word_form` | 词形变化填空 |
| `phrase_cluster` | 短语簇中的一项（同 `relatedGroupId` 连考） |
| `pattern` | 句型/语法结构 |

## 规范化 normalize(s)

1. `trim`
2. 连续空白压成单个空格
3. 转小写
4. 去掉首尾标点：`.?!;:,`
5. 将中文省略号/`…` 视为无关（仅用于展示，不参与比较）

## 判分 grade(item, userInput)

### 单答案题（zh2en / phrase_cluster / pattern / 无 blanks 的 cloze）

- 候选集 = `[answerPrimary] + answerAlts`
- 若 `normalize(userInput)` 等于任一候选的 `normalize` → `correct`
- 否则 → `wrong`

### 多空题（blanks 非空）

- 用户答案按 `|` 或换行拆成多段，段数应 ≥ blanks 数；不足则 `wrong`
- 第 i 空候选 = `[blanks[i].answer] + blanks[i].alts`
- 全对 → `correct`；部分对 → `partial`；全错 → `wrong`

### partial 处理

- 计入错题本，但 `wrongWeight` 为 0.5（相对 wrong 的 1.0）

## 抽题

### 范围（严格对齐目录）

- 权威目录：`content/catalog/units.json`（源自桌面 `3500.txt`）
- **每个 Unit = 50 个中心词**，带首尾词区间，例如 Unit 42 = `pour—progress`
- 抽查分段 `segment`：
  - `1-25`：该 Unit 前 25 词对应考点
  - `26-50`：该 Unit 后 25 词对应考点
  - `all`：整 Unit
- 过滤优先用条目字段 `segment`；若缺失，则按 items 顺序对半切分

### 模式

| mode | 规则 |
|------|------|
| `zh2en` | 仅 type=zh2en |
| `cloze` | type in {cloze, word_form} |
| `mixed` | 全类型按权重随机：zh2en 3, cloze 3, word_form 2, phrase_cluster 2, pattern 1 |
| `wrong_only` | 本地 wrongBook 中未掌握项 |
| `cluster` | 同一 relatedGroupId 连续出完再下一组 |
| `family` | 相邻 word_form / 同 hint lemma 连续 2–5 题 |

### 会话

- 默认题量 25，可配置 10/25/50
- 可重复抽（MVP 允许）；Phase2 SRS 再去重优先

## SRS（Phase2）

- 答对：interval 升档 1 → 3 → 7 → 14 天
- 答错/partial：回到 1 天，记入错题
- `nextReviewAt` 到期优先进入题池

## 回归夹具

见 `content/fixtures/grade_cases.json`：两端应用同一用例断言 verdict。
