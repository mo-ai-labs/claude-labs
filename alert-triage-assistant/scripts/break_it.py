"""W1D1 Mission 5: break the API on purpose and record each error body.

    uv run scripts/break_it.py
"""
import anthropic

client = anthropic.Anthropic(max_retries=0)  # see each failure raw, with no silent SDK retries
MODEL = "claude-sonnet-5-5"
USER = [{"role": "user", "content": "Classify alert ALRT-0001: structuring or not?"}]

experiments = {
    "404 - model that doesn't exist": dict(model="claude-sonnet-9", max_tokens=50, messages=USER),
    "400 - no max_tokens": dict(model=MODEL, messages=USER),
    "400 - prefilled assistant turn": dict(model=MODEL, max_tokens=50,
                                           messages=USER + [{"role": "assistant", "content": '{"verdict": "'}]),
}

for name, kwargs in experiments.items():
    print(f"== {name}")
    try:
        msg = client.messages.create(**kwargs)
        print(f"  unexpectedly succeeded: stop={msg.stop_reason} request_id={msg._request_id}")
    except TypeError as e:  # the SDK may reject a missing required arg before any HTTP call
        print(f"  client-side TypeError (never reached the API, so no request id): {e}")
    except anthropic.APIStatusError as e:
        err = (e.body or {}).get("error", {}) if isinstance(e.body, dict) else {}
        print(f"  status={e.status_code} type={err.get('type')} request_id={e.request_id}")
        print(f"  message={err.get('message')}")
    print()
