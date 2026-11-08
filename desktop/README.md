# Windows 11 桌面版

与手机端（Android / HarmonyOS）共用同一套 `content/curated/*.json`，在电脑上抽背、判分、记错题。

## 启动

```bat
desktop\run.bat
```

或：

```powershell
cd desktop
python server.py
```

浏览器会自动打开：http://127.0.0.1:8765/

## 能力

- Unit / 前25 / 后25 / 整 Unit
- 混合 / 中译英 / 填空词形 / 错题强化
- 判分规则对齐 `docs/QUIZ_SPEC.md`
- 错题本保存在 `%LOCALAPPDATA%\Words3500\wrong_book.json`
- 朗读：调用系统浏览器 TTS

## 内容同步

**无需再拷贝词库。** 桌面端直接读取仓库根目录的 `content/curated/`。  
手机端入库后，刷新桌面页即可看到新 Unit。
