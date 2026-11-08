#!/usr/bin/env python3
"""Promote Units 55, 57, 58, 59 into curated gold."""

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


def unit55() -> dict:
    u = "55"
    s1, s2 = "1-25", "26-50"
    I = lambda *a, **k: item(u, *a, **k)
    items = [
        I("u55-101", "word_form", "theory（形容词）", "theoretical", hint="theory", tags=["word_form"], source="unit55-all#1", segment=s1),
        I("u55-102", "zh2en", "我无论怎么感谢你都不为过", "I can't thank you enough", alts=["I cannot thank you too much"], tags=["zh2en"], source="unit55-all#2", segment=s1),
        I("u55-103", "word_form", "thick（动词）", "thicken", hint="thick", tags=["word_form"], source="unit55-all#3", segment=s1),
        I("u55-104", "zh2en", "一方面", "for one thing", tags=["zh2en"], source="unit55-all#4", segment=s1),
        I("u55-105", "zh2en", "回想起", "think back to", alts=["think of", "recall"], tags=["zh2en"], source="unit55-all#5", segment=s1),
        I("u55-106", "zh2en", "陷入沉思", "be lost in thought", alts=["be deep in thought"], tags=["zh2en"], source="unit55-all#6", segment=s1),
        I("u55-107", "zh2en", "对……造成威胁", "pose a threat to", alts=["be a threat to", "threaten"], tags=["zh2en"], source="unit55-all#7", segment=s1),
        I("u55-108", "zh2en", "威胁要……", "threaten to do", alts=["threaten to"], tags=["zh2en"], source="unit55-all#8", segment=s1),
        I("u55-109", "zh2en", "一整夜、通宵", "all night / throughout the night", alts=["all night long", "overnight"], tags=["zh2en"], source="unit55-all#9", segment=s1),
        I("u55-110", "zh2en", "投身于", "throw oneself into", alts=["devote oneself to"], tags=["zh2en"], source="unit55-all#10", segment=s1),
        I("u55-111", "zh2en", "爆发出雷鸣般的掌声", "burst into thunderous applause", alts=["break into thunderous applause"], tags=["zh2en"], source="unit55-all#11", segment=s1),
        I("u55-112", "zh2en", "往返票", "a return ticket", alts=["a round-trip ticket"], tags=["zh2en"], source="unit55-all#12", segment=s1),
        I("u55-113", "zh2en", "把……绑到", "tie ... to", alts=["tie sth to"], tags=["zh2en"], source="unit55-all#13", segment=s1),
        I("u55-114", "zh2en", "暂时；眼下", "for the time being", tags=["zh2en"], source="unit55-all#14", segment=s1),
        I("u55-115", "zh2en", "厌倦", "be tired of", alts=["be sick of", "be fed up with"], tags=["zh2en"], source="unit55-all#15", segment=s1),
        I("u55-116", "zh2en", "没气的/爆了的轮胎", "a flat/burst tyre", alts=["a flat tire", "a burst tyre"], tags=["zh2en"], source="unit55-all#16", segment=s1),
        I("u55-117", "zh2en", "被授予一个头衔", "be awarded a title", alts=["be given a title", "be conferred a title"], tags=["zh2en"], source="unit55-all#17", segment=s1),
        I("u55-118", "zh2en", "tolerate（adj./n.）", "tolerant / tolerance", alts=["tolerant", "tolerance"], tags=["zh2en"], source="unit55-all#18", segment=s1),
        I("u55-119", "zh2en", "联合起来反对", "band together against", alts=["unite against"], tags=["zh2en"], source="unit55-all#19", segment=s2),
        I("u55-120a", "phrase_cluster", "话到嘴边；差一点说出", "on the tip of one's tongue", related="u55-tip", tags=["phrase"], source="unit55-all#20a", segment=s2),
        I("u55-120b", "phrase_cluster", "给服务员一笔丰厚小费", "give a generous tip to the waiter", related="u55-tip", tags=["phrase"], source="unit55-all#20b", segment=s2),
        I("u55-121", "zh2en", "接通经理电话", "get through to the manager", alts=["put through to the manager"], tags=["zh2en"], source="unit55-all#21", segment=s2),
        I("u55-122", "zh2en", "实施盗窃", "commit theft", alts=["commit a theft"], tags=["zh2en"], source="unit55-all#22", segment=s2),
        I("u55-123", "zh2en", "参加会议的客人不超过五人", "No more than 5 guests attended the meeting", alts=["no more than"], tags=["zh2en"], source="unit55-all#23", segment=s2),
    ]
    return {"unitId": "55", "name": "Unit 55", "order": 55, "wordsPerUnit": 50, "items": items}


def unit57() -> dict:
    u = "57"
    s1, s2 = "1-25", "26-50"
    I = lambda *a, **k: item(u, *a, **k)
    items = [
        I("u57-101", "cloze", "____ vacation", "on", tags=["collocation"], source="unit57-all#5", segment=s1),
        I("u57-102", "zh2en", "习惯于", "be used to", alts=["get used to", "be accustomed to"], tags=["zh2en"], source="unit57-all#6", segment=s1),
        I("u57-103", "cloze", "put sth ____ use", "to", tags=["collocation"], source="unit57-all#7", segment=s1),
        I("u57-104", "zh2en", "力劝某人做……", "urge sb to do", alts=["urge someone to do sth"], tags=["zh2en"], source="unit57-all#8", segment=s1),
        I("u57-105", "zh2en", "在进行中", "under way", alts=["underway", "in progress"], tags=["zh2en"], source="unit57-all#9", segment=s1),
        I("u57-106", "word_form", "He urged that we ____(go) at once.", "go", alts=["should go"], blanks=[blank("go", alts=["should go"])], hint="go / urge that 虚拟", tags=["word_form", "pattern"], source="unit57-all#10", segment=s1),
        I("u57-107", "zh2en", "对……心烦 / upset 的词形", "be upset about / upset/upsetting", alts=["be upset about", "upset", "upsetting"], tags=["zh2en"], source="unit57-all#11", segment=s1),
        I("u57-108a", "zh2en", "坏消息让她心烦", "The bad news upset her", tags=["zh2en"], source="unit57-all#12a", segment=s1),
        I("u57-108b", "zh2en", "他打翻了杯子", "He upset the cup", tags=["zh2en"], source="unit57-all#12b", segment=s1),
        I("u57-108c", "zh2en", "突如其来的雨打乱了我们的旅行安排", "The sudden rain upset our travel arrangement", tags=["zh2en"], source="unit57-all#12c", segment=s1),
        I("u57-109a", "phrase_cluster", "移交；上交", "turn over / turn in", alts=["turn over", "turn in", "hand in"], related="u57-turn", tags=["phrase"], source="unit57-all#13a", segment=s1),
        I("u57-109b", "phrase_cluster", "拒绝", "turn down", related="u57-turn", tags=["phrase"], source="unit57-all#13b", segment=s1),
        I("u57-109c", "phrase_cluster", "拒之门外；打发走", "turn away", related="u57-turn", tags=["phrase"], source="unit57-all#13c", segment=s1),
        I("u57-109d", "zh2en", "理论以实践为基础，反过来又服务于实践", "in turn", alts=["Theory is based on practice and in turn serves practice"], tags=["zh2en"], source="unit57-all#13d", segment=s1),
        I("u57-110", "zh2en", "打字员 / 打字机", "typist / typewriter", alts=["typist", "typewriter"], tags=["zh2en"], source="unit57-all#14", segment=s1),
        I("u57-111", "zh2en", "做……是某人的典型特征", "It is typical of sb to do", alts=["be typical of"], tags=["zh2en"], source="unit57-all#15", segment=s1),
        I("u57-112", "zh2en", "未意识到", "be unaware of", alts=["unaware of"], tags=["zh2en"], source="unit57-all#16", segment=s2),
        I("u57-113", "zh2en", "无意识的欲望", "unconscious desire", tags=["zh2en"], source="unit57-all#17", segment=s2),
        I("u57-114", "zh2en", "乘地铁", "by underground", alts=["by subway", "by metro"], tags=["zh2en"], source="unit57-all#18", segment=s2),
        I("u57-115", "zh2en", "不速之客", "an unexpected guest", alts=["uninvited guest"], tags=["zh2en"], source="unit57-all#19", segment=s2),
        I("u57-116", "cloze", "students ____ uniform", "in", tags=["collocation"], source="unit57-all#20", segment=s2),
        I("u57-117", "cloze", "be unique ____ sb./sth.", "to", tags=["collocation"], source="unit57-all#21", segment=s2),
        I("u57-118", "pattern", "直到半夜她才睡着（not ... until 倒装）", "Not until midnight did she fall asleep", alts=["Not until midnight did she go to sleep"], tags=["pattern"], source="unit57-all#22", segment=s2),
        I("u57-119", "zh2en", "他在忙什么？/ 他在搞什么鬼？", "What is he up to?", alts=["be up to"], tags=["zh2en"], source="unit57-all#23", segment=s2),
        I("u57-120", "zh2en", "最新的；跟上时代的", "up to date", alts=["up-to-date"], tags=["zh2en"], source="unit57-all#24", segment=s2),
        I("u57-121", "zh2en", "教养；培养", "upbringing", tags=["zh2en"], source="unit57-all#25", segment=s2),
        I("u57-122", "zh2en", "上传 / 下载", "upload / download", tags=["zh2en"], source="unit57-all#26", segment=s2),
        I("u57-123", "zh2en", "发表一个振奋人心的演讲", "deliver an uplifting speech", alts=["make an inspiring speech"], tags=["zh2en"], source="unit57-all#27", segment=s2),
        I("u57-124", "zh2en", "告诉项目进展的最新消息", "update sb on the progress of the project", alts=["keep sb updated on the project"], tags=["zh2en"], source="unit57-all#28", segment=s2),
    ]
    return {"unitId": "57", "name": "Unit 57", "order": 57, "wordsPerUnit": 50, "items": items}


def unit58() -> dict:
    u = "58"
    s1, s2 = "1-25", "26-50"
    I = lambda *a, **k: item(u, *a, **k)
    items = [
        I("u58-101", "word_form", "Her eyes were red and ____（泪水汪汪）", "watery", alts=["tearful"], blanks=[blank("watery", alts=["tearful"])], tags=["word_form"], source="unit58-all#6", segment=s1),
        I("u58-102", "cloze", "declare war ____ pollution", "on", tags=["collocation"], source="unit58-all#7", segment=s1),
        I("u58-103a", "zh2en", "跑步前需要热身", "You need to warm up before running", alts=["warm up"], tags=["zh2en"], source="unit58-all#8a", segment=s1),
        I("u58-103b", "zh2en", "几个笑话让讨论活跃起来", "A few jokes helped warm up the discussion", tags=["zh2en"], source="unit58-all#8b", segment=s1),
        I("u58-104", "zh2en", "发出警告", "sound a warning", alts=["give a warning", "issue a warning"], tags=["zh2en"], source="unit58-all#9", segment=s1),
        I("u58-105", "zh2en", "监视；留意", "keep a watch on", alts=["keep watch on", "keep an eye on"], tags=["zh2en"], source="unit58-all#10", segment=s1),
        I("u58-106", "zh2en", "因谋杀被通缉", "be wanted for the murder", alts=["be wanted for murder"], tags=["zh2en"], source="unit58-all#11", segment=s1),
        I("u58-107", "zh2en", "任务因缺乏资金被推迟", "The task was postponed for lack of / due to lack of funds", alts=["for lack of funds", "for want of funds"], tags=["zh2en"], source="unit58-all#12", segment=s1),
        I("u58-108", "word_form", "The desk wants ____（repair）.", "repairing", alts=["to be repaired"], blanks=[blank("repairing", alts=["to be repaired"])], hint="repair", tags=["word_form", "pattern"], source="unit58-all#13", segment=s1),
        I("u58-109", "zh2en", "凭借；由于", "by virtue of", alts=["by means of"], tags=["zh2en"], source="unit58-all#14", segment=s1),
        I("u58-110", "zh2en", "这个项目实际上是一场灾难", "The project was a virtual disaster", alts=["virtual disaster"], tags=["zh2en"], source="unit58-all#15", segment=s1),
        I("u58-111", "zh2en", "一个有远见的领袖", "a visionary leader", tags=["zh2en"], source="unit58-all#16", segment=s1),
        I("u58-112", "zh2en", "意识到危险", "be aware of the danger", alts=["realize the danger"], tags=["zh2en"], source="unit58-all#17", segment=s1),
        I("u58-113", "zh2en", "打破……之间的隔阂", "break down the wall between", alts=["break down barriers between"], tags=["zh2en"], source="unit58-all#18", segment=s1),
        I("u58-114", "zh2en", "在街上闲逛", "wander in the street", alts=["wander the streets", "walk around the street"], tags=["zh2en"], source="unit58-all#19", segment=s2),
        I("u58-115", "zh2en", "别开小差", "Don't let your mind wander", alts=["Don't wander off"], tags=["zh2en"], source="unit58-all#20", segment=s2),
        I("u58-116a", "phrase_cluster", "调高音量", "turn up the volume", related="u58-volume", tags=["phrase"], source="unit58-all#21a", segment=s2),
        I("u58-116b", "phrase_cluster", "容器的容积", "the volume of the container", related="u58-volume", tags=["phrase"], source="unit58-all#21b", segment=s2),
        I("u58-116c", "phrase_cluster", "一部五卷本小说", "a novel in 5 volumes", related="u58-volume", tags=["phrase"], source="unit58-all#21c", segment=s2),
        I("u58-117", "zh2en", "自愿做……", "volunteer to do", alts=["volunteer for"], tags=["zh2en"], source="unit58-all#22", segment=s2),
        I("u58-118", "zh2en", "做志愿工作", "do voluntary work", alts=["do volunteer work"], tags=["zh2en"], source="unit58-all#23", segment=s2),
        I("u58-119", "cloze", "pay a visit ____ sb/sth", "to", tags=["collocation"], source="unit58-all#24", segment=s2),
        I("u58-120", "cloze", "____ a loud voice", "in", tags=["collocation"], source="unit58-all#25", segment=s2),
        I("u58-121", "word_form", "vital（名词）", "vitality", hint="vital", tags=["word_form"], source="unit58-all#26", segment=s2),
        I("u58-122", "zh2en", "公众的强烈反应", "a violent reaction from the public", tags=["zh2en"], source="unit58-all#27", segment=s2),
        I("u58-123a", "phrase_cluster", "生动的记忆", "a vivid memory", related="u58-vivid", tags=["phrase"], source="unit58-all#28a", segment=s2),
        I("u58-123b", "phrase_cluster", "生动地描述", "give a vivid account of", related="u58-vivid", tags=["phrase"], source="unit58-all#28b", segment=s2),
        I("u58-123c", "phrase_cluster", "乡村生活的生动画面", "a vivid picture of rural life", related="u58-vivid", tags=["phrase"], source="unit58-all#28c", segment=s2),
    ]
    return {"unitId": "58", "name": "Unit 58", "order": 58, "wordsPerUnit": 50, "items": items}


def unit59() -> dict:
    u = "59"
    s1, s2 = "1-25", "26-50"
    I = lambda *a, **k: item(u, *a, **k)
    items = [
        I("u59-101", "zh2en", "全神贯注于讲座", "be wrapped up in the lecture", alts=["be wrapped in the lecture", "be absorbed in the lecture"], tags=["zh2en"], source="unit59-59-60#3", segment=s1),
        I("u59-102", "cloze", "____ the problem（全力解决问题）", "wrestle with", alts=["tackle", "deal with"], blanks=[blank("wrestle with", alts=["tackle", "deal with"])], tags=["collocation"], source="unit59-59-60#4", segment=s1),
        I("u59-103", "zh2en", "书面语", "written language", alts=["the written word"], tags=["zh2en"], source="unit59-59-60#5", segment=s1),
        I("u59-104", "zh2en", "冤枉某人；对待某人不公", "do sb wrong", alts=["do wrong to sb"], tags=["zh2en"], source="unit59-59-60#6", segment=s1),
        I("u59-105", "zh2en", "按年计算", "by the year", alts=["yearly", "on a yearly basis"], tags=["zh2en"], source="unit59-59-60#7", segment=s1),
        I("u59-106", "zh2en", "他被学校劝退/退学了", "He was withdrawn from school", alts=["withdraw from school"], tags=["zh2en"], source="unit59-59-60#8", segment=s1),
        I("u59-107", "zh2en", "奏效；创造奇迹", "work wonders", alts=["do wonders", "work miracles"], tags=["zh2en"], source="unit59-59-60#9", segment=s1),
        I("u59-108a", "cloze", "The little boy finished all the housework ____ himself.", "by", tags=["collocation"], source="unit59-59-60#10a", segment=s1),
        I("u59-108b", "cloze", "You should fight ____ yourself.", "for", tags=["collocation"], source="unit59-59-60#10b", segment=s1),
        I("u59-108c", "cloze", "I want to have a bedroom ____ myself.", "to", tags=["collocation"], source="unit59-59-60#10c", segment=s1),
        I("u59-109", "zh2en", "今天没有咖啡也行", "I can do without coffee today", alts=["do without"], tags=["zh2en"], source="unit59-59-60#11", segment=s1),
        I("u59-110", "zh2en", "到底是什么让你哭了？", "What in the world made you cry?", alts=["on earth"], tags=["zh2en"], source="unit59-59-60#12", segment=s1),
        I("u59-111", "zh2en", "在进行中", "under way", alts=["underway"], tags=["zh2en"], source="unit59-59-60#13", segment=s2),
        I("u59-112", "zh2en", "经由；作为", "by way of", tags=["zh2en"], source="unit59-59-60#14", segment=s2),
        I("u59-113", "zh2en", "即将成功；在通往成功的路上", "be on the way to success", tags=["zh2en"], source="unit59-59-60#15a", segment=s2),
        I("u59-114", "zh2en", "穿破；使精疲力竭", "wear out", tags=["zh2en"], source="unit59-59-60#15b", segment=s2),
        I("u59-115", "zh2en", "磨损", "wear and tear", tags=["zh2en"], source="unit59-59-60#16", segment=s2),
        I("u59-116", "word_form", "wear（过去式/过去分词/形容词）", "wore/worn/worn", alts=["wore", "worn"], blanks=[blank("wore/worn/worn", alts=["wore", "worn"])], hint="wear", tags=["word_form"], source="unit59-59-60#17", segment=s2),
        I("u59-117", "zh2en", "她在花园里除草", "she is weeding in the garden", alts=["weed the garden"], tags=["zh2en"], source="unit59-59-60#18", segment=s2),
        I("u59-118", "zh2en", "流下痛苦的眼泪", "shed bitter tears", alts=["weep bitter tears"], tags=["zh2en"], source="unit59-59-60#19", segment=s2),
        I("u59-119", "zh2en", "没有恰当管束，坏习惯会像野草一样蔓延", "Without proper control, bad habits will grow like weeds", alts=["grow like weeds"], tags=["zh2en"], source="unit59-59-60#20", segment=s2),
        I("u59-120", "zh2en", "靠福利生活", "manage on welfare", alts=["live on welfare"], tags=["zh2en"], source="unit59-59-60#21", segment=s2),
        I("u59-121", "zh2en", "成本超过了回报", "The costs outweigh the rewards", alts=["outweigh"], tags=["zh2en"], source="unit59-59-60#22", segment=s2),
        I("u59-122", "zh2en", "他拥抱妻子，热泪盈眶", "He hugged his wife, with tears in his eyes", alts=["eyes filled with tears", "tearfully"], tags=["zh2en"], source="unit59-59-60#23", segment=s2),
    ]
    return {"unitId": "59", "name": "Unit 59", "order": 59, "wordsPerUnit": 50, "items": items}


def main() -> None:
    for builder in (unit55, unit57, unit58, unit59):
        write_unit(wrap(builder))


if __name__ == "__main__":
    main()
