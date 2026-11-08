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
    val sourceRef: String = ""
)

data class UnitBank(
    val unitId: String,
    val name: String,
    val order: Int,
    val items: List<QuizItem>
)

data class UnitMeta(
    val unitId: String,
    val name: String,
    val order: Int,
    val file: String
)

enum class GradeVerdict {
    CORRECT, PARTIAL, WRONG
}

enum class QuizMode {
    ZH2EN, CLOZE, MIXED, WRONG_ONLY
}
