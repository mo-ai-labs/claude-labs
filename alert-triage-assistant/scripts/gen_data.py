"""Generate synthetic AML lab data (all invented, seeded for reproducibility).

    uv run scripts/gen_data.py

Writes data/customers.json, data/transactions.json, data/alerts.json.
"""
import json
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(104)
DATA = Path(__file__).resolve().parent.parent / "data"

FIRST = ["Arlo", "Bexley", "Corin", "Dalia", "Emeric", "Fenna", "Galen", "Hesper", "Idris", "Juno",
         "Kestrel", "Liora", "Maelis", "Noor", "Orrin", "Perrin", "Quilla", "Rafe", "Seren", "Talin"]
LAST = ["Ashgrove", "Brightwater", "Calloway", "Dunmere", "Everhart", "Fallowmere", "Greystone",
        "Hollins", "Ivescombe", "Juniper", "Kettering", "Larkspur", "Marrow", "Northam", "Oakhurst"]
BIZ = ["Lantern Freight Ltd", "Copperleaf Trading", "Bluefin Imports", "Meridian Auto Parts",
       "Saltmarsh Holdings", "Quartz Electronics Wholesale", "Harbourline Logistics", "Verdant Textiles",
       "Northwind Money Services", "Pillar Gems & Bullion"]
OCC = ["teacher", "nurse", "software developer", "restaurant owner", "retired", "student",
       "car dealer", "real-estate agent", "consultant", "truck driver"]
HOME = ["CA", "US"]
LOW = ["US", "CA", "GB", "DE", "FR", "NL", "AU"]
HIGH = ["PA", "AE", "KY", "VG", "CY", "MT"]  # synthetic "high-risk corridor" list for the lab only
CCY = {"CA": "CAD", "US": "USD", "GB": "GBP", "DE": "EUR", "FR": "EUR", "NL": "EUR", "AU": "AUD",
       "PA": "USD", "AE": "AED", "KY": "USD", "VG": "USD", "CY": "EUR", "MT": "EUR"}
START = date(2026, 6, 1)


def d(offset):
    return (START + timedelta(days=offset)).isoformat()


# ---------- customers ----------
customers = []
for i in range(1, 31):
    is_biz = i % 3 == 0
    country = random.choice(HOME)
    cust = {
        "customer_id": f"CUST-{i:04d}",
        "type": "business" if is_biz else "individual",
        "name": BIZ[(i // 3 - 1) % len(BIZ)] if is_biz else f"{random.choice(FIRST)} {random.choice(LAST)}",
        "country": country,
        "occupation_or_industry": random.choice(["import/export", "logistics", "retail", "money services", "precious metals"]) if is_biz else random.choice(OCC),
        "onboarded": d(-random.randint(200, 3000)),
        "kyc_last_review": d(-random.randint(10, 700)),
        "risk_rating": random.choices(["low", "medium", "high"], [5, 3, 2])[0],
        "pep": random.random() < 0.07,
        "expected_monthly_volume": random.choice([3000, 5000, 8000, 15000]) if not is_biz else random.choice([50000, 120000, 400000]),
        "currency": CCY[country],
        "synthetic": True,
    }
    customers.append(cust)

# ---------- transactions ----------
transactions, tid = [], 1
by_cust = {}


def add_tx(c, day, kind, amount, cp_country, direction, cp_name=None):
    global tid
    tx = {
        "transaction_id": f"TX-{tid:06d}",
        "customer_id": c["customer_id"],
        "date": d(day),
        "type": kind,
        "direction": direction,
        "amount": round(amount, 2),
        "currency": c["currency"],
        "counterparty": cp_name or f"{random.choice(FIRST)} {random.choice(LAST)}",
        "counterparty_country": cp_country,
        "synthetic": True,
    }
    tid += 1
    transactions.append(tx)
    by_cust.setdefault(c["customer_id"], []).append(tx)
    return tx


for c in customers:
    for _ in range(random.randint(2, 4)):  # normal background activity
        add_tx(c, random.randint(0, 90), random.choice(["ach", "card", "wire", "cheque"]),
               random.uniform(40, c["expected_monthly_volume"] / 4), c["country"], random.choice(["in", "out"]))

# ---------- alerts (each rule plants matching transactions) ----------
RULES = ["structuring", "rapid_movement", "high_risk_corridor", "large_cash", "dormant_reactivation",
         "round_amounts", "third_party_funding"]
alerts = []
for n in range(1, 51):
    # keep every customer at 5-15 transactions (an alert plants at most 5)
    c = random.choice([x for x in customers if len(by_cust.get(x["customer_id"], [])) <= 10])
    rule = RULES[(n - 1) % len(RULES)]
    day = random.randint(10, 85)
    origin, dest = c["country"], c["country"]
    if rule == "structuring":
        txs = [add_tx(c, day + k, "cash_deposit", random.uniform(8200, 9900), c["country"], "in", "branch cash") for k in range(random.randint(3, 5))]
        narrative = f"{len(txs)} cash deposits just under the 10,000 reporting threshold within {len(txs)} days at different branches."
    elif rule == "rapid_movement":
        amt = random.uniform(20000, 90000)
        dest = random.choice(LOW + HIGH)
        txs = [add_tx(c, day, "wire", amt, random.choice(LOW), "in"),
               add_tx(c, day + 1, "wire", amt * random.uniform(0.92, 0.99), dest, "out")]
        narrative = f"Incoming wire of {amt:,.0f} moved out within 24h to {dest}; account balance returned to near zero."
    elif rule == "high_risk_corridor":
        dest = random.choice(HIGH)
        txs = [add_tx(c, day + k, "wire", random.uniform(5000, 45000), dest, "out", random.choice(BIZ)) for k in range(random.randint(1, 3))]
        narrative = f"Outbound wires to {dest}, a corridor on the lab's high-risk list, with no stated business link."
    elif rule == "large_cash":
        txs = [add_tx(c, day, "cash_deposit", random.uniform(15000, 60000), c["country"], "in", "branch cash")]
        narrative = f"Single cash deposit well above expected monthly volume ({c['expected_monthly_volume']:,})."
    elif rule == "dormant_reactivation":
        txs = [add_tx(c, day + k, random.choice(["wire", "ach"]), random.uniform(9000, 70000), random.choice(LOW + HIGH), random.choice(["in", "out"])) for k in range(2)]
        dest = txs[-1]["counterparty_country"]
        narrative = "Account inactive for 14+ months suddenly shows high-value activity."
    elif rule == "round_amounts":
        txs = [add_tx(c, day + k * 2, "wire", random.choice([10000, 20000, 25000, 50000]), random.choice(LOW), "out") for k in range(3)]
        dest = txs[-1]["counterparty_country"]
        narrative = "Repeated round-figure outbound wires with vague payment references ('services', 'invoice')."
    else:  # third_party_funding
        origin = random.choice(LOW + HIGH)
        txs = [add_tx(c, day + k, "wire", random.uniform(3000, 25000), origin, "in") for k in range(random.randint(3, 4))]
        narrative = f"{len(txs)} unrelated third parties funded the account from {origin}; funds then used for a single large purchase."
    total = sum(t["amount"] for t in txs)
    alerts.append({
        "id": f"ALRT-{n:04d}",
        "customer_id": c["customer_id"],
        "rule": rule,
        "amount": round(total, 2),
        "currency": c["currency"],
        "origin_country": origin,
        "destination_country": dest,
        "narrative": narrative,
        "created_at": d(day + 2),
        "transaction_ids": [t["transaction_id"] for t in txs],
        "synthetic": True,
    })

for c in customers:  # top up quiet customers to the 5-transaction minimum
    while len(by_cust.get(c["customer_id"], [])) < 5:
        add_tx(c, random.randint(0, 90), random.choice(["ach", "card"]),
               random.uniform(40, c["expected_monthly_volume"] / 4), c["country"], random.choice(["in", "out"]))

transactions.sort(key=lambda t: (t["customer_id"], t["date"]))
for name, obj in [("customers", customers), ("transactions", transactions), ("alerts", alerts)]:
    (DATA / f"{name}.json").write_text(json.dumps(obj, indent=2), encoding="utf-8")
counts = [len(v) for v in by_cust.values()]
print(f"customers={len(customers)} transactions={len(transactions)} alerts={len(alerts)} "
      f"tx/customer min={min(counts)} max={max(counts)}")
