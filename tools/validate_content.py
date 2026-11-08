#!/usr/bin/env python3
"""Validate curated/review unit JSON before shipping to apps."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ALLOWED_TYPES = {"zh2en", "cloze", "word_form", "phrase_cluster", "pattern"}


def validate_unit(path: Path, allow_todo: bool) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    if "unitId" not in data or "items" not in data:
        return [f"{path.name}: missing unitId/items"]
    ids: set[str] = set()
    for idx, item in enumerate(data["items"]):
        prefix = f"{path.name}[{idx}]"
        for key in ("id", "unitId", "type", "prompt", "answerPrimary"):
            if key not in item or item[key] in (None, ""):
                errors.append(f"{prefix}: missing {key}")
        if item.get("type") not in ALLOWED_TYPES:
            errors.append(f"{prefix}: invalid type {item.get('type')}")
        if item.get("id") in ids:
            errors.append(f"{prefix}: duplicate id {item.get('id')}")
        ids.add(item.get("id"))
        ans = item.get("answerPrimary", "")
        if not allow_todo and (ans == "TODO" or item.get("needsReview")):
            errors.append(f"{prefix}: unresolved TODO/needsReview")
        blanks = item.get("blanks") or []
        if item.get("type") in ("cloze", "word_form") and not blanks and "|" not in ans:
            # soft warning as error for curated
            if not allow_todo:
                errors.append(f"{prefix}: cloze/word_form should have blanks")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    root = Path(__file__).resolve().parents[1]
    parser.add_argument("--dir", type=Path, default=root / "content" / "curated")
    parser.add_argument("--allow-todo", action="store_true")
    args = parser.parse_args()

    files = sorted(args.dir.glob("unit_*.json"))
    if not files:
        print(f"No unit_*.json in {args.dir}")
        return 1

    all_errors: list[str] = []
    for path in files:
        all_errors.extend(validate_unit(path, args.allow_todo))

    if all_errors:
        print("VALIDATION FAILED")
        for e in all_errors:
            print(" -", e)
        return 1

    print(f"OK: {len(files)} unit file(s) in {args.dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
