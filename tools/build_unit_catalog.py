#!/usr/bin/env python3
"""Build content/catalog/units.json + curated/manifest.json from 3500 directory txt."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


def parse_units(text: str) -> list[dict]:
    pat = re.compile(r"Unit\s+(\d+):\*\*\s*\((.+?)[—\-](.+?)\)", re.I)
    units: list[dict] = []
    seen: set[str] = set()
    for m in pat.finditer(text):
        uid = m.group(1)
        if uid in seen:
            continue
        seen.add(uid)
        a = m.group(2).strip()
        b = m.group(3).strip()
        units.append(
            {
                "unitId": uid,
                "order": int(uid),
                "name": f"Unit {uid}",
                "rangeFrom": a,
                "rangeTo": b,
                "displayName": f"Unit {uid} ({a}—{b})",
                "wordsPerUnit": 50,
                "segments": [
                    {"id": "1-25", "label": "前25词", "wordFrom": 1, "wordTo": 25},
                    {"id": "26-50", "label": "后25词", "wordFrom": 26, "wordTo": 50},
                ],
                "file": f"unit_{uid}.json",
            }
        )
    units.sort(key=lambda x: x["order"])
    return units


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--src",
        type=Path,
        default=Path(r"C:\Users\WHO\Desktop\3500.txt"),
    )
    args = parser.parse_args()

    catalog_dir = root / "content" / "catalog"
    curated_dir = root / "content" / "curated"
    catalog_dir.mkdir(parents=True, exist_ok=True)

    text = args.src.read_text(encoding="utf-8")
    shutil.copy2(args.src, catalog_dir / "3500_units_directory.txt")
    units = parse_units(text)
    if len(units) != 60:
        raise SystemExit(f"expected 60 units, got {len(units)}")

    for u in units:
        u["hasContent"] = (curated_dir / u["file"]).exists()

    catalog = {
        "version": 1,
        "source": "3500_units_directory.txt",
        "rule": "Strictly 50 headwords per Unit; quiz may split into segments 1-25 and 26-50.",
        "unitCount": 60,
        "wordsPerUnit": 50,
        "units": units,
    }
    (catalog_dir / "units.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    manifest = {
        "version": 2,
        "rule": "Each Unit = 50 words; quiz segments = 1-25 / 26-50 / all",
        "units": [
            {
                "unitId": u["unitId"],
                "name": u["displayName"],
                "order": u["order"],
                "rangeFrom": u["rangeFrom"],
                "rangeTo": u["rangeTo"],
                "wordsPerUnit": 50,
                "file": u["file"],
                "hasContent": u["hasContent"],
            }
            for u in units
        ],
    }
    (curated_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"OK: {len(units)} units, hasContent={sum(1 for u in units if u['hasContent'])}")


if __name__ == "__main__":
    main()
