package com.goodmanyiyi.words3500.domain

object Grader {
    fun normalize(raw: String): String {
        var s = raw.trim().lowercase()
        s = s.replace(Regex("\\s+"), " ")
        s = s.trimEnd('.', '?', '!', ';', ':', ',')
        return s
    }

    fun grade(item: QuizItem, userInput: String): GradeVerdict {
        val blanks = item.blanks
        if (blanks.isNotEmpty()) {
            val parts = userInput
                .split('|', '\n')
                .map { it.trim() }
                .filter { it.isNotEmpty() }
            if (parts.size < blanks.size) {
                val matched = blanks.indices.count { i ->
                    i < parts.size && matchesAny(parts[i], blankCandidates(blanks[i]))
                }
                return when {
                    matched == 0 -> GradeVerdict.WRONG
                    matched < blanks.size -> GradeVerdict.PARTIAL
                    else -> GradeVerdict.CORRECT
                }
            }
            var correctCount = 0
            for (i in blanks.indices) {
                if (matchesAny(parts[i], blankCandidates(blanks[i]))) {
                    correctCount += 1
                }
            }
            return when (correctCount) {
                blanks.size -> GradeVerdict.CORRECT
                0 -> GradeVerdict.WRONG
                else -> GradeVerdict.PARTIAL
            }
        }

        val candidates = listOf(item.answerPrimary) + item.answerAlts
        return if (matchesAny(userInput, candidates)) {
            GradeVerdict.CORRECT
        } else {
            GradeVerdict.WRONG
        }
    }

    private fun blankCandidates(blank: Blank): List<String> {
        return listOf(blank.answer) + blank.alts
    }

    private fun matchesAny(input: String, candidates: List<String>): Boolean {
        val normalized = normalize(input)
        return candidates.any { normalize(it) == normalized }
    }
}
