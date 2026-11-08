# HarmonyOS ArkTS 实现约束

本仓库鸿蒙代码遵循用户 ArkTS skill 的硬约束，重点包括：

- 禁止 `any` / `unknown` / `@ts-ignore` / `var`
- 所有函数显式返回类型；异步返回 `Promise<T>`
- 对象用 `class` 建模，避免无类型裸字面量
- 禁止 `delete`、动态 `obj["x"]`（`Record` 除外）、`for...in`、正则字面量
- `build()` 内禁止本地变量、`switch`、三目、`console`
- 同一组件不混用 V1/V2 状态装饰器
- `catch (e)` 不标注类型，随后 `as Error`
- JSON 解析按 `Record<string, Object>` 逐字段断言

判分逻辑与 Android 共用 `docs/QUIZ_SPEC.md`，用 `tools/run_grade_fixtures.py` 做契约回归。
