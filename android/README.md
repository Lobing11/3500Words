# Android 工程

Kotlin + Jetpack Compose MVP。

## 打开方式

1. 用 **Android Studio** 打开 `android/` 目录
2. Sync Gradle
3. 运行 `app` 到模拟器/真机

词库来自 `app/src/main/assets/content/`（由根目录 `scripts/sync_content_to_apps.ps1` 同步）。

## 已实现

- Unit 选择
- 中译英 / 填空 / 混合 / 错题
- 判分（对齐 QUIZ_SPEC）
- 错题本（SharedPreferences）
- 系统 TTS 发音
