"""data/samples/reservations_*.csv を読み、物件別の月次サマリを標準出力に表示する。

使い方:
    python3 scripts/summarize_reservations.py data/samples/reservations_2026-04.csv
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path


def main(path: str) -> None:
    rows = list(csv.DictReader(Path(path).open(encoding="utf-8")))
    by_property: dict[str, dict[str, int]] = defaultdict(
        lambda: {"reservations": 0, "nights": 0, "gross": 0, "ota_fee": 0, "net": 0}
    )
    for r in rows:
        key = f"{r['property_id']} / {r['property_name']}"
        by_property[key]["reservations"] += 1
        by_property[key]["nights"] += int(r["nights"])
        by_property[key]["gross"] += int(r["gross_amount"])
        by_property[key]["ota_fee"] += int(r["ota_fee"])
        by_property[key]["net"] += int(r["net_amount"])

    print(f"# 月次サマリ ({path})")
    print()
    print("| 物件 | 予約数 | 泊数 | 売上合計 | OTA手数料 | 手数料控除後 |")
    print("| --- | ---: | ---: | ---: | ---: | ---: |")
    for key in sorted(by_property):
        s = by_property[key]
        print(
            f"| {key} | {s['reservations']} | {s['nights']} | "
            f"{s['gross']:,} | {s['ota_fee']:,} | {s['net']:,} |"
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: summarize_reservations.py <reservations.csv>")
    main(sys.argv[1])
