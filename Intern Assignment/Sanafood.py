import csv
from collections import defaultdict
from pathlib import Path

UNKNOWN_SHOPS = {"100999"}  # assumption: LMS knows every shop except this one


def to_float(value):
    if value is None:
        return None

    text = str(value).strip()
    if not text:
        return None

    # Handle common SAP/European numeric formatting: 1.234,56 -> 1234.56
    if "," in text and "." in text:
        if text.rfind(",") > text.rfind("."):
            text = text.replace(".", "").replace(",", ".")
        else:
            text = text.replace(",", "")
    elif "," in text:
        text = text.replace(",", ".")

    try:
        return float(text)
    except ValueError:
        return None


csv_path = None
for candidate in [
    Path(__file__).resolve().parent / "SAP_delivery_sample.csv",
    Path(__file__).resolve().parent / "sap_delivery_sample.csv",
    Path(__file__).resolve().parent / "delivery_sample.csv",
    Path(__file__).resolve().parent / "Sanafood.csv",
]:
    if candidate.exists():
        csv_path = candidate
        break

if csv_path is None:
    available = sorted(p.name for p in Path(__file__).resolve().parent.glob("*.csv"))
    print("CSV file not found in the script directory.")
    if available:
        print(f"Found CSV files: {', '.join(available)}")
    else:
        print("Please place the delivery CSV next to this script and use one of the common names:")
        print("SAP_delivery_sample.csv, sap_delivery_sample.csv, delivery_sample.csv, or Sanafood.csv")
    raise SystemExit(1)


deliveries = defaultdict(list)
with open(csv_path, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if not row:
            continue
        vbeln = (row.get("VBELN") or "").strip()
        if not vbeln:
            continue
        deliveries[vbeln].append(row)

for vbeln, rows in deliveries.items():
    first_row = rows[0]
    shop_code = (first_row.get("KUNNR") or "").strip().lstrip("0") or "UNKNOWN"
    name = first_row.get("NAME1") or first_row.get("NAME") or "Unknown shop"
    problems, total = [], 0.0

    for r in rows:
        weight = to_float(r.get("BRGEW", ""))
        posnr = r.get("POSNR") or "?"
        if weight is None:
            problems.append(f"line {posnr}: missing weight")
        else:
            total += weight

    if shop_code in UNKNOWN_SHOPS:
        problems.append("unknown shop")

    flag = " | ISSUES: " + "; ".join(problems) if problems else ""
    print(f"{vbeln} | {name} | {len(rows)} items | {total:.1f} kg{flag}")
