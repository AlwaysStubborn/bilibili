# 本目录说明（vendored）

上游项目：[Janson20/BiliCommentBot](https://github.com/Janson20/BiliCommentBot)（MIT）  
用途：监控**自己账号视频**下的新评论，调用 DeepSeek 自动回复。

本仓库在 `bili-comment-bot/` 内嵌该项目，便于在当前分支上继续改。相对上游的本地改动：

- `server.py`：支持用环境变量覆盖密钥（`DEEPSEEK_API_KEY`、`BILIBILI_COOKIE` 等）
- 默认模型改为 `deepseek-chat`
- 默认 system prompt 改为通用友善回复

## 快速启动

```bash
cd bili-comment-bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp config.example.toml config.toml
# 编辑 config.toml，或导出环境变量后再启动
python main.py
```

浏览器打开 `http://127.0.0.1:5000`，也可用 Web UI 扫码登录与改配置。

### 推荐环境变量

```bash
export DEEPSEEK_API_KEY="sk-..."
export DEEPSEEK_MODEL="deepseek-chat"
# 可选：export BILIBILI_COOKIE="SESSDATA=...; bili_jct=..."
# 可选：export BILIBILI_UID="你的UID"
```

`config.toml`、Cookie、history 等已在 `.gitignore` 中，勿提交密钥。

## 合规提醒

请遵守 B 站用户协议与社区规范；注意限频，避免骚扰与垃圾评论。本工具面向**自己稿件评论区**的自动回复场景。
