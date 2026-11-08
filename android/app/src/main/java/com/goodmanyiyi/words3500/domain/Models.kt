package com.goodmanyiyi.words3500.domain

data class Blank(
    val index: Int,
    val answer: String,
    val alts: List<String> = emptyList()
)

data class QuizItem(
    val id: String,
    val unitId: String,
    val type: String,
    val prompt: String,
    val answerPrimary: String,
    val answerAlts: List<String> = emptyList(),
    val blanks: List<Blank> = emptyList(),
    val hint: String = "",
    val tags: List<String> = emptyList(),
    val relatedGroupId: String = "",
    val sourceRef: String = "",
    val segment: String = ""
)

data class UnitBank(
    val unitId: String,
    val name: String,
    val order: Int,
    val items: List<QuizItem>,
    val rangeFrom: String = "",
    val rangeTo: String = "",
    val wordsPerUnit: Int = 50
)

data class UnitMeta(
    val unitId: String,
    val name: String,
    val order: Int,
    val file: String,
    val rangeFrom: String = "",
    val rangeTo: String = "",
    val wordsPerUnit: Int = 50,
    val hasContent: Boolean = false
)

enum class GradeVerdict {
    CORRECT, PARTIAL, WRONG
}

enum class QuizMode {
    ZH2EN, CLOZE, MIXED, WRONG_ONLY
}

enum class QuizSegment {
    ALL, FIRST_25, LAST_25
}
