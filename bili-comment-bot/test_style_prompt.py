#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验：根据历史回复样本拼提示词。"""
import sys
from bot import BiliCommentBot, DEFAULT_SYSTEM_PROMPT


def main() -> int:
    samples = [
        {"text": "确实，这波有点抽象", "source": "reply_feed", "peer": "up主这操作绝了"},
        {"text": "哈哈我人还在", "source": "own_video"},
        {"text": "？你才是", "source": "reply_feed", "peer": "你是AI吧"},
        {"text": "懂了，下次注意", "source": "history"},
    ]
    prompt = BiliCommentBot.build_system_prompt_from_samples(samples, example_limit=4)
    failed = 0
    if "历史回复" not in prompt:
        print("FAIL missing 历史回复 block")
        failed += 1
    if "确实，这波有点抽象" not in prompt:
        print("FAIL missing sample text")
        failed += 1
    if "对方「up主这操作绝了」" not in prompt:
        print("FAIL missing peer pair")
        failed += 1
    if "绝不承认" not in prompt:
        print("FAIL missing AI denial rule")
        failed += 1
    empty = BiliCommentBot.build_system_prompt_from_samples([])
    if empty != DEFAULT_SYSTEM_PROMPT:
        print("FAIL empty samples should fallback to default")
        failed += 1

    # usable filter
    bot = object.__new__(BiliCommentBot)
    if bot._is_usable_style_sample("我是AI助手"):
        print("FAIL should reject AI confession sample")
        failed += 1
    if bot._is_usable_style_sample("哈哈哈"):
        print("FAIL should reject trivial sample")
        failed += 1
    if not bot._is_usable_style_sample("确实有点离谱"):
        print("FAIL should accept normal sample")
        failed += 1

    if failed:
        print(f"{failed} failed")
        return 1
    print("ok: style prompt from history")
    return 0


if __name__ == "__main__":
    sys.exit(main())
