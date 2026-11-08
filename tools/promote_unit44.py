#!/usr/bin/env python3
"""Build curated Unit 44 gold JSON from classroom drills + reviewed answers."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def item(
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
) -> dict:
    out: dict = {
        "id": id_,
        "unitId": "44",
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


def blank(answer: str, index: int = 0, alts: list[str] | None = None) -> dict:
    return {"index": index, "answer": answer, "alts": alts or []}


def build() -> dict:
    items: list[dict] = []
    s1 = "1-25"
    s2 = "26-50"

    items.extend(
        [
            item(
                "u44-101",
                "zh2en",
                "通过无线电；在广播中",
                "over the radio",
                alts=["on the radio"],
                tags=["zh2en"],
                source="unit44-1-25#1",
                segment=s1,
            ),
            item(
                "u44-102",
                "zh2en",
                "充分发挥你的潜能",
                "realize your full potential",
                alts=[
                    "fulfil your potential",
                    "fulfill your potential",
                    "reach your full potential",
                    "develop your potential to the full",
                ],
                tags=["zh2en"],
                source="unit44-1-25#2",
                segment=s1,
            ),
            item(
                "u44-103",
                "zh2en",
                "现金；现钱（ready money）",
                "ready money",
                alts=["cash"],
                tags=["zh2en"],
                source="unit44-1-25#3",
                segment=s1,
            ),
            item(
                "u44-104a",
                "zh2en",
                "很容易获得；现成可用",
                "readily available",
                alts=["be readily available"],
                tags=["zh2en"],
                source="unit44-1-25#4a",
                segment=s1,
            ),
            item(
                "u44-104b",
                "zh2en",
                "欣然接受；爽快答应",
                "readily accept",
                alts=["readily accepted", "accept readily"],
                tags=["zh2en"],
                source="unit44-1-25#4b",
                segment=s1,
            ),
            item(
                "u44-105",
                "zh2en",
                "制定一个切实可行的计划",
                "make a realistic plan",
                alts=[
                    "work out a realistic plan",
                    "draw up a practical plan",
                    "make a workable plan",
                ],
                tags=["zh2en"],
                source="unit44-1-25#5",
                segment=s1,
            ),
            item(
                "u44-106",
                "zh2en",
                "靠着栏杆",
                "lean against the rail",
                alts=["lean on the rail"],
                tags=["zh2en"],
                source="unit44-1-25#6",
                segment=s1,
            ),
            item(
                "u44-107",
                "zh2en",
                "麻烦接踵而至；祸不单行",
                "Troubles rained down",
                alts=["troubles rain down", "rain down"],
                tags=["zh2en"],
                source="unit44-1-25#7",
                segment=s1,
            ),
            item(
                "u44-108a",
                "phrase_cluster",
                "筹款",
                "raise money",
                related="u44-raise",
                tags=["phrase"],
                source="unit44-1-25#8a",
                segment=s1,
            ),
            item(
                "u44-108b",
                "phrase_cluster",
                "振作精神；提高士气",
                "raise one's spirits",
                alts=["raise sb's spirits"],
                related="u44-raise",
                tags=["phrase"],
                source="unit44-1-25#8b",
                segment=s1,
            ),
            item(
                "u44-108c",
                "phrase_cluster",
                "养家",
                "raise a family",
                related="u44-raise",
                tags=["phrase"],
                source="unit44-1-25#8c",
                segment=s1,
            ),
            item(
                "u44-108d",
                "phrase_cluster",
                "取消禁烟令",
                "raise a ban on smoking",
                alts=["lift a ban on smoking"],
                related="u44-raise",
                tags=["phrase"],
                source="unit44-1-25#8d",
                segment=s1,
            ),
            item(
                "u44-109",
                "zh2en",
                "随机地（短语）",
                "at random",
                alts=["randomly"],
                tags=["zh2en"],
                source="unit44-1-25#9",
                segment=s1,
            ),
            item(
                "u44-110",
                "zh2en",
                "涉及从……到……的范围",
                "range from ... to ...",
                alts=["range from A to B", "range between ... and ..."],
                tags=["zh2en"],
                source="unit44-1-25#10",
                segment=s1,
            ),
            item(
                "u44-111",
                "zh2en",
                "在我的视野范围内",
                "within the range of my vision",
                alts=["within my range of vision", "in the range of my vision"],
                tags=["zh2en"],
                source="unit44-1-25#11",
                segment=s1,
            ),
            item(
                "u44-112",
                "zh2en",
                "属于……之列；在……范围内",
                "rank among",
                alts=["rank with", "be ranked among", "be among"],
                tags=["zh2en"],
                source="unit44-1-25#12",
                segment=s1,
            ),
            item(
                "u44-113",
                "cloze",
                "____ an alarming rate（以惊人的速度）",
                "at",
                tags=["collocation"],
                source="unit44-1-25#13",
                segment=s1,
            ),
            item(
                "u44-114",
                "zh2en",
                "无论如何；至少",
                "at any rate",
                alts=["in any case", "anyway"],
                tags=["zh2en"],
                source="unit44-1-25#14",
                segment=s1,
            ),
            item(
                "u44-115",
                "zh2en",
                "对某事评价很高",
                "rate sth highly",
                alts=["rate something highly", "think highly of"],
                tags=["zh2en"],
                source="unit44-1-25#15",
                segment=s1,
            ),
            item(
                "u44-116",
                "pattern",
                "更确切地说（or rather）",
                "or rather",
                tags=["pattern"],
                source="unit44-1-25#16",
                segment=s1,
            ),
            item(
                "u44-117a",
                "word_form",
                "You are ill, so I would rather you ____(stay) at home.",
                "stayed",
                blanks=[blank("stayed")],
                hint="stay / would rather 虚拟",
                tags=["word_form", "pattern"],
                source="unit44-1-25#17a",
                segment=s1,
            ),
            item(
                "u44-117b",
                "word_form",
                "I would rather you ____(not make) that mistake yesterday.",
                "had not made",
                alts=["hadn't made"],
                blanks=[blank("had not made", alts=["hadn't made"])],
                hint="not make / would rather 对过去虚拟",
                tags=["word_form", "pattern"],
                source="unit44-1-25#17b",
                segment=s1,
            ),
            item(
                "u44-118a",
                "zh2en",
                "原材料",
                "raw materials",
                alts=["raw material"],
                tags=["zh2en"],
                source="unit44-1-25#18a",
                segment=s1,
            ),
            item(
                "u44-118b",
                "zh2en",
                "生手；新手",
                "a raw beginner",
                alts=["raw beginner"],
                tags=["zh2en"],
                source="unit44-1-25#18b",
                segment=s1,
            ),
            item(
                "u44-119",
                "zh2en",
                "一线希望",
                "a ray of hope",
                alts=["a gleam of hope", "a flicker of hope"],
                tags=["zh2en"],
                source="unit44-1-25#19",
                segment=s1,
            ),
            item(
                "u44-120",
                "zh2en",
                "打电话找我；电话联系到我",
                "reach me on the phone",
                alts=["reach me by phone", "reach sb by telephone"],
                tags=["zh2en"],
                source="unit44-1-25#20",
                segment=s1,
            ),
            item(
                "u44-121",
                "zh2en",
                "向……伸出援手；联系",
                "reach out to",
                alts=["reach out"],
                tags=["zh2en"],
                source="unit44-1-25#21",
                segment=s1,
            ),
            item(
                "u44-122",
                "zh2en",
                "在……能力/范围之内",
                "within the reach of",
                alts=["within reach of", "within one's reach"],
                tags=["zh2en"],
                source="unit44-1-25#22",
                segment=s1,
            ),
            item(
                "u44-123",
                "zh2en",
                "反应不一",
                "meet with mixed reactions",
                alts=[
                    "get mixed reactions",
                    "receive mixed reactions",
                    "a mixed reaction",
                    "reactions vary",
                ],
                tags=["zh2en"],
                source="unit44-1-25#23",
                segment=s1,
            ),
            item(
                "u44-124",
                "zh2en",
                "看懂某人的想法；读懂心思",
                "read one's mind",
                alts=["read sb's mind", "read someone's thoughts"],
                tags=["zh2en"],
                source="unit44-1-25#24",
                segment=s1,
            ),
            item(
                "u44-125",
                "zh2en",
                "牌子上写着「禁止吸烟」",
                'The sign reads, "No smoking"',
                alts=["The sign reads No smoking", "The sign says No smoking"],
                tags=["zh2en"],
                source="unit44-1-25#25",
                segment=s1,
            ),
        ]
    )

    items.extend(
        [
            item(
                "u44-201",
                "zh2en",
                "沦为乞丐",
                "be reduced to a beggar",
                alts=["be reduced to begging", "reduce sb to a beggar"],
                tags=["zh2en"],
                source="unit44-26-50#1",
                segment=s2,
            ),
            item(
                "u44-202",
                "word_form",
                "reduce（名词）",
                "reduction",
                hint="reduce",
                tags=["word_form"],
                source="unit44-26-50#2",
                segment=s2,
            ),
            item(
                "u44-203",
                "zh2en",
                "正视现实",
                "face reality",
                alts=["face up to reality", "look reality in the face"],
                tags=["zh2en"],
                source="unit44-26-50#3",
                segment=s2,
            ),
            item(
                "u44-204",
                "zh2en",
                "推理能力",
                "reasoning ability",
                alts=["the ability to reason"],
                tags=["zh2en"],
                source="unit44-26-50#4",
                segment=s2,
            ),
            item(
                "u44-205",
                "cloze",
                "the reason ____ sth = the cause ____ sth",
                "for|of",
                blanks=[blank("for", 0), blank("of", 1)],
                tags=["collocation"],
                source="unit44-26-50#5",
                segment=s2,
            ),
            item(
                "u44-206a",
                "zh2en",
                "提出合理的建议",
                "offer reasonable advice",
                alts=["give reasonable advice"],
                tags=["zh2en"],
                source="unit44-26-50#6a",
                segment=s2,
            ),
            item(
                "u44-206b",
                "zh2en",
                "合理的价格",
                "reasonable price",
                alts=["a reasonable price"],
                tags=["zh2en"],
                source="unit44-26-50#6b",
                segment=s2,
            ),
            item(
                "u44-207a",
                "zh2en",
                "回忆童年",
                "recall my childhood",
                alts=["recall one's childhood"],
                tags=["zh2en"],
                source="unit44-26-50#7a",
                segment=s2,
            ),
            item(
                "u44-207b",
                "zh2en",
                "召回假冒产品",
                "recall the fake product",
                alts=["recall fake products", "product recall"],
                tags=["zh2en"],
                source="unit44-26-50#7b",
                segment=s2,
            ),
            item(
                "u44-208a",
                "zh2en",
                "销售收据；购物小票",
                "a sales receipt",
                alts=["sales receipt", "receipt"],
                tags=["zh2en"],
                source="unit44-26-50#8a",
                segment=s2,
            ),
            item(
                "u44-208b",
                "zh2en",
                "货到付款；收到货物后付款",
                "on receipt of the goods",
                alts=["Payment will be made on receipt of the goods"],
                tags=["zh2en"],
                source="unit44-26-50#8b",
                segment=s2,
            ),
            item(
                "u44-209",
                "zh2en",
                "很受欢迎",
                "be well received",
                alts=["receive a warm welcome", "be popular", "be warmly received"],
                tags=["zh2en"],
                source="unit44-26-50#9",
                segment=s2,
            ),
            item(
                "u44-210",
                "zh2en",
                "挂上听筒；放回听筒",
                "replace the receiver",
                alts=["put down the receiver", "hang up the receiver"],
                tags=["zh2en"],
                source="unit44-26-50#10",
                segment=s2,
            ),
            item(
                "u44-211",
                "zh2en",
                "酒店前台；接待处",
                "hotel reception",
                alts=["reception desk", "the reception"],
                tags=["zh2en"],
                source="unit44-26-50#11",
                segment=s2,
            ),
            item(
                "u44-212",
                "zh2en",
                "这项新政策反响不一",
                "The new policy met with a mixed reception",
                alts=["meet with a mixed reception", "receive a mixed reception"],
                tags=["zh2en"],
                source="unit44-26-50#12",
                segment=s2,
            ),
            item(
                "u44-213",
                "zh2en",
                "健康的秘诀",
                "the recipe for health",
                alts=["a recipe for good health", "the secret of health"],
                tags=["zh2en"],
                source="unit44-26-50#13",
                segment=s2,
            ),
            item(
                "u44-214",
                "word_form",
                "recite（名词）",
                "recitation",
                hint="recite",
                tags=["word_form"],
                source="unit44-26-50#14",
                segment=s2,
            ),
            item(
                "u44-215",
                "zh2en",
                "无法辨认",
                "beyond recognition",
                alts=["unrecognizable", "can't be recognized", "cannot be recognized"],
                tags=["zh2en"],
                source="unit44-26-50#15",
                segment=s2,
            ),
            item(
                "u44-216",
                "zh2en",
                "她一开始演奏我就听出了那支曲子",
                "I recognized the tune the moment she began to play",
                alts=["recognize the tune"],
                tags=["zh2en"],
                source="unit44-26-50#16",
                segment=s2,
            ),
            item(
                "u44-217",
                "zh2en",
                "他未能意识到前方的危险",
                "He failed to recognize the danger ahead",
                alts=["fail to recognize the danger", "not recognize the danger"],
                tags=["zh2en"],
                source="unit44-26-50#17",
                segment=s2,
            ),
            item(
                "u44-218",
                "zh2en",
                "为表彰她的勇气而授予奖牌",
                "in recognition of her courage",
                alts=["receive ... in recognition of"],
                tags=["zh2en"],
                source="unit44-26-50#18",
                segment=s2,
            ),
            item(
                "u44-219",
                "zh2en",
                "人们公认；普遍认为",
                "It is generally recognized that",
                alts=[
                    "It is widely recognized that",
                    "It is universally acknowledged that",
                    "People generally recognize that",
                ],
                tags=["zh2en", "pattern"],
                source="unit44-26-50#19",
                segment=s2,
            ),
            item(
                "u44-220",
                "zh2en",
                "这本书值得推荐。",
                "This book is worth recommending",
                alts=[
                    "The book is worth recommending",
                    "This book deserves to be recommended",
                    "I recommend this book",
                ],
                tags=["zh2en"],
                source="unit44-26-50#20",
                segment=s2,
            ),
            item(
                "u44-221",
                "word_form",
                "The doctor recommended that he ____(give) up staying up late.",
                "give",
                alts=["should give"],
                blanks=[blank("give", alts=["should give"])],
                hint="give / recommend that 虚拟语气",
                tags=["word_form", "pattern"],
                source="unit44-26-50#21",
                segment=s2,
            ),
            item(
                "u44-222a",
                "phrase_cluster",
                "记录；做记录",
                "keep a record of",
                related="u44-record",
                tags=["phrase"],
                source="unit44-26-50#22a",
                segment=s2,
            ),
            item(
                "u44-222b",
                "phrase_cluster",
                "创纪录",
                "set a record",
                alts=["break a record"],
                related="u44-record",
                tags=["phrase"],
                source="unit44-26-50#22b",
                segment=s2,
            ),
            item(
                "u44-222c",
                "phrase_cluster",
                "播放唱片",
                "play a record",
                related="u44-record",
                tags=["phrase"],
                source="unit44-26-50#22c",
                segment=s2,
            ),
            item(
                "u44-223",
                "zh2en",
                "找回丢失的古董",
                "recover the lost antique",
                alts=["recover a lost antique"],
                tags=["zh2en"],
                source="unit44-26-50#23",
                segment=s2,
            ),
            item(
                "u44-224",
                "zh2en",
                "阅读不仅是为了消遣，还能开阔视野",
                "Reading is not only for recreation, but broadens our horizons",
                alts=["for recreation", "recreation"],
                tags=["zh2en"],
                source="unit44-26-50#24",
                segment=s2,
            ),
            item(
                "u44-225",
                "zh2en",
                "娱乐设施",
                "recreational facilities",
                alts=["recreation facilities"],
                tags=["zh2en"],
                source="unit44-26-50#25",
                segment=s2,
            ),
        ]
    )

    return {
        "unitId": "44",
        "name": "Unit 44 (radio—reduce)",
        "order": 44,
        "rangeFrom": "radio",
        "rangeTo": "reduce",
        "wordsPerUnit": 50,
        "items": items,
    }


def update_manifest(curated_file: str = "unit_44.json") -> None:
    man_path = ROOT / "content" / "curated" / "manifest.json"
    man = json.loads(man_path.read_text(encoding="utf-8"))
    found = False
    for u in man["units"]:
        if u["unitId"] == "44":
            u["hasContent"] = True
            u["file"] = curated_file
            u["name"] = "Unit 44 (radio—reduce)"
            u["rangeFrom"] = "radio"
            u["rangeTo"] = "reduce"
            u["wordsPerUnit"] = 50
            found = True
            break
    if not found:
        man["units"].append(
            {
                "unitId": "44",
                "name": "Unit 44 (radio—reduce)",
                "order": 44,
                "file": curated_file,
                "rangeFrom": "radio",
                "rangeTo": "reduce",
                "wordsPerUnit": 50,
                "hasContent": True,
            }
        )
    man["units"].sort(key=lambda x: int(x["order"]))
    man_path.write_text(
        json.dumps(man, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def main() -> None:
    bank = build()
    out = ROOT / "content" / "curated" / "unit_44.json"
    out.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    update_manifest()
    review = ROOT / "content" / "review" / "unit_44.curated_candidate.json"
    review.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    seg = {"1-25": 0, "26-50": 0}
    for it in bank["items"]:
        seg[it["segment"]] = seg.get(it["segment"], 0) + 1
    print(f"wrote {out} items={len(bank['items'])} segments={seg}")


if __name__ == "__main__":
    main()
