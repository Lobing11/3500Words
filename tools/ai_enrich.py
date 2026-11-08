#!/usr/bin/env python3
"""
Offline enrich stub: turns raw jsonl into review unit JSON with placeholder answers.

When OPENAI_API_KEY (or compatible) is set, can call an LLM. Otherwise fills
answerPrimary with TODO markers for human/AI offline editing.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    items: list[dict] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items


def infer_cloze_answer(prompt: str) -> str:
    # very weak heuristic for common prep blanks left empty
    if re.search(r"pressure\s+_+\s*sb", prompt, re.I):
        return "on"
    if re.search(r"priced\s+_+\s*\d", prompt, re.I):
        return "at"
    if re.search(r"purchase.+\s+_+\s*", prompt, re.I) and "price" in prompt.lower():
        return "at"
    return ""


def enrich_item(raw: dict) -> dict:
    prompt = raw.get("prompt", "").strip()
    type_name = raw.get("typeGuess") or "zh2en"
    answer = infer_cloze_answer(prompt)
    item = {
        "id": raw.get("rawId") or f"u{raw.get('unitId')}-{raw.get('seq')}",
        "unitId": str(raw.get("unitId")),
        "type": type_name,
        "prompt": prompt,
        "answerPrimary": answer if answer else "TODO",
        "answerAlts": [],
        "blanks": [],
        "hint": "",
        "tags": [type_name],
        "relatedGroupId": "",
        "sourceRef": raw.get("sourceRef", ""),
        "needsReview": answer == "" or answer == "TODO",
    }
    if type_name in ("cloze", "word_form") and answer:
        item["blanks"] = [{"index": 0, "answer": answer, "alts": []}]
    return item


def try_llm_enrich(items: list[dict]) -> list[dict]:
    api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("LLM_API_KEY")
    if not api_key:
        return items
    # Placeholder hook — keep deterministic offline behavior unless wired by user.
    print("LLM key detected but offline stub mode kept for reproducibility.")
    return items


def main() -> None:
    parser = argparse.ArgumentParser()
    root = Path(__file__).resolve().parents[1]
    parser.add_argument("--raw-dir", type=Path, default=root / "content" / "raw")
    parser.add_argument("--out-dir", type=Path, default=root / "content" / "review")
    parser.add_argument("--unit", type=str, default="")
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    files = sorted(args.raw_dir.glob("unit_*.jsonl"))
    if args.unit:
        files = [p for p in files if p.stem == f"unit_{args.unit}"]

    for path in files:
        raw_items = load_jsonl(path)
        enriched = [enrich_item(x) for x in raw_items]
        enriched = try_llm_enrich(enriched)
        unit_id = path.stem.replace("unit_", "")
        out_obj = {
            "unitId": unit_id,
            "name": f"Unit {unit_id}",
            "order": int(unit_id) if unit_id.isdigit() else 0,
            "items": enriched,
        }
        out = args.out_dir / f"unit_{unit_id}.json"
        out.write_text(json.dumps(out_obj, ensure_ascii=False, indent=2), encoding="utf-8")
        todo = sum(1 for i in enriched if i.get("needsReview"))
        print(f"{out.name}: {len(enriched)} items, needsReview={todo}")


if __name__ == "__main__":
    main()
