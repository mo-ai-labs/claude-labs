# Lab data (synthetic)

Every record here is **invented** for the CCDV-F labs: no real customers, accounts or transactions.
Regenerate (seeded, reproducible) with `uv run scripts/gen_data.py`.

| File | Records | Shape |
|---|---|---|
| `customers.json` | 30 | KYC profile: type, country, occupation/industry, risk rating, PEP flag, expected monthly volume |
| `transactions.json` | 226 | 5–12 per customer: date, type, direction, amount, counterparty, counterparty country |
| `alerts.json` | 50 | `id`, `customer_id`, `rule`, `amount`, `currency`, `origin_country`, `destination_country`, `narrative`, plus `transaction_ids` linking to the planted transactions |

Rules: `structuring`, `rapid_movement`, `high_risk_corridor`, `large_cash`, `dormant_reactivation`, `round_amounts`, `third_party_funding`.
The "high-risk corridor" country list in the generator exists only for this lab.
