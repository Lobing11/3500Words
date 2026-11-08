#!/usr/bin/env python3
"""Promote Units 52-54 into curated gold."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from promote_lib import blank, item, write_unit  # noqa: E402

CAT = json.loads(Path(r"D:\3500Words\content\catalog\units.json").read_text(encoding="utf-8"))
META = {str(u["unitId"]): u for u in CAT["units"]}


def wrap(builder):
    bank = builder()
    m = META.get(bank["unitId"], {})
    bank["name"] = m.get("displayName", bank["name"])
    bank["rangeFrom"] = m.get("rangeFrom", bank.get("rangeFrom"))
    bank["rangeTo"] = m.get("rangeTo", bank.get("rangeTo"))
    return bank


def unit52() -> dict:
    u = "52"
    s1, s2 = "1-25", "26-50"
    I = lambda *a, **k: item(u, *a, **k)
    items = [
        # 1-25
        I("u52-101", "cloze", "____ one's intention（说明意图）", "state", tags=["collocation"], source="unit52-1-25#1", segment=s1),
        I("u52-102", "zh2en", "据称", "It is stated that", alts=["allegedly", "It is claimed that"], tags=["zh2en"], source="unit52-1-25#2", segment=s1),
        I("u52-103", "zh2en", "起草声明", "draft a statement", alts=["draw up a statement", "make a statement"], tags=["zh2en"], source="unit52-1-25#3", segment=s1),
        I("u52-104", "zh2en", "使驻扎", "station", alts=["be stationed", "station troops"], tags=["zh2en"], source="unit52-1-25#4", segment=s1),
        I("u52-105", "zh2en", "在他家过夜", "stay over in his home", alts=["stay over"], tags=["zh2en"], source="unit52-1-25#5", segment=s1),
        I("u52-106", "zh2en", "牛排 / 钢 / 台湾海峡", "steak / steel / the Taiwan Straits", alts=["steak", "steel", "the Taiwan Strait"], tags=["zh2en"], source="unit52-1-25#6", segment=s1),
        I("u52-107", "zh2en", "便利贴", "sticky notes", alts=["a sticky note"], tags=["zh2en"], source="unit52-1-25#7", segment=s1),
        I("u52-108", "zh2en", "直截了当地说", "speak sth in a straightforward manner", alts=["in a straightforward manner", "straightforwardly"], tags=["zh2en"], source="unit52-1-25#8", segment=s1),
        I("u52-109", "zh2en", "一栋三层楼的建筑", "a three-story building", alts=["a three-storey building"], tags=["zh2en"], source="unit52-1-25#9", segment=s1),
        I("u52-110", "zh2en", "报纸刊登了一篇关于环保的报道", "The paper ran a story about environmental protection", alts=["run a story"], tags=["zh2en"], source="unit52-1-25#10", segment=s1),
        I("u52-111", "zh2en", "暴风雨的", "stormy", tags=["zh2en"], source="unit52-1-25#11", segment=s1),
        I("u52-112", "zh2en", "一句话不说冲出房间", "storm out of the room without a word", alts=["storm out"], tags=["zh2en"], source="unit52-1-25#12", segment=s1),
        I("u52-113", "zh2en", "溜出房间", "steal out of the room", alts=["slip out of the room", "sneak out of the room"], tags=["zh2en"], source="unit52-1-25#13", segment=s1),
        I("u52-114", "zh2en", "加快研究", "speed up the research", alts=["accelerate the research"], tags=["zh2en"], source="unit52-1-25#14", segment=s1),
        I("u52-115", "zh2en", "步某人后尘；效仿", "follow in one's steps", alts=["follow in sb's footsteps"], tags=["zh2en"], source="unit52-1-25#15", segment=s1),
        I("u52-116", "zh2en", "水壶在炉子上冒着蒸汽", "The kettle steamed on the stove", alts=["steam"], tags=["zh2en"], source="unit52-1-25#16", segment=s1),
        I("u52-117a", "phrase_cluster", "伸出舌头", "stick out one's tongue", related="u52-stick", tags=["phrase"], source="unit52-1-25#17a", segment=s1),
        I("u52-117b", "phrase_cluster", "在蓝天衬托下显得突出", "stick out against the blue sky", alts=["stand out against the blue sky"], related="u52-stick", tags=["phrase"], source="unit52-1-25#17b", segment=s1),
        I("u52-118", "zh2en", "陷在泥巴里", "be stuck in the mud", alts=["get stuck in the mud"], tags=["zh2en"], source="unit52-1-25#18", segment=s1),
        I("u52-119", "zh2en", "站着不动", "stand still", tags=["zh2en"], source="unit52-1-25#19", segment=s1),
        I("u52-120", "zh2en", "激发对……的兴趣", "stimulate interest in", alts=["arouse interest in"], tags=["zh2en"], source="unit52-1-25#20", segment=s1),
        I("u52-121", "cloze", "There are better days ____ you.（好日子等着我们）", "in store for", alts=["ahead of"], blanks=[blank("in store for", alts=["ahead of"])], tags=["collocation"], source="unit52-1-25#21", segment=s1),
        I("u52-122", "zh2en", "酒店离海滩只有一箭之遥", "The hotel is a stone's throw from the beach", alts=["a stone's throw from"], tags=["zh2en"], source="unit52-1-25#22", segment=s1),
        # 26-50
        I("u52-201", "zh2en", "易遭受", "be subject to", alts=["be liable to", "be prone to"], tags=["zh2en"], source="unit52-26-50#1", segment=s2),
        I("u52-202", "zh2en", "跑题", "get off the subject", alts=["go off the subject", "wander off the subject"], tags=["zh2en"], source="unit52-26-50#2", segment=s2),
        I("u52-203", "zh2en", "研究课题", "research subjects", alts=["research subject"], tags=["zh2en"], source="unit52-26-50#3", segment=s2),
        I("u52-204", "word_form", "She looks very ____(style) in that dress.", "stylish", hint="style", tags=["word_form"], source="unit52-26-50#4", segment=s2),
        I("u52-205", "zh2en", "把那些东西都收起来", "Put all that stuff away", alts=["put ... away", "stuff"], tags=["zh2en"], source="unit52-26-50#5", segment=s2),
        I("u52-206", "zh2en", "往口袋塞了些零食", "stuff some snacks into the pocket", alts=["stuff snacks into one's pocket"], tags=["zh2en"], source="unit52-26-50#6", segment=s2),
        I("u52-207a", "zh2en", "她仔细端详他的脸", "She studied his face carefully", alts=["study one's face"], tags=["zh2en"], source="unit52-26-50#7a", segment=s2),
        I("u52-207b", "zh2en", "他在书房里读书", "He is reading in his study", alts=["in one's study"], tags=["zh2en"], source="unit52-26-50#7b", segment=s2),
        I("u52-208", "zh2en", "文科 / 理科学生", "arts/science students", alts=["art students", "science students"], tags=["zh2en"], source="unit52-26-50#8", segment=s2),
        I("u52-209", "zh2en", "在雪中艰难跋涉", "struggle through the snow", alts=["trudge through the snow"], tags=["zh2en"], source="unit52-26-50#9", segment=s2),
        I("u52-210", "zh2en", "挣扎着站起来", "struggle to one's feet", alts=["struggle to stand up"], tags=["zh2en"], source="unit52-26-50#10", segment=s2),
        I("u52-211", "zh2en", "强忍着不哭", "struggle to hold back tears", alts=["fight back tears", "hold back tears"], tags=["zh2en"], source="unit52-26-50#11", segment=s2),
        I("u52-212", "zh2en", "对他来说接受这个变化很艰难", "It was a struggle for him to accept the change", alts=["a struggle to"], tags=["zh2en"], source="unit52-26-50#12", segment=s2),
        I("u52-213", "zh2en", "结构清晰的报告", "a well-structured report", tags=["zh2en"], source="unit52-26-50#13", segment=s2),
        I("u52-214", "zh2en", "组织自己的论点", "structure one's argument", tags=["zh2en"], source="unit52-26-50#14", segment=s2),
        I("u52-215", "zh2en", "她有很强的体力", "She has great physical strength", alts=["physical strength"], tags=["zh2en"], source="unit52-26-50#15", segment=s2),
        I("u52-216", "zh2en", "坚强的意志", "a strong will", alts=["strong will"], tags=["zh2en"], source="unit52-26-50#16", segment=s2),
        I("u52-217", "word_form", "Knowing your ____ will ____ your confidence.（strong）", "strengths|strengthen", blanks=[blank("strengths", 0, ["strength"]), blank("strengthen", 1)], hint="strong", tags=["word_form"], source="unit52-26-50#17", segment=s2),
        I("u52-218a", "zh2en", "吉他弦", "the strings of a guitar", alts=["guitar strings"], tags=["zh2en"], source="unit52-26-50#18a", segment=s2),
        I("u52-218b", "word_form", "Lanterns were ____(string) in the trees.", "strung", hint="string", tags=["word_form"], source="unit52-26-50#18b", segment=s2),
        I("u52-218c", "zh2en", "鞋带", "shoestrings", alts=["shoe strings", "shoelaces"], tags=["zh2en"], source="unit52-26-50#18c", segment=s2),
        I("u52-218d", "zh2en", "把绳子绷紧", "stretch the string tight", tags=["zh2en"], source="unit52-26-50#18d", segment=s2),
        I("u52-219", "zh2en", "对外国文化感到陌生", "be strange to foreign culture", alts=["be unfamiliar with foreign culture"], tags=["zh2en"], source="unit52-26-50#19", segment=s2),
        I("u52-220a", "phrase_cluster", "川流不息的访客", "a stream of visitors", related="u52-stream", tags=["phrase"], source="unit52-26-50#20a", segment=s2),
        I("u52-220b", "phrase_cluster", "顺着……流淌下来", "stream down", alts=["tears stream down"], related="u52-stream", tags=["phrase"], source="unit52-26-50#20b", segment=s2),
        I("u52-220c", "phrase_cluster", "山间小溪", "a mountain stream", related="u52-stream", tags=["phrase"], source="unit52-26-50#20c", segment=s2),
        I("u52-221a", "zh2en", "再怎么强调……的重要性也不为过", "I can't stress the importance of sth too much", alts=["cannot stress too much"], tags=["zh2en"], source="unit52-26-50#21a", segment=s2),
        I("u52-221b", "cloze", "____ stress / The ____ job made him feel ____.（stress）", "under|stressful|stressed", blanks=[blank("under", 0), blank("stressful", 1), blank("stressed", 2)], tags=["collocation", "word_form"], source="unit52-26-50#21b", segment=s2),
        I("u52-222", "cloze", "be strict ____ sb. ____ sth.", "with|in", blanks=[blank("with", 0), blank("in", 1, ["about"])], tags=["collocation"], source="unit52-26-50#22", segment=s2),
        I("u52-223", "word_form", "____(strike) features", "striking", hint="strike", tags=["word_form"], source="unit52-26-50#23", segment=s2),
        I("u52-224a", "zh2en", "我突然想到一个主意", "An idea struck me", alts=["It struck me that"], tags=["zh2en"], source="unit52-26-50#24a", segment=s2),
        I("u52-224b", "zh2en", "被她的外貌打动", "be struck by her appearance", tags=["zh2en"], source="unit52-26-50#24b", segment=s2),
    ]
    return {"unitId": "52", "name": "Unit 52", "order": 52, "wordsPerUnit": 50, "items": items}


def unit53() -> dict:
    u = "53"
    s1, s2 = "1-25", "26-50"
    I = lambda *a, **k: item(u, *a, **k)
    items = [
        I("u53-101", "word_form", "the deadline for ____(submit)", "submission", hint="submit", tags=["word_form"], source="unit53-all#9", segment=s1),
        I("u53-102a", "phrase_cluster", "提交申请", "submit an application", related="u53-submit", tags=["phrase"], source="unit53-all#10a", segment=s1),
        I("u53-102b", "phrase_cluster", "听天由命", "submit oneself to fate", related="u53-submit", tags=["phrase"], source="unit53-all#10b", segment=s1),
        I("u53-103a", "phrase_cluster", "赞同这个想法", "subscribe to the idea", related="u53-subscribe", tags=["phrase"], source="unit53-all#11a", segment=s1),
        I("u53-103b", "phrase_cluster", "订阅期刊", "subscribe to the journal", related="u53-subscribe", tags=["phrase"], source="unit53-all#11b", segment=s1),
        I("u53-103c", "phrase_cluster", "向慈善机构捐款/认捐", "subscribe to the charity", related="u53-subscribe", tags=["phrase"], source="unit53-all#11c", segment=s1),
        I("u53-104", "zh2en", "订阅者 / 订阅（n.）", "subscriber / subscription", alts=["subscriber", "subscription"], tags=["zh2en"], source="unit53-all#12", segment=s1),
        I("u53-105", "zh2en", "随后的实验", "subsequent experiments", tags=["zh2en"], source="unit53-all#13", segment=s1),
        I("u53-106", "zh2en", "地铁 / 大量的 / 极好的 / 外科医生 / 手术", "subway/substantial/superb/surgeon/surgery", tags=["zh2en"], source="unit53-all#14", segment=s1),
        I("u53-107a", "zh2en", "演讲的实质内容", "the substance of the speech", tags=["zh2en"], source="unit53-all#15a", segment=s1),
        I("u53-107b", "zh2en", "一种化学物质", "a chemical substance", tags=["zh2en"], source="unit53-all#15b", segment=s1),
        I("u53-108", "word_form", "perform a ____(surgery) operation", "surgical", hint="surgery", tags=["word_form"], source="unit53-all#16", segment=s1),
        I("u53-109a", "cloze", "succeed ____ doing", "in", tags=["collocation"], source="unit53-all#17a", segment=s1),
        I("u53-109b", "zh2en", "接替他担任主席", "succeed him as chairman", tags=["zh2en"], source="unit53-all#17b", segment=s1),
        I("u53-110", "word_form", "sufficient（反义词）", "insufficient", hint="sufficient", tags=["word_form"], source="unit53-all#18", segment=s1),
        I("u53-111", "cloze", "____ one's suggestion（根据）", "at", alts=["on"], blanks=[blank("at", alts=["on"])], tags=["collocation"], source="unit53-all#19", segment=s1),
        I("u53-112a", "word_form", "I suggest him ____(accept) the plan.", "accepting", hint="accept", tags=["word_form", "pattern"], source="unit53-all#20a", segment=s1),
        I("u53-112b", "word_form", "I suggest that he ____(calm) down, for his look suggests that he ____(be) very anxious.", "calm|is", blanks=[blank("calm", 0, ["should calm"]), blank("is", 1)], hint="suggest 虚拟 / 表明", tags=["word_form", "pattern"], source="unit53-all#20b", segment=s1),
        I("u53-113", "cloze", "be suited ____ / be suitable ____（适合于）", "to|for", blanks=[blank("to", 0, ["for"]), blank("for", 1, ["to"])], tags=["collocation"], source="unit53-all#21", segment=s1),
        I("u53-114", "zh2en", "总结，归纳（两个）", "sum up / summarize", alts=["sum up", "summarise", "make a summary"], tags=["zh2en"], source="unit53-all#22", segment=s1),
        I("u53-115", "zh2en", "救援物资", "relief supplies", tags=["zh2en"], source="unit53-all#23", segment=s2),
        I("u53-116", "cloze", "supply sb. ____ sth. / supply sth. ____ sb.", "with|to", blanks=[blank("with", 0), blank("to", 1, ["for"])], tags=["collocation"], source="unit53-all#24", segment=s2),
        I("u53-117", "word_form", "support（形容词）", "supportive", hint="support", tags=["word_form"], source="unit53-all#25a", segment=s2),
        I("u53-118", "word_form", "Everyone is supposed ____(obey) the school rules.", "to obey", hint="obey", tags=["word_form", "pattern"], source="unit53-all#25b", segment=s2),
        I("u53-119", "word_form", "He has a sense of ____(superior), thinking he is superior ____ everyone else.", "superiority|to", blanks=[blank("superiority", 0), blank("to", 1)], hint="superior", tags=["word_form"], source="unit53-all#27", segment=s2),
        I("u53-120", "word_form", "____(suppose) you are wrong, what will you do?", "Supposing", alts=["Suppose"], blanks=[blank("Supposing", alts=["Suppose"])], hint="suppose", tags=["word_form", "pattern"], source="unit53-all#28", segment=s2),
        I("u53-121", "zh2en", "不足为奇", "It is no surprise that", alts=["No wonder", "It is not surprising that"], tags=["zh2en"], source="unit53-all#29", segment=s2),
        I("u53-122", "zh2en", "出其不意地做某事；使某人吃惊", "take sth by surprise", alts=["take sb by surprise"], tags=["zh2en"], source="unit53-all#30", segment=s2),
        I("u53-123a", "zh2en", "进行调查", "conduct a survey", alts=["make a survey", "carry out a survey"], tags=["zh2en"], source="unit53-all#31a", segment=s2),
        I("u53-123b", "word_form", "He likes the ____ woods and enjoys the peaceful ____.（surround）", "surrounding|surroundings", blanks=[blank("surrounding", 0), blank("surroundings", 1)], hint="surround", tags=["word_form"], source="unit53-all#31b", segment=s2),
        I("u53-124a", "word_form", "a ____(sustain) effort", "sustained", hint="sustain", tags=["word_form"], source="unit53-all#4a", segment=s2),
        I("u53-124b", "word_form", "promote ____(sustain) development", "sustainable", hint="sustain", tags=["word_form"], source="unit53-all#4b", segment=s2),
        I("u53-125a", "zh2en", "被停职", "be suspended from office", tags=["zh2en"], source="unit53-all#5a", segment=s2),
        I("u53-125b", "zh2en", "把灯吊在天花板上", "suspend a lamp from the ceiling", tags=["zh2en"], source="unit53-all#5b", segment=s2),
        I("u53-126", "zh2en", "适者生存", "survival of the fittest", tags=["zh2en"], source="unit53-all#6", segment=s2),
        I("u53-127", "zh2en", "她比丈夫多活了五年", "He survived her husband by 5 years", alts=["survive sb by"], tags=["zh2en"], source="unit53-all#7", segment=s2),
        I("u53-128", "cloze", "survive ____ my salary", "on", tags=["collocation"], source="unit53-all#8", segment=s2),
    ]
    return {"unitId": "53", "name": "Unit 53", "order": 53, "wordsPerUnit": 50, "items": items}


def unit54() -> dict:
    u = "54"
    s1, s2 = "1-25", "26-50"
    I = lambda *a, **k: item(u, *a, **k)
    items = [
        I("u54-101", "zh2en", "荡秋千", "play on the swing", alts=["play the swing", "swing"], tags=["zh2en"], source="unit54-all#46", segment=s1),
        I("u54-102", "zh2en", "打开收音机", "switch on the radio", alts=["turn on the radio"], tags=["zh2en"], source="unit54-all#2", segment=s1),
        I("u54-103", "zh2en", "象征（v./n./adj.）", "symbolize / symbol / symbolic", alts=["symbolise", "symbol", "symbolic"], tags=["zh2en"], source="unit54-all#3", segment=s1),
        I("u54-104", "zh2en", "同情（v./n./adj.）", "sympathize / sympathy / sympathetic", alts=["sympathise", "sympathy", "sympathetic"], tags=["zh2en"], source="unit54-all#4", segment=s1),
        I("u54-105", "zh2en", "系统的", "systematic", tags=["zh2en"], source="unit54-all#5", segment=s1),
        I("u54-106", "zh2en", "摆桌子（吃饭）", "set the table", alts=["lay the table"], tags=["zh2en"], source="unit54-all#6", segment=s1),
        I("u54-107", "zh2en", "平板电脑；药片", "tablet", tags=["zh2en"], source="unit54-all#7", segment=s1),
        I("u54-108", "zh2en", "处理；应对（tackle）", "tackle", alts=["tackle a problem"], tags=["zh2en"], source="unit54-all#8", segment=s1),
        I("u54-109", "zh2en", "摇尾巴", "wag its tail", alts=["wag one's tail"], tags=["zh2en"], source="unit54-all#9", segment=s1),
        I("u54-110", "zh2en", "按照你的需求定制", "tailor ... to your needs", alts=["be tailored to your needs", "customize to your needs"], tags=["zh2en"], source="unit54-all#10", segment=s1),
        I("u54-111", "zh2en", "发短信告诉我最终结果", "text me the final result", alts=["send me a text about the final result"], tags=["zh2en"], source="unit54-all#11", segment=s1),
        I("u54-112", "zh2en", "经受考验", "stand the test", alts=["stand the test of time"], tags=["zh2en"], source="unit54-all#12", segment=s1),
        I("u54-113", "zh2en", "把某人吓哭", "scare sb into tears", alts=["frighten sb into tears", "scare someone to tears"], tags=["zh2en"], source="unit54-all#13", segment=s1),
        I("u54-114", "zh2en", "合同条款", "the terms of the contract", tags=["zh2en"], source="unit54-all#14", segment=s1),
        I("u54-115", "zh2en", "就……而言；在……方面", "in terms of", tags=["zh2en"], source="unit54-all#15", segment=s1),
        I("u54-116", "zh2en", "与……关系良好", "be on good terms with", tags=["zh2en"], source="unit54-all#16", segment=s1),
        I("u54-117", "zh2en", "法律术语", "a legal term", tags=["zh2en"], source="unit54-all#17", segment=s1),
        I("u54-118", "zh2en", "缓解紧张", "relieve tension", alts=["ease tension", "reduce tension"], tags=["zh2en"], source="unit54-all#18", segment=s1),
        I("u54-119", "zh2en", "泪流满面", "be in tears", alts=["burst into tears", "tears stream down"], tags=["zh2en"], source="unit54-all#19", segment=s1),
        I("u54-120", "zh2en", "抑制住眼泪", "hold back tears", alts=["fight back tears"], tags=["zh2en"], source="unit54-all#20", segment=s1),
        I("u54-121", "word_form", "tear（形容词）", "tearful", hint="tear", tags=["word_form"], source="unit54-all#21", segment=s1),
        I("u54-122", "zh2en", "营销技巧", "marketing techniques", alts=["marketing skills"], tags=["zh2en"], source="unit54-all#22", segment=s1),
        I("u54-123", "zh2en", "区分", "tell ... apart", alts=["distinguish", "tell A from B"], tags=["zh2en"], source="unit54-all#23", segment=s1),
        I("u54-124", "zh2en", "算命", "tell fortunes", alts=["tell sb's fortune"], tags=["zh2en"], source="unit54-all#24", segment=s1),
        I("u54-125", "zh2en", "出纳员；讲述者", "teller", tags=["zh2en"], source="unit54-all#25", segment=s2),
        I("u54-126", "zh2en", "量体温", "take one's temperature", alts=["take sb's temperature"], tags=["zh2en"], source="unit54-all#26", segment=s2),
        I("u54-127", "zh2en", "照料病人", "tend to the sick", alts=["tend the sick"], tags=["zh2en"], source="unit54-all#27", segment=s2),
        I("u54-128", "zh2en", "往往会", "tend to", alts=["have a tendency to"], tags=["zh2en"], source="unit54-all#28", segment=s2),
        I("u54-129", "zh2en", "左右为难", "be in a dilemma", alts=["be torn between", "on the horns of a dilemma"], tags=["zh2en"], source="unit54-all#29", segment=s2),
        I("u54-130", "zh2en", "拆除历史遗产", "tear down the historic heritage", alts=["tear down"], tags=["zh2en"], source="unit54-all#30", segment=s2),
        I("u54-131", "zh2en", "依依不舍地离开", "tear oneself away", alts=["be reluctant to leave"], tags=["zh2en"], source="unit54-all#31", segment=s2),
        I("u54-132", "zh2en", "沏茶", "make tea", alts=["brew tea"], tags=["zh2en"], source="unit54-all#32", segment=s2),
        I("u54-133", "zh2en", "征税", "impose a tax", alts=["levy a tax", "tax"], tags=["zh2en"], source="unit54-all#33", segment=s2),
        I("u54-134", "zh2en", "投合某人的口味", "suit one's taste", alts=["to one's taste"], tags=["zh2en"], source="unit54-all#34", segment=s2),
        I("u54-135", "zh2en", "尝起来有……味", "taste of", alts=["taste like"], tags=["zh2en"], source="unit54-all#35", segment=s2),
        I("u54-136", "zh2en", "美味的，可口的", "tasty", alts=["delicious"], tags=["zh2en"], source="unit54-all#36", segment=s2),
        I("u54-137", "zh2en", "针对于", "be targeted at", alts=["target", "aim at"], tags=["zh2en"], source="unit54-all#37", segment=s2),
        I("u54-138", "zh2en", "终点线", "the finishing tape", alts=["the finishing line"], tags=["zh2en"], source="unit54-all#38", segment=s2),
        I("u54-139", "zh2en", "劝服某人做……", "talk sb into doing", alts=["persuade sb to do"], tags=["zh2en"], source="unit54-all#39", segment=s2),
        I("u54-140", "cloze", "have a talent ____ sth / be talented ____", "for|in", blanks=[blank("for", 0), blank("in", 1, ["at"])], tags=["collocation"], source="unit54-all#40", segment=s2),
        I("u54-141a", "phrase_cluster", "把……误当作", "take ... for", related="u54-take", tags=["phrase"], source="unit54-all#41", segment=s2),
        I("u54-141b", "phrase_cluster", "吸收；理解；欺骗", "take in", related="u54-take", tags=["phrase"], source="unit54-all#42", segment=s2),
        I("u54-141c", "phrase_cluster", "记下；拆除", "take down", related="u54-take", tags=["phrase"], source="unit54-all#43", segment=s2),
        I("u54-141d", "phrase_cluster", "接管", "take over", related="u54-take", tags=["phrase"], source="unit54-all#44", segment=s2),
        I("u54-141e", "phrase_cluster", "退休后开始学画", "take up the painting after retirement", alts=["take up painting"], related="u54-take", tags=["phrase"], source="unit54-all#45", segment=s2),
        I("u54-142", "zh2en", "甩背；摆背（按课堂语境）", "swing one's back", alts=["swing"], tags=["zh2en"], source="unit54-all#1", segment=s1),
    ]
    return {"unitId": "54", "name": "Unit 54", "order": 54, "wordsPerUnit": 50, "items": items}


def main() -> None:
    for builder in (unit52, unit53, unit54):
        write_unit(wrap(builder))


if __name__ == "__main__":
    main()
