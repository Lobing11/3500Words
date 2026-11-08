#!/usr/bin/env python3
"""Build curated Unit 43 gold JSON from classroom drills + reviewed answers."""

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
        "unitId": "43",
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

    # ---- segment 1-25 (prohibit—... ~ promise/protect/provide area) ----
    s1 = "1-25"
    items.extend(
        [
            item(
                "u43-101",
                "cloze",
                "A timely snow ____ a good harvest.（瑞雪兆丰年）",
                "promises",
                alts=["promise"],
                blanks=[blank("promises", alts=["promise"])],
                tags=["collocation"],
                source="unit43-1-25#1",
                segment=s1,
            ),
            item(
                "u43-102a",
                "cloze",
                "a ____ writer（一个有前途的作家）",
                "promising",
                tags=["collocation"],
                source="unit43-1-25#2a",
                segment=s1,
            ),
            item(
                "u43-102b",
                "cloze",
                "a writer with ____（一个有前途的作家）",
                "promise",
                tags=["collocation"],
                source="unit43-1-25#2b",
                segment=s1,
            ),
            item(
                "u43-103a",
                "zh2en",
                "出版；发表",
                "publish",
                alts=["publication"],
                tags=["zh2en"],
                source="unit43-1-25#3a",
                segment=s1,
            ),
            item(
                "u43-103b",
                "zh2en",
                "惩罚；处罚",
                "punish",
                alts=["punishment"],
                tags=["zh2en"],
                source="unit43-1-25#3b",
                segment=s1,
            ),
            item(
                "u43-104",
                "cloze",
                "____ the protection of",
                "under",
                tags=["collocation"],
                source="unit43-1-25#4",
                segment=s1,
            ),
            item(
                "u43-105",
                "zh2en",
                "引体向上（锻炼）",
                "pull-ups",
                alts=["do pull-ups", "pull-up"],
                tags=["zh2en"],
                source="unit43-1-25#5",
                segment=s1,
            ),
            item(
                "u43-106a",
                "phrase_cluster",
                "拆除（旧建筑）",
                "pull down",
                related="u43-pull",
                tags=["phrase"],
                source="unit43-1-25#6a",
                segment=s1,
            ),
            item(
                "u43-106b",
                "phrase_cluster",
                "退出（项目）",
                "pull out of",
                alts=["pull out"],
                related="u43-pull",
                tags=["phrase"],
                source="unit43-1-25#6b",
                segment=s1,
            ),
            item(
                "u43-106c",
                "phrase_cluster",
                "齐心协力",
                "pull together",
                related="u43-pull",
                tags=["phrase"],
                source="unit43-1-25#6c",
                segment=s1,
            ),
            item(
                "u43-106d",
                "phrase_cluster",
                "停车；停下",
                "pull up",
                related="u43-pull",
                tags=["phrase"],
                source="unit43-1-25#6d",
                segment=s1,
            ),
            item(
                "u43-106e",
                "phrase_cluster",
                "帮助某人渡过难关",
                "pull sb through",
                alts=["pull through", "pull someone through"],
                related="u43-pull",
                tags=["phrase"],
                source="unit43-1-25#6e",
                segment=s1,
            ),
            item(
                "u43-107",
                "zh2en",
                "当众演讲",
                "make a speech in public",
                alts=["speak in public", "give a public speech", "speak publicly"],
                tags=["zh2en"],
                source="unit43-1-25#7",
                segment=s1,
            ),
            item(
                "u43-108",
                "word_form",
                "The plan was ____(public) announced last week.",
                "publicly",
                hint="public",
                tags=["word_form"],
                source="unit43-1-25#8",
                segment=s1,
            ),
            item(
                "u43-109",
                "word_form",
                "____(protect) suits",
                "protective",
                hint="protect",
                tags=["word_form"],
                source="unit43-1-25#9",
                segment=s1,
            ),
            item(
                "u43-110a",
                "zh2en",
                "推广产品",
                "promote the product",
                alts=["promote products"],
                tags=["zh2en"],
                source="unit43-1-25#10a",
                segment=s1,
            ),
            item(
                "u43-110b",
                "zh2en",
                "促进和平事业",
                "promote the peace cause",
                alts=["promote peace", "promote the cause of peace"],
                tags=["zh2en"],
                source="unit43-1-25#10b",
                segment=s1,
            ),
            item(
                "u43-110c",
                "zh2en",
                "晋升为经理",
                "be promoted to manager",
                alts=["promote sb to manager", "get promoted to manager"],
                tags=["zh2en"],
                source="unit43-1-25#10c",
                segment=s1,
            ),
            item(
                "u43-111",
                "word_form",
                "pronounce（名词）",
                "pronunciation",
                hint="pronounce",
                tags=["word_form"],
                source="unit43-1-25#11",
                segment=s1,
            ),
            item(
                "u43-112",
                "pattern",
                "有证据表明……（句型）",
                "There is evidence that",
                alts=[
                    "There is evidence that...",
                    "Evidence shows that",
                    "Evidence indicates that",
                ],
                tags=["pattern"],
                source="unit43-1-25#12",
                segment=s1,
            ),
            item(
                "u43-113",
                "zh2en",
                "防水服",
                "waterproof suit",
                alts=["waterproof clothing", "a waterproof"],
                tags=["zh2en"],
                source="unit43-1-25#13",
                segment=s1,
            ),
            item(
                "u43-114",
                "zh2en",
                "有力的证明；说明问题的证据（telling proof）",
                "a telling proof",
                alts=["telling proof"],
                tags=["zh2en"],
                source="unit43-1-25#14",
                segment=s1,
            ),
            item(
                "u43-115",
                "word_form",
                "After months of investigation, he ____(prove) innocent.",
                "was proved",
                alts=["proved", "was proven", "proved to be"],
                blanks=[
                    blank(
                        "was proved",
                        alts=["proved", "was proven", "proved to be"],
                    )
                ],
                hint="prove",
                tags=["word_form"],
                source="unit43-1-25#15",
                segment=s1,
            ),
            item(
                "u43-116",
                "zh2en",
                "提交一个提议",
                "put forward a proposal",
                alts=["make a proposal", "submit a proposal", "propose a proposal"],
                tags=["zh2en"],
                source="unit43-1-25#16",
                segment=s1,
            ),
            item(
                "u43-117",
                "word_form",
                "proper（反义词）",
                "improper",
                hint="proper",
                tags=["word_form"],
                source="unit43-1-25#17",
                segment=s1,
            ),
            item(
                "u43-118",
                "word_form",
                "I propose ____(hold) a class meeting this Friday.",
                "holding",
                alts=["to hold"],
                blanks=[blank("holding", alts=["to hold"])],
                hint="hold",
                tags=["word_form", "pattern"],
                source="unit43-1-25#18",
                segment=s1,
            ),
            item(
                "u43-119",
                "cloze",
                "be proud ____ = take pride ____",
                "of|in",
                blanks=[blank("of", 0), blank("in", 1)],
                tags=["collocation"],
                source="unit43-1-25#19",
                segment=s1,
            ),
            item(
                "u43-120",
                "cloze",
                "provide sb. ____ sth. = provide sth. ____ sb.",
                "with|for",
                blanks=[blank("with", 0), blank("for", 1)],
                tags=["collocation"],
                source="unit43-1-25#20",
                segment=s1,
            ),
            item(
                "u43-121a",
                "zh2en",
                "供养一大家子",
                "provide for a big family",
                alts=["provide for the family"],
                tags=["zh2en"],
                source="unit43-1-25#21a",
                segment=s1,
            ),
            item(
                "u43-121b",
                "zh2en",
                "计划为可能的风险做好准备（provide for）",
                "provide for possible risks",
                alts=["The plan provides for possible risks"],
                tags=["zh2en"],
                source="unit43-1-25#21b",
                segment=s1,
            ),
            item(
                "u43-122",
                "cloze",
                "providing (conj.) = ____",
                "provided that",
                alts=["provided", "as long as"],
                blanks=[blank("provided that", alts=["provided", "as long as"])],
                tags=["collocation", "pattern"],
                source="unit43-1-25#22",
                segment=s1,
            ),
        ]
    )

    # ---- segment 26-50 ----
    s2 = "26-50"
    items.extend(
        [
            item(
                "u43-201a",
                "cloze",
                "She purchased the necklace ____ 800 yuan.",
                "for",
                tags=["collocation"],
                source="unit43-26-50#1a",
                segment=s2,
            ),
            item(
                "u43-201b",
                "cloze",
                "He made a purchase ____ a valuable vase.",
                "of",
                tags=["collocation"],
                source="unit43-26-50#1b",
                segment=s2,
            ),
            item(
                "u43-202",
                "zh2en",
                "纯属偶然；碰巧",
                "by pure chance",
                alts=["by chance", "purely by chance"],
                tags=["zh2en"],
                source="unit43-26-50#2",
                segment=s2,
            ),
            item(
                "u43-203",
                "zh2en",
                "种族偏见",
                "racial prejudice",
                alts=["race prejudice", "prejudice against race"],
                tags=["zh2en"],
                source="unit43-26-50#3",
                segment=s2,
            ),
            item(
                "u43-204",
                "cloze",
                "be equal to everyone ____（不管他们的种族）",
                "regardless of their race",
                alts=["regardless of race", "irrespective of their race"],
                blanks=[
                    blank(
                        "regardless of their race",
                        alts=["regardless of race", "irrespective of their race"],
                    )
                ],
                tags=["collocation", "pattern"],
                source="unit43-26-50#4",
                segment=s2,
            ),
            item(
                "u43-205",
                "zh2en",
                "与某人赛跑；与……竞争",
                "race against sb",
                alts=["race against someone", "race against"],
                tags=["zh2en"],
                source="unit43-26-50#5",
                segment=s2,
            ),
            item(
                "u43-206",
                "word_form",
                "____(净化) yourself / 净化心灵",
                "purify",
                alts=["purify your mind", "purify oneself"],
                blanks=[blank("purify", alts=["purify your mind"])],
                hint="pure",
                tags=["word_form", "zh2en"],
                source="unit43-26-50#6",
                segment=s2,
            ),
            item(
                "u43-207",
                "zh2en",
                "故意地（写出常见说法）",
                "on purpose",
                alts=[
                    "purposely",
                    "deliberately",
                    "intentionally",
                    "by design",
                    "with intent",
                ],
                tags=["zh2en"],
                source="unit43-26-50#7",
                segment=s2,
            ),
            item(
                "u43-208",
                "zh2en",
                "能解决问题；管用；达到目的",
                "serve the purpose",
                alts=["serve one's purpose", "serve its purpose"],
                tags=["zh2en"],
                source="unit43-26-50#8",
                segment=s2,
            ),
            item(
                "u43-209",
                "zh2en",
                "引用剧本中的一句台词",
                "quote a line from the play",
                alts=["quote a line from a play"],
                tags=["zh2en"],
                source="unit43-26-50#9",
                segment=s2,
            ),
            item(
                "u43-210",
                "zh2en",
                "辍学",
                "drop out of school",
                alts=["quit school", "drop out"],
                tags=["zh2en"],
                source="unit43-26-50#10",
                segment=s2,
            ),
            item(
                "u43-211",
                "zh2en",
                "戒烟",
                "quit smoking",
                alts=["give up smoking", "stop smoking"],
                tags=["zh2en"],
                source="unit43-26-50#11",
                segment=s2,
            ),
            item(
                "u43-212",
                "word_form",
                "____(quick) the pace",
                "quicken",
                hint="quick",
                tags=["word_form"],
                source="unit43-26-50#13",
                segment=s2,
            ),
            item(
                "u43-213",
                "zh2en",
                "买不起；超出某人的经济能力",
                "beyond one's purse",
                alts=["beyond my purse", "beyond sb's purse"],
                tags=["zh2en"],
                source="unit43-26-50#14",
                segment=s2,
            ),
            item(
                "u43-214",
                "zh2en",
                "符合资格",
                "qualify",
                alts=["be qualified", "qualify for"],
                tags=["zh2en"],
                source="unit43-26-50#15",
                segment=s2,
            ),
            item(
                "u43-215",
                "zh2en",
                "被取消比赛资格",
                "be disqualified from the competition",
                alts=[
                    "be disqualified",
                    "disqualify sb from the competition",
                    "be disqualified for the game",
                ],
                tags=["zh2en"],
                source="unit43-26-50#16",
                segment=s2,
            ),
            item(
                "u43-216",
                "zh2en",
                "胜任该职位",
                "be qualified for the position",
                alts=[
                    "qualify for the position",
                    "be equal to the position",
                    "be competent for the post",
                ],
                tags=["zh2en"],
                source="unit43-26-50#17",
                segment=s2,
            ),
            item(
                "u43-217",
                "cloze",
                "The product is ____ high quality.（修正原文拼写 quliaty）",
                "of",
                tags=["collocation"],
                source="unit43-26-50#18",
                segment=s2,
            ),
            item(
                "u43-218",
                "cloze",
                "buy sth ____ large quantities",
                "in",
                tags=["collocation"],
                source="unit43-26-50#19",
                segment=s2,
            ),
            item(
                "u43-219",
                "word_form",
                "Unfortunately, large quantities of water ____(pollute).",
                "are polluted",
                alts=["have been polluted", "is polluted"],
                blanks=[
                    blank(
                        "are polluted",
                        alts=["have been polluted", "is polluted"],
                    )
                ],
                hint="pollute",
                tags=["word_form"],
                source="unit43-26-50#20",
                segment=s2,
            ),
            item(
                "u43-220a",
                "zh2en",
                "它值三个季度/四分之三（three quarters）",
                "It costs three quarters",
                alts=["three quarters"],
                tags=["zh2en"],
                source="unit43-26-50#21a",
                segment=s2,
            ),
            item(
                "u43-220b",
                "zh2en",
                "他按季度领工资",
                "He gets paid by the quarter",
                alts=["get paid by the quarter", "be paid by the quarter"],
                tags=["zh2en"],
                source="unit43-26-50#21b",
                segment=s2,
            ),
            item(
                "u43-221a",
                "zh2en",
                "毫无疑问（out of question）",
                "out of question",
                alts=["beyond question"],
                tags=["zh2en"],
                source="unit43-26-50#22a",
                segment=s2,
            ),
            item(
                "u43-221b",
                "zh2en",
                "不可能；办不到（out of the question）",
                "out of the question",
                tags=["zh2en"],
                source="unit43-26-50#22b",
                segment=s2,
            ),
            item(
                "u43-221c",
                "zh2en",
                "警察就事故询问了目击者",
                "The police questioned the witness about the accident",
                alts=["question sb about sth"],
                tags=["zh2en"],
                source="unit43-26-50#22c",
                segment=s2,
            ),
            item(
                "u43-222",
                "zh2en",
                "逐梦",
                "pursue one's dream",
                alts=["chase one's dream", "pursue a dream", "go after one's dream"],
                tags=["zh2en"],
                source="unit43-26-50#23",
                segment=s2,
            ),
            item(
                "u43-223",
                "word_form",
                "He travelled west ____(追求) fortune.",
                "in pursuit of",
                alts=["pursuing", "to pursue"],
                blanks=[blank("in pursuit of", alts=["pursuing", "to pursue"])],
                hint="pursue",
                tags=["word_form", "collocation"],
                source="unit43-26-50#24",
                segment=s2,
            ),
            item(
                "u43-224a",
                "zh2en",
                "毅然推行；努力争取",
                "push for",
                alts=["push ahead with", "push through"],
                tags=["zh2en"],
                source="unit43-26-50#25a",
                segment=s2,
            ),
            item(
                "u43-224b",
                "zh2en",
                "催促某人做……",
                "push sb to do",
                alts=["push someone to do sth", "urge sb to do"],
                tags=["zh2en"],
                source="unit43-26-50#25b",
                segment=s2,
            ),
            item(
                "u43-225a",
                "phrase_cluster",
                "把……收起/放好",
                "put away",
                related="u43-put",
                tags=["phrase"],
                source="unit43-26-50#26a",
                segment=s2,
            ),
            item(
                "u43-225b",
                "phrase_cluster",
                "放下；写下；镇压",
                "put down",
                related="u43-put",
                tags=["phrase"],
                source="unit43-26-50#26b",
                segment=s2,
            ),
            item(
                "u43-225c",
                "phrase_cluster",
                "推迟",
                "put off",
                related="u43-put",
                tags=["phrase"],
                source="unit43-26-50#26c",
                segment=s2,
            ),
            item(
                "u43-225d",
                "phrase_cluster",
                "增加体重",
                "put on weight",
                related="u43-put",
                tags=["phrase"],
                source="unit43-26-50#26d",
                segment=s2,
            ),
            item(
                "u43-225e",
                "phrase_cluster",
                "播放音乐",
                "put on music",
                alts=["put on some music"],
                related="u43-put",
                tags=["phrase"],
                source="unit43-26-50#26e",
                segment=s2,
            ),
            item(
                "u43-225f",
                "phrase_cluster",
                "请帮我接通经理",
                "put me through to the manager",
                alts=["put sb through to"],
                related="u43-put",
                tags=["phrase"],
                source="unit43-26-50#26f",
                segment=s2,
            ),
            item(
                "u43-225g",
                "phrase_cluster",
                "忍受",
                "put up with",
                related="u43-put",
                tags=["phrase"],
                source="unit43-26-50#26g",
                segment=s2,
            ),
            item(
                "u43-225h",
                "phrase_cluster",
                "搭帐篷",
                "put up a tent",
                related="u43-put",
                tags=["phrase"],
                source="unit43-26-50#26h",
                segment=s2,
            ),
            item(
                "u43-225i",
                "phrase_cluster",
                "一起商量；集思广益",
                "put our heads together",
                alts=["put your heads together"],
                related="u43-put",
                tags=["phrase"],
                source="unit43-26-50#26i",
                segment=s2,
            ),
            item(
                "u43-225j",
                "phrase_cluster",
                "简单地说",
                "to put it simply",
                alts=["put simply"],
                related="u43-put",
                tags=["phrase"],
                source="unit43-26-50#26j",
                segment=s2,
            ),
        ]
    )

    return {
        "unitId": "43",
        "name": "Unit 43 (prohibit—radiation)",
        "order": 43,
        "rangeFrom": "prohibit",
        "rangeTo": "radiation",
        "wordsPerUnit": 50,
        "items": items,
    }


def update_manifest(curated_file: str = "unit_43.json") -> None:
    man_path = ROOT / "content" / "curated" / "manifest.json"
    man = json.loads(man_path.read_text(encoding="utf-8"))
    found = False
    for u in man["units"]:
        if u["unitId"] == "43":
            u["hasContent"] = True
            u["file"] = curated_file
            u["name"] = "Unit 43 (prohibit—radiation)"
            u["rangeFrom"] = "prohibit"
            u["rangeTo"] = "radiation"
            u["wordsPerUnit"] = 50
            found = True
            break
    if not found:
        man["units"].append(
            {
                "unitId": "43",
                "name": "Unit 43 (prohibit—radiation)",
                "order": 43,
                "file": curated_file,
                "rangeFrom": "prohibit",
                "rangeTo": "radiation",
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
    out = ROOT / "content" / "curated" / "unit_43.json"
    out.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    update_manifest()
    # also drop a reviewed copy for audit trail
    review = ROOT / "content" / "review" / "unit_43.curated_candidate.json"
    review.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    seg = {"1-25": 0, "26-50": 0}
    for it in bank["items"]:
        seg[it["segment"]] = seg.get(it["segment"], 0) + 1
    print(f"wrote {out} items={len(bank['items'])} segments={seg}")


if __name__ == "__main__":
    main()
