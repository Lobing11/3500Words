#!/usr/bin/env python3
"""Promote Units 45, 47, 48 into curated gold."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from promote_lib import blank, item, write_unit  # noqa: E402


def unit45() -> dict:
    u = "45"
    s1, s2 = "1-25", "26-50"
    I = lambda *a, **k: item(u, *a, **k)
    items = [
        # ---- 1-25 ----
        I("u45-101", "zh2en", "拭目以待", "wait and see", alts=["wait to see"], tags=["zh2en"], source="unit45-1-25#1", segment=s1),
        I("u45-102", "zh2en", "依然坐着；继续坐着", "remain seated", alts=["stay seated", "remain sitting"], tags=["zh2en"], source="unit45-1-25#2", segment=s1),
        I("u45-103", "zh2en", "你可以放心他会成功", "You may rely on it that he will succeed", alts=["rely on it that", "rely on sb to succeed"], tags=["zh2en"], source="unit45-1-25#3", segment=s1),
        I("u45-104", "zh2en", "缓解焦虑", "relieve anxiety", alts=["ease anxiety", "relieve one's anxiety"], tags=["zh2en"], source="unit45-1-25#4", segment=s1),
        I("u45-105", "zh2en", "宽慰地叹了口气", "sigh with relief", alts=["breathe a sigh of relief", "heave a sigh of relief"], tags=["zh2en"], source="unit45-1-25#5", segment=s1),
        I("u45-106", "zh2en", "靠救济维生", "survive on relief", alts=["live on relief"], tags=["zh2en"], source="unit45-1-25#6", segment=s1),
        I("u45-107", "zh2en", "与……相关", "be related to", alts=["relate to", "be relevant to"], tags=["zh2en"], source="unit45-1-25#7", segment=s1),
        I("u45-108", "word_form", "buy the book with the ____(remain) money", "remaining", hint="remain", tags=["word_form"], source="unit45-1-25#8", segment=s1),
        I("u45-109a", "zh2en", "接力赛", "a relay race", alts=["relay race"], tags=["zh2en"], source="unit45-1-25#9a", segment=s1),
        I("u45-109b", "zh2en", "把他的请求转告给我", "She relayed his request to me", alts=["relay sth to sb"], tags=["zh2en"], source="unit45-1-25#9b", segment=s1),
        I("u45-110a", "phrase_cluster", "发行新专辑", "release a new album", related="u45-release", tags=["phrase"], source="unit45-1-25#10a", segment=s1),
        I("u45-110b", "phrase_cluster", "排放二氧化碳", "release CO2", alts=["release carbon dioxide"], related="u45-release", tags=["phrase"], source="unit45-1-25#10b", segment=s1),
        I("u45-110c", "phrase_cluster", "发布报告", "release the report", alts=["release a report"], related="u45-release", tags=["phrase"], source="unit45-1-25#10c", segment=s1),
        I("u45-110d", "phrase_cluster", "释放人质", "release the hostage", alts=["release hostages"], related="u45-release", tags=["phrase"], source="unit45-1-25#10d", segment=s1),
        I("u45-111a", "phrase_cluster", "把……称作", "refer to ... as", alts=["refer to sb as", "refer to sth as"], related="u45-refer", tags=["phrase"], source="unit45-1-25#11a", segment=s1),
        I("u45-111b", "phrase_cluster", "把病人转诊给另一位专家", "refer the patient to another specialist", alts=["refer sb to"], related="u45-refer", tags=["phrase"], source="unit45-1-25#11b", segment=s1),
        I("u45-111c", "phrase_cluster", "参考笔记", "refer to the notes", alts=["refer to one's notes"], related="u45-refer", tags=["phrase"], source="unit45-1-25#11c", segment=s1),
        I("u45-112a", "zh2en", "没提及", "make no reference to", alts=["without reference to", "no reference to"], tags=["zh2en"], source="unit45-1-25#12a", segment=s1),
        I("u45-112b", "zh2en", "关于；就……而言（in reference to）", "in reference to", alts=["with reference to"], tags=["zh2en"], source="unit45-1-25#12b", segment=s1),
        I("u45-113", "zh2en", "反思；仔细思考", "reflect on", alts=["reflect upon", "think over"], tags=["zh2en"], source="unit45-1-25#13", segment=s1),
        I("u45-114", "zh2en", "小偷决定改过自新", "The thief decided to reform", alts=["reform", "decide to reform"], tags=["zh2en"], source="unit45-1-25#14", segment=s1),
        I("u45-115a", "phrase_cluster", "刷新文档", "refresh the document", related="u45-refresh", tags=["phrase"], source="unit45-1-25#15a", segment=s1),
        I("u45-115b", "phrase_cluster", "唤起我对某事的记忆", "refresh my memory of sth", alts=["refresh one's memory"], related="u45-refresh", tags=["phrase"], source="unit45-1-25#15b", segment=s1),
        I("u45-116", "zh2en", "神清气爽", "feel refreshed", alts=["be refreshed", "refreshing"], tags=["zh2en"], source="unit45-1-25#16", segment=s1),
        I("u45-117", "word_form", "拒绝（名词）", "refusal", hint="refuse", tags=["word_form"], source="unit45-1-25#17", segment=s1),
        I("u45-118", "word_form", "I have something to say ____(regard) the matter.（= 短语）", "regarding", alts=["with regard to", "in regard to", "as regards"], blanks=[blank("regarding", alts=["with regard to", "in regard to", "as regards"])], hint="regard", tags=["word_form"], source="unit45-1-25#18", segment=s1),
        I("u45-119", "cloze", "be equal to everyone ____ their backgrounds（不管，不顾）", "regardless of", alts=["irrespective of"], tags=["collocation"], source="unit45-1-25#19", segment=s1),
        I("u45-120", "zh2en", "注册网上课程", "register for an online course", alts=["sign up for an online course", "enroll in an online course"], tags=["zh2en"], source="unit45-1-25#20", segment=s1),
        I("u45-121", "word_form", "register（名词）", "registration", hint="register", tags=["word_form"], source="unit45-1-25#21", segment=s1),
        I("u45-122", "zh2en", "挂号信", "a registered letter", alts=["registered mail"], tags=["zh2en"], source="unit45-1-25#22", segment=s1),
        I("u45-123", "zh2en", "常客；定期访客", "a regular visitor", alts=["regular visitor"], tags=["zh2en"], source="unit45-1-25#23", segment=s1),
        I("u45-124", "zh2en", "不规律的", "irregular", alts=["not regular"], tags=["zh2en"], source="unit45-1-25#24", segment=s1),
        I("u45-125", "zh2en", "定期（短语）", "on a regular basis", alts=["regularly", "at regular intervals"], tags=["zh2en"], source="unit45-1-25#25", segment=s1),
        I("u45-126", "zh2en", "拒绝申请者", "reject the applicant", alts=["reject an applicant"], tags=["zh2en"], source="unit45-1-25#26", segment=s1),
        I("u45-127", "zh2en", "向警察讲述事故经过", "relate the accident to the policeman", alts=["relate sth to sb"], tags=["zh2en"], source="unit45-1-25#27", segment=s1),
        I("u45-128", "zh2en", "与……有关", "be related to", alts=["have relation to", "be connected with"], tags=["zh2en"], source="unit45-1-25#28", segment=s1),
        I("u45-129", "zh2en", "许多青少年能与小说主角产生共鸣", "Many teenagers can relate to the main character in the novel", alts=["relate to"], tags=["zh2en"], source="unit45-1-25#29", segment=s1),
        I("u45-130a", "zh2en", "就……而言；与……相关（in relation to）", "in relation to", tags=["zh2en"], source="unit45-1-25#30a", segment=s1),
        I("u45-130b", "zh2en", "相对而言；相对来说", "relatively speaking", tags=["zh2en"], source="unit45-1-25#31", segment=s1),
        I("u45-131", "word_form", "放松（名词）", "relaxation", hint="relax", tags=["word_form"], source="unit45-1-25#32", segment=s1),
        # ---- 26-50 ----
        I("u45-201", "word_form", "She ____(评论) that his work was ____(非凡的).", "remarked|remarkable", blanks=[blank("remarked", 0, ["commented"]), blank("remarkable", 1)], hint="remark / remarkable", tags=["word_form"], source="unit45-26-50#1", segment=s2),
        I("u45-202", "zh2en", "被他刻薄的话弄得心烦", "be upset by his mean remarks", alts=["upset by mean remarks"], tags=["zh2en"], source="unit45-26-50#2", segment=s2),
        I("u45-203a", "pattern", "记得做过某事", "remember doing", alts=["remember having done"], tags=["pattern"], source="unit45-26-50#3a", segment=s2),
        I("u45-203b", "pattern", "记得要去做某事", "remember to do", tags=["pattern"], source="unit45-26-50#3b", segment=s2),
        I("u45-204", "word_form", "remind（名词）", "reminder", hint="remind", tags=["word_form"], source="unit45-26-50#4", segment=s2),
        I("u45-205a", "phrase_cluster", "遥控器", "a remote control", alts=["remote control"], related="u45-remote", tags=["phrase"], source="unit45-26-50#5a", segment=s2),
        I("u45-205b", "phrase_cluster", "远亲", "a remote relative", alts=["distant relative"], related="u45-remote", tags=["phrase"], source="unit45-26-50#5b", segment=s2),
        I("u45-205c", "phrase_cluster", "远程教育", "remote education", alts=["distance education"], related="u45-remote", tags=["phrase"], source="unit45-26-50#5c", segment=s2),
        I("u45-205d", "zh2en", "我们获胜的可能性微乎其微", "There is only a remote chance that we will win", alts=["a remote chance"], tags=["zh2en"], source="unit45-26-50#5d", segment=s2),
        I("u45-206", "zh2en", "摘掉眼镜", "remove glasses", alts=["take off one's glasses"], tags=["zh2en"], source="unit45-26-50#6", segment=s2),
        I("u45-207", "zh2en", "撤他的职", "remove him from office", alts=["remove sb from office", "dismiss him from his post"], tags=["zh2en"], source="unit45-26-50#7", segment=s2),
        I("u45-208", "zh2en", "消除异议", "remove objections", alts=["remove the objections", "clear up objections"], tags=["zh2en"], source="unit45-26-50#8", segment=s2),
        I("u45-209", "word_form", "remove（名词）", "removal", hint="remove", tags=["word_form"], source="unit45-26-50#9", segment=s2),
        I("u45-210", "cloze", "The house is ____ rent.", "for", tags=["collocation"], source="unit45-26-50#10", segment=s2),
        I("u45-211", "cloze", "____ repair（在修理中）", "under", tags=["collocation"], source="unit45-26-50#11", segment=s2),
        I("u45-212a", "zh2en", "无法修理；坏到不能修", "beyond repair", tags=["zh2en"], source="unit45-26-50#12a", segment=s2),
        I("u45-212b", "word_form", "____(repeat) practice helps improve your English.", "Repeated", alts=["repeated"], blanks=[blank("Repeated", alts=["repeated"])], hint="repeat", tags=["word_form"], source="unit45-26-50#12b", segment=s2),
        I("u45-213a", "zh2en", "读完后把书放回书架", "Replace the books on the shelf after reading", alts=["replace the books on the shelf"], tags=["zh2en"], source="unit45-26-50#14a", segment=s2),
        I("u45-213b", "cloze", "We replaced the old equipment ____ new ones.", "with", alts=["by"], tags=["collocation"], source="unit45-26-50#14b", segment=s2),
        I("u45-213c", "word_form", "He will act as a ____(replace) for our manager.", "replacement", hint="replace", tags=["word_form"], source="unit45-26-50#14c", segment=s2),
        I("u45-214a", "word_form", "Several residents reported ____(hear) loud noises last night.", "hearing", hint="hear", tags=["word_form", "pattern"], source="unit45-26-50#15a", segment=s2),
        I("u45-214b", "word_form", "He was reported ____(donate) a large fortune to the charity.", "to have donated", alts=["to donate"], blanks=[blank("to have donated", alts=["to donate"])], hint="donate", tags=["word_form", "pattern"], source="unit45-26-50#15b", segment=s2),
        I("u45-215a", "zh2en", "媒体把他描绘成英雄", "The media represented him as a hero", alts=["represent sb as"], tags=["zh2en"], source="unit45-26-50#16a", segment=s2),
        I("u45-215b", "word_form", "act as a sales ____(represent)", "representative", hint="represent", tags=["word_form"], source="unit45-26-50#16b", segment=s2),
        I("u45-216", "zh2en", "名副其实", "deserve the reputation", alts=["live up to one's reputation", "worthy of the name", "deserve one's reputation"], tags=["zh2en"], source="unit45-26-50#17", segment=s2),
        I("u45-217", "zh2en", "按照某人的要求", "at one's request", alts=["at sb's request", "by request"], tags=["zh2en"], source="unit45-26-50#18", segment=s2),
        I("u45-218", "cloze", "make a request ____ sth（请求）", "for", tags=["collocation"], source="unit45-26-50#19", segment=s2),
        I("u45-219", "word_form", "He made a request that we ____(arrive) on time.", "arrive", alts=["should arrive"], blanks=[blank("arrive", alts=["should arrive"])], hint="arrive / request that 虚拟", tags=["word_form", "pattern"], source="unit45-26-50#20", segment=s2),
        I("u45-220", "word_form", "The house requires ____(mend).", "mending", alts=["to be mended"], blanks=[blank("mending", alts=["to be mended"])], hint="mend", tags=["word_form", "pattern"], source="unit45-26-50#21", segment=s2),
        I("u45-221", "zh2en", "来营救某人", "come to sb's rescue", alts=["come to one's rescue", "rescue sb"], tags=["zh2en"], source="unit45-26-50#22", segment=s2),
        I("u45-222", "cloze", "do research ____ eco-system", "on", alts=["into"], tags=["collocation"], source="unit45-26-50#23", segment=s2),
        I("u45-223", "zh2en", "保留做……的权利", "reserve the right to do", alts=["reserve one's right to do"], tags=["zh2en"], source="unit45-26-50#24", segment=s2),
        I("u45-224", "zh2en", "野生动物保护区", "wildlife reserves", alts=["wildlife reserve", "nature reserve"], tags=["zh2en"], source="unit45-26-50#25", segment=s2),
        I("u45-225", "zh2en", "把位子留给残疾人", "reserve seats for the disabled", alts=["reserve a seat for the disabled"], tags=["zh2en"], source="unit45-26-50#26", segment=s2),
        I("u45-226", "zh2en", "备用资金；储备金", "funds in reserve", alts=["money in reserve"], tags=["zh2en"], source="unit45-26-50#27", segment=s2),
        I("u45-227", "cloze", "make a ____ ____ a hotel（预定）", "reservation|at", blanks=[blank("reservation", 0), blank("at", 1, ["in", "with"])], tags=["collocation"], source="unit45-26-50#28", segment=s2),
        I("u45-228", "zh2en", "顺从于；听任", "resign oneself to", alts=["be resigned to", "resign to"], tags=["zh2en"], source="unit45-26-50#29", segment=s2),
        I("u45-229", "zh2en", "忍不住要笑", "can't resist laughing", alts=["cannot resist laughing", "can't help laughing"], tags=["zh2en"], source="unit45-26-50#30", segment=s2),
        I("u45-230", "zh2en", "耐热材料", "heat-resistant materials", alts=["heat resistant materials"], tags=["zh2en"], source="unit45-26-50#31a", segment=s2),
        I("u45-231", "zh2en", "对……有抵抗力", "be resistant to", alts=["have resistance to"], tags=["zh2en"], source="unit45-26-50#31b", segment=s2),
        I("u45-232", "zh2en", "风阻；空气阻力", "wind resistance", tags=["zh2en"], source="unit45-26-50#32", segment=s2),
    ]
    return {
        "unitId": "45",
        "name": "Unit 45 (refer—resistance)",
        "order": 45,
        "rangeFrom": "refer",
        "rangeTo": "resistance",
        "wordsPerUnit": 50,
        "items": items,
    }


def unit47() -> dict:
    u = "47"
    s1, s2 = "1-25", "26-50"
    I = lambda *a, **k: item(u, *a, **k)
    items = [
        I("u47-101", "zh2en", "橡皮 / 尺子（区分）", "rubber / ruler", alts=["rubber", "ruler"], tags=["zh2en"], source="unit47-1-25#2", segment=s1),
        I("u47-102", "zh2en", "沦为废墟", "lie in ruins", alts=["be in ruins", "fall into ruin", "be reduced to ruins"], tags=["zh2en"], source="unit47-1-25#3", segment=s1),
        I("u47-103", "zh2en", "遵守规则", "observe a rule", alts=["obey a rule", "follow a rule"], tags=["zh2en"], source="unit47-1-25#4", segment=s1),
        I("u47-104", "zh2en", "排除可能性", "rule out the possibility", alts=["rule out"], tags=["zh2en"], source="unit47-1-25#5", segment=s1),
        I("u47-105", "zh2en", "偶遇", "run into", alts=["come across", "run across"], tags=["zh2en"], source="unit47-1-25#6", segment=s1),
        I("u47-106", "zh2en", "追赶", "run after", alts=["chase"], tags=["zh2en"], source="unit47-1-25#7", segment=s1),
        I("u47-107", "zh2en", "用光", "run out of", alts=["run out"], tags=["zh2en"], source="unit47-1-25#8", segment=s1),
        I("u47-108", "zh2en", "把某人紧急送往医院", "rush sb to hospital", alts=["rush someone to the hospital", "rush sb to the hospital"], tags=["zh2en"], source="unit47-1-25#9", segment=s1),
        I("u47-109", "zh2en", "圣诞购物高峰", "the Christmas rush", alts=["Christmas rush"], tags=["zh2en"], source="unit47-1-25#10", segment=s1),
        I("u47-110", "zh2en", "一阵怒火", "a rush of anger", alts=["a rush of rage"], tags=["zh2en"], source="unit47-1-25#11", segment=s1),
        I("u47-111", "zh2en", "启航", "set sail", alts=["sail"], tags=["zh2en"], source="unit47-1-25#12", segment=s1),
        I("u47-112", "zh2en", "在销售；降价出售", "on sale", alts=["for sale"], tags=["zh2en"], source="unit47-1-25#13", segment=s1),
        I("u47-113", "zh2en", "品尝当地美食", "sample local food", alts=["taste local food", "sample the local cuisine"], tags=["zh2en"], source="unit47-1-25#14", segment=s1),
        # 26-50
        I("u47-201", "zh2en", "庇护某人免受……；掩护", "screen sb from", alts=["screen someone from"], tags=["zh2en"], source="unit47-26-50#1", segment=s2),
        I("u47-202", "zh2en", "筛查疾病", "screen for disease", alts=["screen for diseases"], tags=["zh2en"], source="unit47-26-50#2", segment=s2),
        I("u47-203", "zh2en", "发出尖叫声", "let out a scream", alts=["scream", "give a scream"], tags=["zh2en"], source="unit47-26-50#3", segment=s2),
        I("u47-204", "zh2en", "踢进一球", "score a goal", alts=["score"], tags=["zh2en"], source="unit47-26-50#4", segment=s2),
        I("u47-205", "zh2en", "剪刀", "scissors", alts=["a pair of scissors"], tags=["zh2en"], source="unit47-26-50#5", segment=s2),
        I("u47-206", "zh2en", "文科和理科", "arts and science", alts=["arts and sciences"], tags=["zh2en"], source="unit47-26-50#6", segment=s2),
        I("u47-207", "zh2en", "获得奖学金", "win a scholarship", alts=["get a scholarship", "be awarded a scholarship"], tags=["zh2en"], source="unit47-26-50#7", segment=s2),
        I("u47-208", "zh2en", "会议定于下周举行。", "The meeting is scheduled for next week", alts=["The meeting is scheduled to be held next week"], tags=["zh2en"], source="unit47-26-50#8", segment=s2),
        I("u47-209", "zh2en", "如期；按时", "on schedule", alts=["ahead of schedule", "behind schedule"], tags=["zh2en"], source="unit47-26-50#9", segment=s2),
        I("u47-210", "word_form", "a ____(scene) spot", "scenic", hint="scene", tags=["word_form"], source="unit47-26-50#10", segment=s2),
        I("u47-211", "zh2en", "突然出现；登场", "burst on the scene", alts=["burst onto the scene", "come on the scene"], tags=["zh2en"], source="unit47-26-50#11", segment=s2),
        I("u47-212", "zh2en", "吓走", "scare away", alts=["scare off", "frighten away"], tags=["zh2en"], source="unit47-26-50#12", segment=s2),
        I("u47-213", "zh2en", "吓得某人做某事", "scare sb into doing", alts=["scare someone into doing sth", "frighten sb into doing"], tags=["zh2en"], source="unit47-26-50#13", segment=s2),
        I("u47-214", "zh2en", "常言道", "as the saying goes", alts=["as a saying goes"], tags=["zh2en"], source="unit47-26-50#14", segment=s2),
        I("u47-215", "zh2en", "发射卫星", "launch a satellite", alts=["send up a satellite"], tags=["zh2en"], source="unit47-26-50#15", segment=s2),
        I("u47-216", "zh2en", "一个满意的微笑", "a satisfied smile", alts=["a satisfying smile"], tags=["zh2en"], source="unit47-26-50#16", segment=s2),
        I("u47-217", "zh2en", "满足感", "a sense of satisfaction", alts=["satisfaction"], tags=["zh2en"], source="unit47-26-50#17", segment=s2),
        I("u47-218", "zh2en", "省得我跑一趟", "save me a trip", alts=["save me the trip", "save sb a journey"], tags=["zh2en"], source="unit47-26-50#18", segment=s2),
        I("u47-219", "cloze", "open a ____ account（储蓄账户）", "savings", tags=["collocation"], source="unit47-26-50#19", segment=s2),
        I("u47-220", "zh2en", "也就是说", "that is to say", alts=["namely", "in other words"], tags=["zh2en"], source="unit47-26-50#20", segment=s2),
        I("u47-221", "zh2en", "不言而喻；不用说", "It goes without saying that", alts=["needless to say", "it goes without saying"], tags=["zh2en"], source="unit47-26-50#21", segment=s2),
    ]
    return {
        "unitId": "47",
        "name": "Unit 47 (row—sculpture)",
        "order": 47,
        "rangeFrom": "row",
        "rangeTo": "sculpture",
        "wordsPerUnit": 50,
        "items": items,
    }


def unit48() -> dict:
    u = "48"
    s1, s2 = "1-25", "26-50"
    I = lambda *a, **k: item(u, *a, **k)
    items = [
        I("u48-101", "word_form", "____(seat) by the window, Mr. Henderson stared at the snow.", "Seated", alts=["seated"], blanks=[blank("Seated", alts=["seated"])], hint="seat", tags=["word_form"], source="unit48-1-25#4", segment=s1),
        I("u48-102a", "phrase_cluster", "仅次于", "second only to", related="u48-second", tags=["phrase"], source="unit48-1-25#5a", segment=s1),
        I("u48-102b", "phrase_cluster", "首屈一指；不亚于任何人", "second to none", related="u48-second", tags=["phrase"], source="unit48-1-25#5b", segment=s1),
        I("u48-102c", "phrase_cluster", "第二次机会", "a second chance", related="u48-second", tags=["phrase"], source="unit48-1-25#5c", segment=s1),
        I("u48-103", "zh2en", "主要 / 次要因素", "a primary/secondary factor", alts=["primary factor", "secondary factor"], tags=["zh2en"], source="unit48-1-25#6", segment=s1),
        I("u48-104a", "phrase_cluster", "安全的藏身之处", "a secure place to hide", related="u48-secure", tags=["phrase"], source="unit48-1-25#7a", segment=s1),
        I("u48-104b", "phrase_cluster", "对未来感到安心", "feel secure about one's future", related="u48-secure", tags=["phrase"], source="unit48-1-25#7b", segment=s1),
        I("u48-104c", "phrase_cluster", "使老人免受寒冷", "secure the old man from the cold", related="u48-secure", tags=["phrase"], source="unit48-1-25#7c", segment=s1),
        I("u48-104d", "phrase_cluster", "获得一个职位", "secure a position", alts=["secure a positon"], related="u48-secure", tags=["phrase"], source="unit48-1-25#7d", segment=s1),
        I("u48-104e", "phrase_cluster", "离开前把门关牢", "Secure the door before leaving", alts=["secure the door"], related="u48-secure", tags=["phrase"], source="unit48-1-25#7e", segment=s1),
        I("u48-105", "zh2en", "处理紧急情况；照料", "see to the emergency", alts=["see to", "attend to the emergency"], tags=["zh2en"], source="unit48-1-25#8", segment=s1),
        I("u48-106", "word_form", "Last year ____(见证) the development of the city.", "witnessed", hint="witness", tags=["word_form"], source="unit48-1-25#9", segment=s1),
        I("u48-107", "zh2en", "我设法安抚老人。（seek）", "I sought to comfort the old man", alts=["seek to comfort the old man", "I tried to soothe the old man"], tags=["zh2en"], source="unit48-1-25#10", segment=s1),
        I("u48-108", "zh2en", "似乎有", "there seems to be", alts=["seem to have", "there seem to be"], tags=["zh2en"], source="unit48-1-25#11", segment=s1),
        I("u48-109", "cloze", "The kind of books ____（畅销）", "sells well", alts=["sell well", "are best-sellers"], blanks=[blank("sells well", alts=["sell well", "are best-sellers"])], tags=["collocation"], source="unit48-1-25#12", segment=s1),
        I("u48-110", "cloze", "send ____ a doctor / send ____ a rocket", "for|up", blanks=[blank("for", 0), blank("up", 1)], tags=["collocation"], source="unit48-1-25#13", segment=s1),
        I("u48-111", "cloze", "be senior/junior/superior/inferior ____", "to", tags=["collocation"], source="unit48-1-25#14", segment=s1),
        I("u48-112", "zh2en", "高三学生", "senior students", alts=["Senior Three students", "students in Senior 3"], tags=["zh2en"], source="unit48-1-25#15", segment=s1),
        I("u48-113", "zh2en", "老年人", "senior citizens", alts=["the elderly"], tags=["zh2en"], source="unit48-1-25#16", segment=s1),
        I("u48-114a", "phrase_cluster", "恢复理智；醒悟过来", "come to one's senses", related="u48-sense", tags=["phrase"], source="unit48-1-25#17a", segment=s1),
        I("u48-114b", "phrase_cluster", "做某事没意义", "There is no sense/point doing", alts=["there is no sense in doing", "there is no point doing"], related="u48-sense", tags=["phrase"], source="unit48-1-25#17b", segment=s1),
        I("u48-114c", "phrase_cluster", "触觉", "the sense of touch", related="u48-sense", tags=["phrase"], source="unit48-1-25#17c", segment=s1),
        I("u48-115", "zh2en", "对……体贴、敏感", "be sensitive to", alts=["be considerate of"], tags=["zh2en"], source="unit48-1-25#18", segment=s1),
        I("u48-116", "zh2en", "被判处死刑", "be sentenced to death", tags=["zh2en"], source="unit48-1-25#19", segment=s1),
        # 26-50
        I("u48-201", "zh2en", "把……和……分开", "separate ... from", alts=["separate A from B"], tags=["zh2en"], source="unit48-26-50#1", segment=s2),
        I("u48-202", "word_form", "分开（名词）", "separation", hint="separate", tags=["word_form"], source="unit48-26-50#2", segment=s2),
        I("u48-203", "zh2en", "认真对待……", "take ... seriously", alts=["take sth seriously"], tags=["zh2en"], source="unit48-26-50#3", segment=s2),
        I("u48-204", "zh2en", "当床用", "serve as a bed", alts=["serve as"], tags=["zh2en"], source="unit48-26-50#4", segment=s2),
        I("u48-205", "zh2en", "服兵役", "serve in the army", alts=["do military service", "serve the army"], tags=["zh2en"], source="unit48-26-50#5", segment=s2),
        I("u48-206", "zh2en", "供应早餐", "serve breakfast", alts=["serve breakfast to"], tags=["zh2en"], source="unit48-26-50#6", segment=s2),
        I("u48-207", "zh2en", "我的车随时为你效劳", "My car is at your service", alts=["at your service"], tags=["zh2en"], source="unit48-26-50#7", segment=s2),
        I("u48-208a", "zh2en", "把生锈的刀磨锋利", "sharpen the rusting knife", alts=["sharpen a knife"], tags=["zh2en"], source="unit48-26-50#8a", segment=s2),
        I("u48-208b", "zh2en", "提高写作技巧", "sharpen writing skills", alts=["sharpen one's writing skills"], tags=["zh2en"], source="unit48-26-50#8b", segment=s2),
        I("u48-209a", "phrase_cluster", "急转弯", "a sharp turn", related="u48-sharp", tags=["phrase"], source="unit48-26-50#9a", segment=s2),
        I("u48-209b", "phrase_cluster", "急剧增加", "a sharp increase", alts=["sharp increse"], related="u48-sharp", tags=["phrase"], source="unit48-26-50#9b", segment=s2),
        I("u48-209c", "phrase_cluster", "剧痛", "a sharp pain", related="u48-sharp", tags=["phrase"], source="unit48-26-50#9c", segment=s2),
        I("u48-209d", "phrase_cluster", "敏锐的眼睛", "sharp eyes", related="u48-sharp", tags=["phrase"], source="unit48-26-50#9d", segment=s2),
        I("u48-210", "zh2en", "分担负担", "share the burden", alts=["share burdens"], tags=["zh2en"], source="unit48-26-50#10", segment=s2),
        I("u48-211", "zh2en", "共同的价值观", "shared values", alts=["common values"], tags=["zh2en"], source="unit48-26-50#11", segment=s2),
        I("u48-212", "zh2en", "人人都必须做好自己那份工作", "Everyone must do their share of the work", alts=["do one's share of the work"], tags=["zh2en"], source="unit48-26-50#12", segment=s2),
        I("u48-213", "zh2en", "强身健体", "keep fit", alts=["build up one's body", "strengthen the body"], tags=["zh2en"], source="unit48-26-50#13", segment=s2),
        I("u48-214", "zh2en", "以……的形状", "in the shape of", alts=["in shape of"], tags=["zh2en"], source="unit48-26-50#14", segment=s2),
        I("u48-215", "zh2en", "真遗憾", "What a shame", alts=["What a pity"], tags=["zh2en"], source="unit48-26-50#15", segment=s2),
        I("u48-216", "zh2en", "以……为背景", "be set in", alts=["set in"], tags=["zh2en"], source="unit48-26-50#16", segment=s2),
        I("u48-217", "zh2en", "着手做", "set about doing", alts=["set out to do", "set about"], tags=["zh2en"], source="unit48-26-50#17", segment=s2),
        I("u48-218a", "phrase_cluster", "引发辩论", "set off a debate", related="u48-set", tags=["phrase"], source="unit48-26-50#18a", segment=s2),
        I("u48-218b", "phrase_cluster", "燃放烟花", "set off fireworks", related="u48-set", tags=["phrase"], source="unit48-26-50#18b", segment=s2),
        I("u48-219", "zh2en", "摆餐具", "set the table", tags=["zh2en"], source="unit48-26-50#19", segment=s2),
        I("u48-220", "zh2en", "理想的散步环境", "an ideal setting for a walk", alts=["ideal setting"], tags=["zh2en"], source="unit48-26-50#20", segment=s2),
        I("u48-221", "zh2en", "勉强接受这个价格", "settle for the price", alts=["settle for"], tags=["zh2en"], source="unit48-26-50#21", segment=s2),
        I("u48-222", "zh2en", "他心神不宁", "He was unsettled", alts=["feel unsettled"], tags=["zh2en"], source="unit48-26-50#22", segment=s2),
        I("u48-223", "zh2en", "灰尘落在桌上", "Dust settled on the table", alts=["settle on"], tags=["zh2en"], source="unit48-26-50#23", segment=s2),
        I("u48-224a", "zh2en", "永久定居点", "a permanent settlement", tags=["zh2en"], source="unit48-26-50#24a", segment=s2),
        I("u48-224b", "zh2en", "达成协议", "reach a settlement", alts=["reach an agreement"], tags=["zh2en"], source="unit48-26-50#24b", segment=s2),
        I("u48-225", "zh2en", "在阴凉处", "in the shade", alts=["in the shadow"], tags=["zh2en"], source="unit48-26-50#25", segment=s2),
        I("u48-226", "zh2en", "给……蒙上阴影", "cast a shadow on", alts=["cast a shadow over", "overshadow"], tags=["zh2en"], source="unit48-26-50#26", segment=s2),
        I("u48-227", "zh2en", "吓得发抖", "shake with fear", alts=["tremble with fear"], tags=["zh2en"], source="unit48-26-50#27", segment=s2),
        I("u48-228", "zh2en", "摆脱恐惧", "shake off fear", alts=["shake off"], tags=["zh2en"], source="unit48-26-50#28", segment=s2),
        I("u48-229", "zh2en", "动摇某人对……的信心", "shake one's confidence in", alts=["shake sb's confidence in"], tags=["zh2en"], source="unit48-26-50#29", segment=s2),
        I("u48-230a", "zh2en", "浅溪", "a shallow stream", tags=["zh2en"], source="unit48-26-50#30a", segment=s2),
        I("u48-230b", "zh2en", "对某事一知半解", "a shallow knowledge of sth", alts=["shallow knowledge"], tags=["zh2en"], source="unit48-26-50#30b", segment=s2),
    ]
    return {
        "unitId": "48",
        "name": "Unit 48 (sea—sheep)",
        "order": 48,
        "rangeFrom": "sea",
        "rangeTo": "sheep",
        "wordsPerUnit": 50,
        "items": items,
    }


def main() -> None:
    for builder in (unit45, unit47, unit48):
        write_unit(builder())


if __name__ == "__main__":
    main()
