#!/usr/bin/env python3
"""Helpers for promoting reviewed unit banks into content/curated."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def item(
    unit_id: str,
    id_: str,
    type_: str,
    prompt: str,
    answer: str,
    *,
    alts: list[str] | None = None,
    blanks: list[dict] | None = None,
    hint: str = "",
    tags: list[str] | None = None,
    related: str = "",
    source: str = "",
    segment: str = "",
) -> dict[str, Any]:
    out: dict[str, Any] = {
        "id": id_,
        "unitId": str(unit_id),
        "type": type_,
        "prompt": prompt,
        "answerPrimary": answer,
        "answerAlts": alts or [],
        "tags": tags or [type_],
        "sourceRef": source,
        "segment": segment,
    }
    if blanks is not None:
        out["blanks"] = blanks
    elif type_ in ("cloze", "word_form") and "|" not in answer:
        out["blanks"] = [{"index": 0, "answer": answer, "alts": list(alts or [])}]
    else:
        out["blanks"] = blanks or []
    if hint:
        out["hint"] = hint
    if related:
        out["relatedGroupId"] = related
    return out


def blank(answer: str, index: int = 0, alts: list[str] | None = None) -> dict[str, Any]:
    return {"index": index, "answer": answer, "alts": alts or []}


def write_unit(bank: dict[str, Any]) -> Path:
    unit_id = str(bank["unitId"])
    out = ROOT / "content" / "curated" / f"unit_{unit_id}.json"
    out.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    review = ROOT / "content" / "review" / f"unit_{unit_id}.curated_candidate.json"
    review.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    man_path = ROOT / "content" / "curated" / "manifest.json"
    man = json.loads(man_path.read_text(encoding="utf-8"))
    found = False
    for u in man["units"]:
        if str(u["unitId"]) == unit_id:
            u.update(
                {
                    "hasContent": True,
                    "file": f"unit_{unit_id}.json",
                    "name": bank["name"],
                    "rangeFrom": bank.get("rangeFrom", u.get("rangeFrom", "")),
                    "rangeTo": bank.get("rangeTo", u.get("rangeTo", "")),
                    "wordsPerUnit": bank.get("wordsPerUnit", 50),
                    "order": bank.get("order", int(unit_id)),
                }
            )
            found = True
            break
    if not found:
        man["units"].append(
            {
                "unitId": unit_id,
                "name": bank["name"],
                "order": bank.get("order", int(unit_id)),
                "file": f"unit_{unit_id}.json",
                "rangeFrom": bank.get("rangeFrom", ""),
                "rangeTo": bank.get("rangeTo", ""),
                "wordsPerUnit": bank.get("wordsPerUnit", 50),
                "hasContent": True,
            }
        )
    man["units"].sort(key=lambda x: int(x["order"]))
    man_path.write_text(json.dumps(man, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # catalog flag
    cat_path = ROOT / "content" / "catalog" / "units.json"
    if cat_path.exists():
        cat = json.loads(cat_path.read_text(encoding="utf-8"))
        for u in cat.get("units", []):
            if str(u.get("unitId")) == unit_id:
                u["hasContent"] = True
        cat_path.write_text(json.dumps(cat, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    seg: dict[str, int] = {}
    for it in bank["items"]:
        seg[it.get("segment", "")] = seg.get(it.get("segment", ""), 0) + 1
    print(f"wrote {out.name} items={len(bank['items'])} segments={seg}")
    return out
