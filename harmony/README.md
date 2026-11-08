# HarmonyOS 工程（ArkTS）

DevEco Studio 打开 `harmony/` 目录。代码遵循仓库 `docs/ARKTS_CONSTRAINTS.md`。

## 打开方式

1. 安装 **DevEco Studio**（API 12+ / HarmonyOS 5 兼容配置，按本机 SDK 可再调 `compatibleSdkVersion`）
2. 打开本目录，等待 ohpm/hvigor 同步
3. 真机或模拟器运行 `entry`

词库：`entry/src/main/resources/rawfile/content/`

## 已实现

- 与 Android 相同的抽背主路径（中译英/填空/混合/错题）
- 判分与 QUIZ_SPEC 对齐
- 错题本（Preferences）
- TTS 预留（避免 SDK 差异阻断编译）
