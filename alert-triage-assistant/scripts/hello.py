"""W1D1 Mission 4: a three-turn conversation where YOU carry the history.

    uv run scripts/hello.py             # full history resent every call
    uv run scripts/hello.py --stripped  # only the latest user message: can it recall C-104?

Needs ANTHROPIC_API_KEY in the environment (never in the repo).
"""
import os
import sys

import anthropic

MODEL = os.environ.get("CCDV_MODEL", "claude-sonnet-5-5")
STRIPPED = "--stripped" in sys.argv

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
history = []
for turn in ["My case id is C-104. Say OK.", "What's my case id?", "Summarise our chat in 5 words."]:
    history.append({"role": "user", "content": turn})
    msg = client.messages.create(
        model=MODEL,
        max_tokens=256,
        system="You are a terse AML operations assistant.",
        messages=history[-1:] if STRIPPED else history,
    )
    text = "".join(b.text for b in msg.content if b.type == "text")
    print(f"> {turn}\n  {text!r}\n  stop={msg.stop_reason} in={msg.usage.input_tokens} "
          f"out={msg.usage.output_tokens} request_id={msg._request_id}\n")
    history.append({"role": "assistant", "content": msg.content})
