# 本目录说明（vendored）

上游项目：[Janson20/BiliCommentBot](https://github.com/Janson20/BiliCommentBot)（MIT）  
用途：调用 DeepSeek 自动回复 B 站评论，支持两种模式：

1. **自己视频**：监控自己投稿视频下的新评论并回复  
2. **回复我的**：监控消息中心「回复我的」，别人回复你在任意视频下的评论时自动回（首次启用只追新通知）

本仓库在 `bili-comment-bot/` 内嵌该项目，便于在当前分支上继续改。相对上游的本地改动：

- `server.py`：支持用环境变量覆盖密钥（`DEEPSEEK_API_KEY`、`BILIBILI_COOKIE` 等）
- 默认模型改为 `deepseek-chat`
- 默认 system prompt 改为通用友善回复
- 双模式：`reply.own_videos_enabled` / `reply.reply_to_me_enabled`
- 去 AI 味默认提示词；对方问「是不是AI」时强制口语否认，并拦截自曝回复；防刷：`per_user_interval` / `daily_ai_limit` / `skip_trivial`（无对外 API，不做 IP 黑白名单）
- 默认回复前缀为空（勿用 🤖，评论区会直接露馅）

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
