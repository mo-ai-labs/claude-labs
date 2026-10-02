"""Diagnose a 401 without printing the key.

    uv run scripts/check_key.py
"""
import os

import anthropic
import httpx

print("== Environment (names only; values masked) ==")
for name in sorted(os.environ):
    if name.upper().startswith(("ANTHROPIC", "CLAUDE")) or name.upper() in {"HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "NO_PROXY"}:
        v = os.environ[name]
        shown = v if ("URL" in name.upper() or "PROXY" in name.upper()) else f"{v[:10]}… len={len(v)}"
        print(f"  {name} = {shown}")

key = os.environ.get("ANTHROPIC_API_KEY", "")
print("\n== Key shape ==")
has_quotes = any(q in key for q in "\"'")
print(f"  len={len(key)} prefix={key[:10]!r} whitespace={key != key.strip()} quotes={has_quotes}")

client = anthropic.Anthropic()
print("\n== Where the SDK will send requests ==")
print(f"  base_url = {client.base_url}")

print("\n== Raw call straight to api.anthropic.com (bypasses ANTHROPIC_BASE_URL) ==")
r = httpx.post(
    "https://api.anthropic.com/v1/messages",
    headers={"x-api-key": key.strip(), "anthropic-version": "2023-06-01", "content-type": "application/json"},
    json={"model": "claude-haiku-4-5-20251001", "max_tokens": 5, "messages": [{"role": "user", "content": "hi"}]},
    timeout=30,
)
print(f"  status={r.status_code} request-id={r.headers.get('request-id')} server={r.headers.get('server')}")
print(f"  body={r.text[:300]}")
