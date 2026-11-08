#!/usr/bin/env python3
"""Shared quiz/grader logic aligned with docs/QUIZ_SPEC.md."""

from __future__ import annotations

import random
import re
from typing import Any


def normalize(raw: str) -> str:
    s = raw.strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = s.rstrip(".?!;:,")
    return s


def _matches_any(user_input: str, candidates: list[str]) -> bool:
    norm = normalize(user_input)
    return any(normalize(c) == norm for c in candidates if c)


def grade(item: dict[str, Any], user_input: str) -> str:
    blanks = item.get("blanks") or []
    if blanks:
        parts = [p.strip() for p in re.split(r"[|\n]", user_input) if p.strip()]
        if len(parts) < len(blanks):
            matched = sum(
                1
                for i, blank in enumerate(blanks)
                if i < len(parts)
                and _matches_any(
                    parts[i],
                    [blank.get("answer", "")] + list(blank.get("alts") or []),
                )
            )
            if matched == 0:
                return "wrong"
            if matched < len(blanks):
                return "partial"
            return "correct"

        correct_count = 0
        for i, blank in enumerate(blanks):
            cands = [blank.get("answer", "")] + list(blank.get("alts") or [])
            if _matches_any(parts[i], cands):
                correct_count += 1
        if correct_count == len(blanks):
            return "correct"
        if correct_count == 0:
            return "wrong"
        return "partial"

    cands = [item.get("answerPrimary", "")] + list(item.get("answerAlts") or [])
    return "correct" if _matches_any(user_input, cands) else "wrong"


def filter_by_segment(items: list[dict[str, Any]], segment: str) -> list[dict[str, Any]]:
    if segment == "all" or not segment:
        return list(items)
    tagged = [it for it in items if it.get("segment") == segment]
    if tagged:
        return tagged
    if not items:
        return []
    mid = (len(items) + 1) // 2
    if segment == "1-25":
        return items[:mid]
    if segment == "26-50":
        return items[mid:]
    return list(items)


def filter_by_mode(
    items: list[dict[str, Any]], mode: str, wrong_ids: set[str]
) -> list[dict[str, Any]]:
    if mode == "zh2en":
        return [it for it in items if it.get("type") == "zh2en"]
    if mode == "cloze":
        return [it for it in items if it.get("type") in ("cloze", "word_form")]
    if mode == "wrong_only":
        return [it for it in items if it.get("id") in wrong_ids]
    return list(items)


def build_session(
    items: list[dict[str, Any]],
    *,
    mode: str,
    segment: str,
    wrong_ids: set[str],
    count: int = 25,
    seed: int | None = None,
) -> list[dict[str, Any]]:
    pool = filter_by_segment(items, segment)
    pool = filter_by_mode(pool, mode, wrong_ids)
    if not pool:
        return []
    rng = random.Random(seed)
    unique = list({it["id"]: it for it in pool}.values())
    if mode == "mixed":
        weights = {
            "zh2en": 3,
            "cloze": 3,
            "word_form": 2,
            "phrase_cluster": 2,
            "pattern": 1,
        }

        def key_fn(it: dict[str, Any]) -> float:
            return rng.random() / weights.get(str(it.get("type")), 1)

        unique.sort(key=key_fn)
    else:
        rng.shuffle(unique)

    if len(unique) >= count:
        return unique[:count]
    result = list(unique)
    while len(result) < count and unique:
        result.append(rng.choice(unique))
    return result[:count]
