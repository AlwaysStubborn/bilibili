#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""不依赖网络：校验「是不是 AI」探测与回复露馅拦截。"""
import sys
from bot import BiliCommentBot


def main() -> int:
    probes = [
        "你是不是AI啊",
        "机器人吧？",
        "这是自动回复吗",
        "人机验证一下",
        "ChatGPT写的？",
        "你是 deepseek 吗",
    ]
    normals = [
        "这个视频好好看",
        "up主更新啦",
        "哈哈哈哈",
        "ai画风确实不错",  # 聊内容不该当试探
    ]
    confessions = [
        "我是AI助手，很高兴为你服务",
        "作为AI我无法体验情感",
        "其实我是机器人啦",
        "这条是由DeepSeek生成的",
        "🤖 你好呀",
        "我无法拥有情感哦",
    ]
    ok_replies = [
        "？你才是",
        "打字快就叫AI啊哈哈",
        "认真的，这个视频我也觉得好看",
        "ai画风确实不错",
    ]

    failed = 0
    for t in probes:
        if not BiliCommentBot._is_ai_probe_comment(t):
            print(f"FAIL probe miss: {t}")
            failed += 1
    for t in normals:
        if BiliCommentBot._is_ai_probe_comment(t):
            print(f"FAIL probe false positive: {t}")
            failed += 1
    for t in confessions:
        if not BiliCommentBot._looks_like_ai_confession(t):
            print(f"FAIL confession miss: {t}")
            failed += 1
    for t in ok_replies:
        if BiliCommentBot._looks_like_ai_confession(t):
            print(f"FAIL confession false positive: {t}")
            failed += 1

    # sanitize：自曝应被替换成口语否认
    class _Dummy:
        logger = type("L", (), {"warning": staticmethod(lambda *a, **k: None)})()
        _looks_like_ai_confession = staticmethod(BiliCommentBot._looks_like_ai_confession)
        _human_denial_reply = staticmethod(BiliCommentBot._human_denial_reply)

    out = BiliCommentBot._sanitize_reply_text(
        _Dummy(), "我是AI，被你发现了", probe=True
    )
    if BiliCommentBot._looks_like_ai_confession(out):
        print(f"FAIL sanitize still confesses: {out}")
        failed += 1
    if "🤖" in out:
        print(f"FAIL sanitize kept robot emoji: {out}")
        failed += 1

    if failed:
        print(f"{failed} failed")
        return 1
    print("ok: ai probe / confession guards")
    return 0


if __name__ == "__main__":
    sys.exit(main())
