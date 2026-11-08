package com.goodmanyiyi.words3500.domain

object QuizEngine {
    fun filterByMode(items: List<QuizItem>, mode: QuizMode, wrongIds: Set<String>): List<QuizItem> {
        return when (mode) {
            QuizMode.ZH2EN -> items.filter { it.type == "zh2en" }
            QuizMode.CLOZE -> items.filter { it.type == "cloze" || it.type == "word_form" }
            QuizMode.MIXED -> items
            QuizMode.WRONG_ONLY -> items.filter { wrongIds.contains(it.id) }
        }
    }

    fun pickSession(pool: List<QuizItem>, count: Int, mode: QuizMode): List<QuizItem> {
        if (pool.isEmpty()) return emptyList()
        val weighted = when (mode) {
            QuizMode.MIXED -> weightedShuffle(pool)
            else -> pool.shuffled()
        }
        return weighted.take(count.coerceAtMost(weighted.size))
    }

    private fun weightedShuffle(items: List<QuizItem>): List<QuizItem> {
        val weightOf = { type: String ->
            when (type) {
                "zh2en" -> 3
                "cloze" -> 3
                "word_form" -> 2
                "phrase_cluster" -> 2
                "pattern" -> 1
                else -> 1
            }
        }
        val bag = mutableListOf<QuizItem>()
        items.forEach { item ->
            repeat(weightOf(item.type)) { bag.add(item) }
        }
        return bag.shuffled().distinctBy { it.id }
    }
}
