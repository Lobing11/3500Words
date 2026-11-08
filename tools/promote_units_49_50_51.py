#!/usr/bin/env python3
"""Promote Units 49, 50, 51 into curated gold."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from promote_lib import blank, item, write_unit  # noqa: E402


def unit49() -> dict:
    u = "49"
    s1, s2 = "1-25", "26-50"
    I = lambda *a, **k: item(u, *a, **k)
    items = [
        I("u49-101", "cloze", "____(一看到) his mother, the boy's eyes lit up.", "At the sight of", alts=["On seeing", "Seeing"], blanks=[blank("At the sight of", alts=["On seeing", "Seeing"])], tags=["collocation", "pattern"], source="unit49-1-25#1", segment=s1),
        I("u49-102", "zh2en", "观光", "go sightseeing", alts=["sightseeing", "do sightseeing"], tags=["zh2en"], source="unit49-1-25#2", segment=s1),
        I("u49-103", "zh2en", "洗掉床单上的污渍", "wash the stained sheet", alts=["wash the stained sheets"], tags=["zh2en"], source="unit49-1-25#3", segment=s1),
        I("u49-104", "zh2en", "避雨", "take shelter from the rain", alts=["shelter from the rain", "seek shelter from the rain"], tags=["zh2en"], source="unit49-1-25#4", segment=s1),
        I("u49-105", "zh2en", "动物收容所", "an animal shelter", alts=["animal shelter"], tags=["zh2en"], source="unit49-1-25#5", segment=s1),
        I("u49-106", "zh2en", "推卸责任", "shift the blame", alts=["shift the blame onto"], tags=["zh2en"], source="unit49-1-25#6", segment=s1),
        I("u49-107", "zh2en", "夜班", "night shifts", alts=["night shift", "work the night shift"], tags=["zh2en"], source="unit49-1-25#7", segment=s1),
        I("u49-108", "zh2en", "他学业出色", "He shines academically", alts=["shine academically"], tags=["zh2en"], source="unit49-1-25#8", segment=s1),
        I("u49-109", "zh2en", "运送货物；发货", "ship goods", alts=["ship the goods"], tags=["zh2en"], source="unit49-1-25#9", segment=s1),
        I("u49-110", "zh2en", "电击", "an electric shock", alts=["electric shock"], tags=["zh2en"], source="unit49-1-25#10", segment=s1),
        I("u49-111", "zh2en", "换位思考", "put oneself in sb's shoes", alts=["put yourself in someone's shoes", "stand in sb's shoes"], tags=["zh2en"], source="unit49-1-25#11", segment=s1),
        I("u49-112", "zh2en", "射门得分", "shoot a goal", alts=["score a goal"], tags=["zh2en"], source="unit49-1-25#12", segment=s1),
        I("u49-113a", "phrase_cluster", "猛长；蹿高", "shoot up", related="u49-shoot", tags=["phrase"], source="unit49-1-25#13a", segment=s1),
        I("u49-113b", "phrase_cluster", "销售额飙升", "The sales shot up", alts=["sales shot up"], related="u49-shoot", tags=["phrase"], source="unit49-1-25#13b", segment=s1),
        I("u49-114", "zh2en", "这段视频的每个镜头都在桂林拍摄", "Every shot in this video was shot in Guilin", alts=["shot in Guilin"], tags=["zh2en"], source="unit49-1-25#14", segment=s1),
        I("u49-115", "cloze", "____ shore（离海岸不远处）", "off", tags=["collocation"], source="unit49-1-25#15", segment=s1),
        I("u49-116a", "phrase_cluster", "缺少", "be short of", related="u49-short", tags=["phrase"], source="unit49-1-25#16a", segment=s1),
        I("u49-116b", "phrase_cluster", "是……的缩写", "be short for", related="u49-short", tags=["phrase"], source="unit49-1-25#16b", segment=s1),
        I("u49-116c", "phrase_cluster", "简称某物", "call sth for short", alts=["call sth short"], related="u49-short", tags=["phrase"], source="unit49-1-25#16c", segment=s1),
        I("u49-116d", "phrase_cluster", "走捷径", "take a short cut", alts=["take a shortcut"], related="u49-short", tags=["phrase"], source="unit49-1-25#16d", segment=s1),
        I("u49-116e", "zh2en", "学英语没捷径", "There is no short cut to learning English", alts=["no shortcut to learning English"], tags=["zh2en"], source="unit49-1-25#16e", segment=s1),
        I("u49-117", "word_form", "There is a ____(short) of money.", "shortage", hint="short", tags=["word_form"], source="unit49-1-25#17", segment=s1),
        I("u49-118", "zh2en", "肩并肩（两个）", "shoulder to shoulder / side by side", alts=["shoulder to shoulder", "side by side"], tags=["zh2en"], source="unit49-1-25#18", segment=s1),
        I("u49-119a", "phrase_cluster", "带领某人参观", "show sb around", alts=["show someone around"], related="u49-show", tags=["phrase"], source="unit49-1-25#19a", segment=s1),
        I("u49-119b", "phrase_cluster", "炫耀", "show off", related="u49-show", tags=["phrase"], source="unit49-1-25#19b", segment=s1),
        I("u49-119c", "phrase_cluster", "到场；露面", "show up", related="u49-show", tags=["phrase"], source="unit49-1-25#19c", segment=s1),
        I("u49-120a", "phrase_cluster", "一阵掌声", "a shower of applause", related="u49-shower", tags=["phrase"], source="unit49-1-25#18b", segment=s1),
        I("u49-120b", "phrase_cluster", "送他大量礼物", "People showered him with gifts", alts=["shower sb with"], related="u49-shower", tags=["phrase"], source="unit49-1-25#18c", segment=s1),
        I("u49-121", "zh2en", "厌倦", "be sick of", alts=["be tired of", "be fed up with"], tags=["zh2en"], source="unit49-1-25#19b", segment=s1),
        I("u49-122", "zh2en", "晕船 / 想家", "seasick / homesick", alts=["seasick", "homesick"], tags=["zh2en"], source="unit49-1-25#20", segment=s1),
        I("u49-123", "zh2en", "站在某人一边；支持某人", "be on one's side", alts=["be on sb's side", "take one's side"], tags=["zh2en"], source="unit49-1-25#21", segment=s1),
        # 26-50 (deduped)
        I("u49-201", "zh2en", "把这封信寄给校长。", "Send this letter to the headmaster", alts=["Post this letter to the principal"], tags=["zh2en"], source="unit49-26-50#1a", segment=s2),
        I("u49-202", "word_form", "Much work ____(finish), I can't go out.", "unfinished", alts=["having been unfinished", "not finished"], blanks=[blank("unfinished", alts=["not finished"])], hint="finish / 独立主格", tags=["word_form", "pattern"], source="unit49-26-50#2", segment=s2),
        I("u49-203", "word_form", "All things ____(consider), he didn't mean to hurt you.", "considered", hint="consider / 独立主格", tags=["word_form", "pattern"], source="unit49-26-50#3", segment=s2),
        I("u49-204", "zh2en", "签协议", "sign an agreement", alts=["sign a contract"], tags=["zh2en"], source="unit49-26-50#1b", segment=s2),
        I("u49-205", "zh2en", "手语", "sign language", tags=["zh2en"], source="unit49-26-50#2b", segment=s2),
        I("u49-206", "zh2en", "交通标志", "a traffic sign", alts=["traffic sign"], tags=["zh2en"], source="unit49-26-50#3b", segment=s2),
        I("u49-207", "zh2en", "示意某人做……（三个）", "sign to sb to do / signal sb to do / motion to sb to do", alts=["sign to sb to do", "signal sb to do", "motion to sb to do"], tags=["zh2en"], source="unit49-26-50#4", segment=s2),
        I("u49-208", "zh2en", "真实签名", "genuine signature", alts=["a genuine signature"], tags=["zh2en"], source="unit49-26-50#5", segment=s2),
        I("u49-209", "zh2en", "学业表现显著提升", "a significant improvement in academic performance", tags=["zh2en"], source="unit49-26-50#6", segment=s2),
        I("u49-210", "cloze", "It's silly ____ sb. to do", "of", tags=["collocation"], source="unit49-26-50#7", segment=s2),
        I("u49-211", "cloze", "be similar ____", "to", tags=["collocation"], source="unit49-26-50#8", segment=s2),
        I("u49-212a", "word_form", "____(simple) the concept", "simplify", hint="simple", tags=["word_form"], source="unit49-26-50#9a", segment=s2),
        I("u49-212b", "word_form", "a ____(simple) version of the App", "simplified", hint="simple", tags=["word_form"], source="unit49-26-50#9b", segment=s2),
        I("u49-213a", "zh2en", "这只是时间问题，别担心", "It is simply a matter of time", alts=["simply a matter of time"], tags=["zh2en"], source="unit49-26-50#10a", segment=s2),
        I("u49-213b", "zh2en", "黄山简直太美了", "Huangshan is simply amazing", tags=["zh2en"], source="unit49-26-50#10b", segment=s2),
        I("u49-214", "zh2en", "表达由衷的感谢", "express sincere thanks", alts=["express heartfelt thanks", "express sincere gratitude"], tags=["zh2en"], source="unit49-26-50#11", segment=s2),
        I("u49-215", "zh2en", "单程票 / 往返票", "a single/return ticket", alts=["single ticket", "return ticket", "one-way ticket", "round-trip ticket"], tags=["zh2en"], source="unit49-26-50#12", segment=s2),
        I("u49-216", "zh2en", "我的心消沉下来。", "My heart sank", alts=["one's heart sinks"], tags=["zh2en"], source="unit49-26-50#13", segment=s2),
        I("u49-217", "zh2en", "坐直；熬夜", "sit up", alts=["sit up late"], tags=["zh2en"], source="unit49-26-50#14", segment=s2),
        I("u49-218", "zh2en", "营地", "campsite", alts=["camp site", "camping site"], tags=["zh2en"], source="unit49-26-50#15", segment=s2),
        I("u49-219", "cloze", "I encountered a situation ____ I had to make a hard choice.", "where", alts=["in which"], blanks=[blank("where", alts=["in which"])], tags=["collocation", "pattern"], source="unit49-26-50#16", segment=s2),
        I("u49-220", "cloze", "The boxes are ____ different sizes.", "of", tags=["collocation"], source="unit49-26-50#17", segment=s2),
    ]
    return {
        "unitId": "49",
        "name": "Unit 49 (sheet—side)",
        "order": 49,
        "rangeFrom": "sheet",
        "rangeTo": "side",
        "wordsPerUnit": 50,
        "items": items,
    }


def unit50() -> dict:
    u = "50"
    s1, s2 = "1-25", "26-50"
    I = lambda *a, **k: item(u, *a, **k)
    # catalog: side—smoke? check
    items = [
        I("u50-101", "zh2en", "逃课", "skip class", alts=["cut class", "play truant", "skip school"], tags=["zh2en"], source="unit50-1-25#1", segment=s1),
        I("u50-102", "zh2en", "滑板 / 滑雪者", "skateboard / skier", alts=["skateboard", "skier"], tags=["zh2en"], source="unit50-1-25#2", segment=s1),
        I("u50-103", "zh2en", "瞌睡的", "sleepy", alts=["drowsy"], tags=["zh2en"], source="unit50-1-25#3", segment=s1),
        I("u50-104", "zh2en", "一份利润 / 一片面包", "a slice of the profit / a slice of bread", alts=["a slice of the profit", "a slice of bread"], tags=["zh2en"], source="unit50-1-25#4", segment=s1),
        I("u50-105", "zh2en", "溜进房间", "slip into the room", alts=["sneak into the room"], tags=["zh2en"], source="unit50-1-25#5", segment=s1),
        I("u50-106", "zh2en", "不知不觉染上坏习惯", "slip into a bad habit", alts=["fall into a bad habit"], tags=["zh2en"], source="unit50-1-25#6", segment=s1),
        I("u50-107a", "phrase_cluster", "略微增加", "a slight increase", related="u50-slight", tags=["phrase"], source="unit50-1-25#7a", segment=s1),
        I("u50-107b", "phrase_cluster", "苗条身材", "a slight figure", related="u50-slight", tags=["phrase"], source="unit50-1-25#7b", segment=s1),
        I("u50-107c", "phrase_cluster", "一点儿也不", "not in the slightest", related="u50-slight", tags=["phrase"], source="unit50-1-25#7c", segment=s1),
        I("u50-108", "zh2en", "成功的希望渺茫", "a slim chance of success", alts=["slim chances"], tags=["zh2en"], source="unit50-1-25#8", segment=s1),
        I("u50-109a", "phrase_cluster", "她在减肥", "She is slimming down", alts=["slim down"], related="u50-slim", tags=["phrase"], source="unit50-1-25#9a", segment=s1),
        I("u50-109b", "phrase_cluster", "精简人员", "slim down the staff", related="u50-slim", tags=["phrase"], source="unit50-1-25#9b", segment=s1),
        I("u50-110a", "phrase_cluster", "时间悄然流逝", "Time is slipping away", alts=["slip away"], related="u50-slip", tags=["phrase"], source="unit50-1-25#10a", segment=s1),
        I("u50-110b", "phrase_cluster", "他的名字我一时想不起来了", "His name slipped my mind", alts=["slip one's mind"], related="u50-slip", tags=["phrase"], source="unit50-1-25#10b", segment=s1),
        I("u50-110c", "phrase_cluster", "盘子从我手里滑落", "The plate slipped from my hand", related="u50-slip", tags=["phrase"], source="unit50-1-25#10c", segment=s1),
        I("u50-110d", "phrase_cluster", "口误", "a slip of the tongue", alts=["a slip of tounge"], related="u50-slip", tags=["phrase"], source="unit50-1-25#10d", segment=s1),
        I("u50-111a", "zh2en", "他迈着轻快的步伐出发了", "He set off at a smart pace", alts=["at a smart pace"], tags=["zh2en"], source="unit50-1-25#11a", segment=s1),
        I("u50-111b", "zh2en", "穿着得体", "dress smartly", tags=["zh2en"], source="unit50-1-25#11b", segment=s1),
        I("u50-112", "zh2en", "闻起来有油漆味", "smell of paint", alts=["smell like paint"], tags=["zh2en"], source="unit50-1-25#12", segment=s1),
        I("u50-113", "zh2en", "臭袜子", "smelly socks", tags=["zh2en"], source="unit50-1-25#13", segment=s1),
        I("u50-114", "zh2en", "消除困难；扫清障碍", "smooth away difficulties", alts=["smooth out difficulties", "remove difficulties"], tags=["zh2en"], source="unit50-1-25#14", segment=s1),
        I("u50-115", "zh2en", "小吃店；快餐柜台", "a snack bar", alts=["snack bar"], tags=["zh2en"], source="unit50-1-25#15", segment=s1),
        # 26-50
        I("u50-201", "zh2en", "与……打交道", "deal with", alts=["do with", "handle"], tags=["zh2en"], source="unit50-26-50#1", segment=s2),
        I("u50-202", "zh2en", "加入辩论社", "join the debating society", alts=["join in the debating society"], tags=["zh2en"], source="unit50-26-50#2a", segment=s2),
        I("u50-203", "word_form", "His words ____(soft) my anxiety.", "softened", hint="soft", tags=["word_form"], source="unit50-26-50#2b", segment=s2),
        I("u50-204", "zh2en", "太阳能电池板 / 太阳能电池", "a solar panel / a solar cell", alts=["solar panel", "solar cell"], tags=["zh2en"], source="unit50-26-50#4", segment=s2),
        I("u50-205", "zh2en", "大厅挤得满满当当", "The hall was packed solid", alts=["packed solid"], tags=["zh2en"], source="unit50-26-50#5", segment=s2),
        I("u50-206", "word_form", "The crisis strengthened the ____(solid) among team members.", "solidarity", hint="solid", tags=["word_form"], source="unit50-26-50#6", segment=s2),
        I("u50-207", "zh2en", "打下坚实的基础", "lay a solid foundation", alts=["build a solid foundation"], tags=["zh2en"], source="unit50-26-50#7", segment=s2),
        I("u50-208", "zh2en", "……的解决方法", "a solution to", alts=["the solution to"], tags=["zh2en"], source="unit50-26-50#8", segment=s2),
        I("u50-209", "zh2en", "解谜", "solve a puzzle", alts=["solve the puzzle"], tags=["zh2en"], source="unit50-26-50#9", segment=s2),
        I("u50-210a", "zh2en", "我们总会设法完成任务", "We will somehow finish the task", alts=["somehow"], tags=["zh2en"], source="unit50-26-50#10a", segment=s2),
        I("u50-210b", "zh2en", "我对村子很熟，但不知怎的还是迷路了", "somehow I got lost", alts=["but somehow I got lost"], tags=["zh2en"], source="unit50-26-50#10b", segment=s2),
        I("u50-211", "zh2en", "他算得上是个专家", "He is something of an expert", alts=["something of"], tags=["zh2en"], source="unit50-26-50#11", segment=s2),
    ]
    return {
        "unitId": "50",
        "name": "Unit 50 (side—somehow)",
        "order": 50,
        "rangeFrom": "side",
        "rangeTo": "somehow",
        "wordsPerUnit": 50,
        "items": items,
    }


def unit51() -> dict:
    u = "51"
    s1, s2 = "1-25", "26-50"
    I = lambda *a, **k: item(u, *a, **k)
    items = [
        I("u51-101", "zh2en", "有几分；有点儿累", "feel somewhat/sort of exhausted", alts=["somewhat exhausted", "sort of exhausted"], tags=["zh2en"], source="unit51-1-25#1", segment=s1),
        I("u51-102", "zh2en", "我们刚出发就开始下雨（Soon）", "We had hardly set off when it began to rain", alts=["Soon after we set off, it began to rain", "No sooner had we set off than it began to rain"], tags=["zh2en", "pattern"], source="unit51-1-25#2", segment=s1),
        I("u51-103", "zh2en", "发表演讲；致辞", "deliver an address", alts=["make an address", "give an address"], tags=["zh2en"], source="unit51-1-25#3", segment=s1),
        I("u51-104", "zh2en", "气得说不出话来", "be speechless with anger", alts=["speechless with rage"], tags=["zh2en"], source="unit51-1-25#4", segment=s1),
        I("u51-105", "zh2en", "设定具体目标", "set specific goals", tags=["zh2en"], source="unit51-1-25#5", segment=s1),
        I("u51-106", "zh2en", "儿童特有的疾病", "a disease specific to children", tags=["zh2en"], source="unit51-1-25#6", segment=s1),
        I("u51-107", "word_form", "sorrow（形容词）", "sorrowful", hint="sorrow", tags=["word_form"], source="unit51-1-25#7", segment=s1),
        I("u51-108", "zh2en", "同情某人", "be sorry for sb", alts=["feel sorry for sb"], tags=["zh2en"], source="unit51-1-25#8", segment=s1),
        I("u51-109a", "phrase_cluster", "整理抽屉", "sort out the drawer", related="u51-sort", tags=["phrase"], source="unit51-1-25#9a", segment=s1),
        I("u51-109b", "phrase_cluster", "按等级给苹果分类", "sort the apples by grade", related="u51-sort", tags=["phrase"], source="unit51-1-25#9b", segment=s1),
        I("u51-110a", "phrase_cluster", "勉强糊口", "keep body and soul together", related="u51-soul", tags=["phrase"], source="unit51-1-25#10a", segment=s1),
        I("u51-110b", "phrase_cluster", "全心全意为某人服务", "serve sb heart and soul", alts=["heart and soul"], related="u51-soul", tags=["phrase"], source="unit51-1-25#10b", segment=s1),
        I("u51-111a", "phrase_cluster", "从……采购", "source sth from", related="u51-source", tags=["phrase"], source="unit51-1-25#11a", segment=s1),
        I("u51-111b", "phrase_cluster", "冲突的根源", "the source of the conflict", related="u51-source", tags=["phrase"], source="unit51-1-25#11b", segment=s1),
        I("u51-111c", "phrase_cluster", "海的源头；源头", "the source of the sea", alts=["the source of a river"], related="u51-source", tags=["phrase"], source="unit51-1-25#11c", segment=s1),
        I("u51-112a", "phrase_cluster", "提出合理建议", "offer some sound advice", related="u51-sound", tags=["phrase"], source="unit51-1-25#12a", segment=s1),
        I("u51-112b", "phrase_cluster", "安然无恙", "safe and sound", related="u51-sound", tags=["phrase"], source="unit51-1-25#12b", segment=s1),
        I("u51-112c", "phrase_cluster", "酣睡", "a sound sleep", related="u51-sound", tags=["phrase"], source="unit51-1-25#12c", segment=s1),
        I("u51-112d", "phrase_cluster", "鸣笛", "sound the whistle", related="u51-sound", tags=["phrase"], source="unit51-1-25#12d", segment=s1),
        I("u51-113", "word_form", "south（形容词）", "southern", hint="south", tags=["word_form"], source="unit51-1-25#14", segment=s1),
        I("u51-114a", "word_form", "sow（过去式、过去分词）", "sowed/sown", alts=["sowed", "sown"], blanks=[blank("sowed/sown", alts=["sowed", "sown"])], hint="sow", tags=["word_form"], source="unit51-1-25#15a", segment=s1),
        I("u51-114b", "zh2en", "省得你跑一趟公司", "spare you a visit to the company", alts=["spare sb a visit"], tags=["zh2en"], source="unit51-1-25#15b", segment=s1),
        I("u51-114c", "zh2en", "备用钥匙", "a spare key", tags=["zh2en"], source="unit51-1-25#15c", segment=s1),
        I("u51-114d", "zh2en", "为无家可归者想一想", "spare a thought for the homeless", tags=["zh2en"], source="unit51-1-25#15d", segment=s1),
        I("u51-115a", "phrase_cluster", "充分说明", "speak volumes for", related="u51-speak", tags=["phrase"], source="unit51-1-25#17a", segment=s1),
        I("u51-115b", "phrase_cluster", "说某人坏话", "speak ill of sb", related="u51-speak", tags=["phrase"], source="unit51-1-25#17b", segment=s1),
        I("u51-116", "word_form", "a ____(speak) agreement", "spoken", hint="speak", tags=["word_form"], source="unit51-1-25#18", segment=s1),
        I("u51-117", "zh2en", "把手机接到扬声器上", "Connect your phone to the speaker", alts=["connect to the speaker"], tags=["zh2en"], source="unit51-1-25#19", segment=s1),
        I("u51-118", "zh2en", "特价出售", "be on special offer", alts=["on special offer"], tags=["zh2en"], source="unit51-1-25#20", segment=s1),
        I("u51-119", "zh2en", "专攻于；专门从事", "specialize in", alts=["specialise in", "be specialized in"], tags=["zh2en"], source="unit51-1-25#21", segment=s1),
        # 26-50
        I("u51-201", "zh2en", "首先；第一", "to start with", alts=["for a start", "first of all"], tags=["zh2en"], source="unit51-26-50#1", segment=s2),
        I("u51-202", "zh2en", "开始；起步", "make a start", tags=["zh2en"], source="unit51-26-50#2", segment=s2),
        I("u51-203", "word_form", "die of ____(starve)", "starvation", hint="starve", tags=["word_form"], source="unit51-26-50#3", segment=s2),
        I("u51-204", "zh2en", "这部电影将由他主演", "The film will star him", alts=["star in a film"], tags=["zh2en"], source="unit51-26-50#4", segment=s2),
        I("u51-205a", "phrase_cluster", "经受考验", "stand the test", related="u51-stand", tags=["phrase"], source="unit51-26-50#5a", segment=s2),
        I("u51-205b", "phrase_cluster", "支持；袖手旁观", "stand by", related="u51-stand", tags=["phrase"], source="unit51-26-50#5b", segment=s2),
        I("u51-205c", "phrase_cluster", "在……衬托下醒目；突出", "stand out against", related="u51-stand", tags=["phrase"], source="unit51-26-50#5c", segment=s2),
        I("u51-205d", "phrase_cluster", "作为……竞选/担任", "stand as", related="u51-stand", tags=["phrase"], source="unit51-26-50#5d", segment=s2),
        I("u51-206", "zh2en", "在护照上盖戳", "stamp the passport", alts=["stamp on the passport"], tags=["zh2en"], source="unit51-26-50#6", segment=s2),
        I("u51-207", "zh2en", "气得跺脚", "stamp one's feet in anger", tags=["zh2en"], source="unit51-26-50#7", segment=s2),
        I("u51-208", "zh2en", "一段楼梯", "a flight of stairs", tags=["zh2en"], source="unit51-26-50#8", segment=s2),
        I("u51-209a", "phrase_cluster", "为……创造条件", "set the stage for", related="u51-stage", tags=["phrase"], source="unit51-26-50#9a", segment=s2),
        I("u51-209b", "phrase_cluster", "举办仪式", "stage a ceremony", related="u51-stage", tags=["phrase"], source="unit51-26-50#9b", segment=s2),
        I("u51-210", "word_form", "stable（名词：马厩 / 稳定性相关按语境）", "stable / stability", alts=["stable", "stability"], blanks=[blank("stable / stability", alts=["stable", "stability"])], hint="stable", tags=["word_form"], source="unit51-26-50#10", segment=s2),
        I("u51-211a", "phrase_cluster", "涌现；突然出现", "spring up", related="u51-spring", tags=["phrase"], source="unit51-26-50#11a", segment=s2),
        I("u51-211b", "phrase_cluster", "温泉", "hot spring", related="u51-spring", tags=["phrase"], source="unit51-26-50#11b", segment=s2),
        I("u51-212", "zh2en", "一跃而起", "spring to one's feet", tags=["zh2en"], source="unit51-26-50#12", segment=s2),
        I("u51-213a", "phrase_cluster", "展开地图", "spread out the map", related="u51-spread", tags=["phrase"], source="unit51-26-50#13a", segment=s2),
        I("u51-213b", "phrase_cluster", "把药涂在伤口上", "spread medicine on the wound", related="u51-spread", tags=["phrase"], source="unit51-26-50#13b", segment=s2),
        I("u51-214a", "phrase_cluster", "发现某人正在做", "spot sb doing", related="u51-spot", tags=["phrase"], source="unit51-26-50#14a", segment=s2),
        I("u51-214b", "phrase_cluster", "恰到好处；正合需要", "hit the spot", related="u51-spot", tags=["phrase"], source="unit51-26-50#14b", segment=s2),
        I("u51-215", "word_form", "spoon（形容词）", "spoonful", alts=["spoon-shaped"], blanks=[blank("spoonful", alts=["spoon-shaped"])], hint="spoon", tags=["word_form"], source="unit51-26-50#15", segment=s2),
        I("u51-216", "zh2en", "情绪高昂", "in high spirits", alts=["in good spirits"], tags=["zh2en"], source="unit51-26-50#16", segment=s2),
        I("u51-217", "zh2en", "斗志", "fighting spirit", tags=["zh2en"], source="unit51-26-50#17", segment=s2),
        I("u51-218", "word_form", "spirit（形容词）", "spiritual", hint="spirit", tags=["word_form"], source="unit51-26-50#18", segment=s2),
        I("u51-219a", "phrase_cluster", "招致灾难", "spell a disaster", related="u51-spell", tags=["phrase"], source="unit51-26-50#19a", segment=s2),
        I("u51-219b", "phrase_cluster", "拼写你的名字", "spell your name", related="u51-spell", tags=["phrase"], source="unit51-26-50#19b", segment=s2),
        I("u51-220", "cloze", "____ a speed of / pick up speed", "at", tags=["collocation"], source="unit51-26-50#20", segment=s2),
    ]
    return {
        "unitId": "51",
        "name": "Unit 51 (somewhat—specialize)",
        "order": 51,
        "rangeFrom": "somewhat",
        "rangeTo": "specialize",
        "wordsPerUnit": 50,
        "items": items,
    }


def main() -> None:
    # Fix names from catalog if possible
    import json
    from pathlib import Path

    cat = json.loads(Path(r"D:\3500Words\content\catalog\units.json").read_text(encoding="utf-8"))
    by_id = {str(u["unitId"]): u for u in cat["units"]}
    for builder in (unit49, unit50, unit51):
        bank = builder()
        meta = by_id.get(bank["unitId"], {})
        if meta:
            bank["name"] = meta.get("displayName") or bank["name"]
            bank["rangeFrom"] = meta.get("rangeFrom", bank.get("rangeFrom"))
            bank["rangeTo"] = meta.get("rangeTo", bank.get("rangeTo"))
        write_unit(bank)


if __name__ == "__main__":
    main()
