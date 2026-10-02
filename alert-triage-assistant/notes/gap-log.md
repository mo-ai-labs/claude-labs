# CCDV-F gap log

Log every miss: a wrong quiz answer, a lost bet, or a doc fact that surprised you. Re-read the linked doc before it's marked closed.

| Date | Objective | Why I missed it | Doc link |
|---|---|---|---|
| 2026-10-02 | 2.3 / 4.1 | Bet B: guessed the SDKs retry a 529 **1×** by default; the docs say **2×** (exponential backoff, honoring `retry-after`). Under-estimated the built-in retries, so raw retry loops on top would multiply calls. | [Errors → HTTP errors](https://platform.claude.com/docs/en/api/errors#http-errors) |
| 2026-10-02 | 7.4 | Real 401 `invalid x-api-key` on the first run: the key in my environment wasn't valid. It's a *fix* error, so retrying can't help. Check the key's source, the shell that's running, and that the key wasn't revoked. | [Errors → HTTP errors](https://platform.claude.com/docs/en/api/errors#http-errors) |
