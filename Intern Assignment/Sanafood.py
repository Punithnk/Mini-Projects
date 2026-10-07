import csv
from collections import defaultdict

CSV_FILE = "SAP_delivery_sample.csv"
# Assumption from the brief: the LMS knows every shop except 100999
UNKNOWN_SHOPS = {"100999"}


def to_float(value):
    """Return a number, or None if the value is empty or not a number."""
    try:
        return float(str(value).strip().replace(",", "."))
    except (TypeError, ValueError):
        return None


def normalize_header(header_name):
    """Normalize malformed header names from the sample export."""
    if header_name is None:
        return ""

    text = str(header_name).strip().upper()
    if "BELN" in text and text.startswith("V"):
        return "VBELN"
    return text


# csv.DictReader reads every value as text, so leading zeros are kept
# (0080001234 stays 0080001234, 000010 stays 000010).
deliveries = defaultdict(list)
with open(CSV_FILE, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    if reader.fieldnames:
        reader.fieldnames = [normalize_header(name) for name in reader.fieldnames]

    for row in reader:
        if not any((value or "").strip() for value in row.values()):
            continue
        deliveries[row["VBELN"]].append(row)

for vbeln, rows in deliveries.items():
    shop_code = rows[0]["KUNNR"].lstrip("0")   # LMS shop_code has no leading zeros
    problems, total_kg = [], 0.0

    for r in rows:
        weight = to_float(r.get("BRGEW", ""))
        if not weight:                          # missing, empty or 0
            problems.append(f"line {r['POSNR']}: missing weight")
        else:
            total_kg += weight

    if shop_code in UNKNOWN_SHOPS:
        problems.append("unknown shop")

    n = len(rows)
    word = "item" if n == 1 else "items"
    flag = " | ISSUES: " + "; ".join(problems) if problems else ""
    print(f"{vbeln} | {rows[0]['NAME1']} | {n} {word} | {total_kg:.1f} kg{flag}")