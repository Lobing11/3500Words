#!/usr/bin/env python3
"""Cross-platform grade fixture runner mirroring QUIZ_SPEC."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def normalize(raw: str) -> str:
    s = raw.strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[.?!;:,]+$", "", s)
    return s


def matches_any(inp: str, candidates: list[str]) -> bool:
    n = normalize(inp)
    return any(normalize(c) == n for c in candidates)


def grade(item: dict, user_input: str) -> str:
    blanks = item.get("blanks") or []
    if blanks:
        parts = [p.strip() for p in re.split(r"[|\n]", user_input) if p.strip()]
        correct = 0
        for i, blank in enumerate(blanks):
            if i >= len(parts):
                continue
            cands = [blank["answer"]] + list(blank.get("alts") or [])
            if matches_any(parts[i], cands):
                correct += 1
        if correct == len(blanks):
            return "correct"
        if correct == 0:
            return "wrong"
        return "partial"
    cands = [item["answerPrimary"]] + list(item.get("answerAlts") or [])
    return "correct" if matches_any(user_input, cands) else "wrong"


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    bank = json.loads((root / "content/curated/unit_42.json").read_text(encoding="utf-8"))
    by_id = {i["id"]: i for i in bank["items"]}
    fixtures = json.loads((root / "content/fixtures/grade_cases.json").read_text(encoding="utf-8"))
    failed = 0
    for case in fixtures["cases"]:
        item = by_id[case["itemId"]]
        got = grade(item, case["input"])
        ok = got == case["expected"]
        print(f"{'OK' if ok else 'FAIL'} {case['id']}: got={got} expected={case['expected']}")
        if not ok:
            failed += 1
    if failed:
        print(f"FAILED: {failed}")
        return 1
    print("All grade fixtures passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
