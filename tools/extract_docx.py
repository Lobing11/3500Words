#!/usr/bin/env python3
"""Extract unit vocabulary drills from a .docx into content/raw/*.jsonl"""

from __future__ import annotations

import argparse
import html
import json
import re
import zipfile
from pathlib import Path


UNIT_HEADER = re.compile(
    r"(?i)^\s*(unit\s*(\d+)(?:\s*[-–]?\s*(\d+))?(?:\s+(\d+\s*[-–]\s*\d+))?)\s*$"
)
ITEM_SPLIT = re.compile(r"(?:(?<=\D)|^)(\d{1,3})\.\s+")


def docx_to_text(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml").decode("utf-8")
    text = re.sub(r"</w:p>", "\n", xml)
    text = re.sub(r"<w:tab[^/]*/>", "\t", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def looks_chinese_heavy(s: str) -> bool:
    cn = len(re.findall(r"[\u4e00-\u9fff]", s))
    en = len(re.findall(r"[A-Za-z]", s))
    return cn >= 2 and cn >= en


def guess_type(prompt: str) -> str:
    if re.search(r"_{2,}|\b_{1,}\b|\(\w+\)", prompt):
        if re.search(r"\([A-Za-z]+\)", prompt):
            return "word_form"
        return "cloze"
    if looks_chinese_heavy(prompt) and not re.search(r"[A-Za-z]{3,}", prompt):
        return "zh2en"
    if "句型" in prompt:
        return "pattern"
    if "/" in prompt and re.search(r"\b(put|take|get|make)\b", prompt, re.I):
        return "phrase_cluster"
    if looks_chinese_heavy(prompt):
        return "zh2en"
    return "cloze"


def parse_units(text: str) -> dict[str, list[dict]]:
    units: dict[str, list[dict]] = {}
    current_unit = "unknown"
    current_segment = "all"
    buf_lines: list[str] = []

    def flush_block(block: str) -> None:
        nonlocal current_unit, current_segment
        if not block.strip():
            return
        parts = ITEM_SPLIT.split(block)
        # parts: [preamble, num, body, num, body, ...]
        i = 1
        while i + 1 < len(parts):
            num = parts[i]
            body = parts[i + 1].strip()
            i += 2
            if not body:
                continue
            # split multi-prompt lines joined by " / " cautiously kept as one raw item
            item = {
                "rawId": f"u{current_unit}-{num}",
                "unitId": current_unit,
                "segment": current_segment,
                "seq": int(num),
                "prompt": body,
                "typeGuess": guess_type(body),
                "answerPrimary": "",
                "sourceRef": f"unit{current_unit}-{current_segment}#{num}",
            }
            units.setdefault(current_unit, []).append(item)

    for line in text.splitlines():
        raw = line.strip()
        if not raw:
            continue
        m = UNIT_HEADER.match(raw.replace("、", " "))
        # also match "unit 42 26-50" style
        m2 = re.match(
            r"(?i)^\s*unit\s*(\d+)(?:\s+(\d+\s*[-–]\s*\d+))?\s*$", raw
        )
        if m2:
            flush_block(" ".join(buf_lines))
            buf_lines = []
            current_unit = m2.group(1)
            current_segment = (m2.group(2) or "all").replace(" ", "").replace("–", "-")
            continue
        if re.match(r"(?i)^\s*unit\s*\d+", raw):
            flush_block(" ".join(buf_lines))
            buf_lines = []
            mm = re.search(r"(?i)unit\s*(\d+)", raw)
            seg = re.search(r"(\d+\s*[-–]\s*\d+)", raw)
            current_unit = mm.group(1) if mm else current_unit
            current_segment = seg.group(1).replace(" ", "").replace("–", "-") if seg else "all"
            continue
        buf_lines.append(raw)

    flush_block(" ".join(buf_lines))
    return units


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--docx",
        type=Path,
        default=Path(r"C:\Users\WHO\Downloads\Unit词汇练习提取.docx"),
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "content" / "raw",
    )
    args = parser.parse_args()

    text = docx_to_text(args.docx)
    units = parse_units(text)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    summary = []
    for unit_id, items in sorted(units.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 999):
        out = args.out_dir / f"unit_{unit_id}.jsonl"
        with out.open("w", encoding="utf-8") as f:
            for item in items:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
        summary.append({"unitId": unit_id, "count": len(items), "file": out.name})
        print(f"unit {unit_id}: {len(items)} items -> {out}")

    (args.out_dir / "_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
