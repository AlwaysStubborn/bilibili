# bilibili

B 站评论/数据相关工具仓库。当前主体为内嵌的 [BiliCommentBot](https://github.com/Janson20/BiliCommentBot)（MIT）。

## 目录

- [`bili-comment-bot/`](bili-comment-bot/) — DeepSeek 自动回复；支持「自己视频评论区」与消息中心「回复我的」（跨视频）；含 Web UI

更细的说明见 [`bili-comment-bot/README.md`](bili-comment-bot/README.md) 与 [`bili-comment-bot/SETUP.md`](bili-comment-bot/SETUP.md)。

## 快速启动

```bash
cd bili-comment-bot
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS / Linux:
# source .venv/bin/activate
pip install -r requirements.txt
copy config.example.toml config.toml   # Windows
# cp config.example.toml config.toml   # macOS / Linux
python main.py
```

浏览器打开 `http://127.0.0.1:5000`，在 Web UI 中扫码登录、配置后启动。

Windows 若控制台报编码错误，可先设置：

```powershell
$env:PYTHONIOENCODING='utf-8'
$env:PYTHONUTF8='1'
```

## 合规

请遵守 B 站用户协议与社区规范；注意限频。本工具面向自己稿件评论区、以及别人回复你评论后的自动回应等合法使用场景。

## 许可证

见根目录 [LICENSE](LICENSE)（与 `bili-comment-bot/LICENSE` 一致，上游 BiliCommentBot MIT）。
