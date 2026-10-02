# CCDV-F gap log

Log every miss: a wrong quiz answer, a lost bet, or a doc fact that surprised you. Re-read the linked doc before it's marked closed.

| Date | Objective | Why I missed it | Doc link |
|---|---|---|---|
| 2026-10-02 | 2.3 / 4.1 | Bet B: guessed the SDKs retry a 529 **1×** by default; the docs say **2×** (exponential backoff, honoring `retry-after`). Under-estimated the built-in retries, so raw retry loops on top would multiply calls. | [Errors → HTTP errors](https://platform.claude.com/docs/en/api/errors#http-errors) |
| 2026-10-02 | 7.4 / 4.1 | Real 401s on the first run. Root cause: a personal `sk-ant-usr` key **not scoped to a workspace**. Keys that span workspaces need the `anthropic-workspace-id` header. Fixed by re-creating the key scoped to `ccdv-lab`. Lesson: an error with no request-id never reached the API. | [Get your API key](https://platform.claude.com/docs/en/get-api-key) |
