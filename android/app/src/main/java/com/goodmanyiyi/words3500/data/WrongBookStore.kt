package com.goodmanyiyi.words3500.data

import android.content.Context

class WrongBookStore(context: Context) {
    private val prefs = context.getSharedPreferences("wrong_book", Context.MODE_PRIVATE)

    fun wrongIds(): Set<String> {
        return prefs.getStringSet(KEY_IDS, emptySet())?.toSet() ?: emptySet()
    }

    fun markWrong(itemId: String) {
        val next = wrongIds().toMutableSet()
        next.add(itemId)
        prefs.edit().putStringSet(KEY_IDS, next).apply()
        val count = prefs.getInt(countKey(itemId), 0) + 1
        prefs.edit().putInt(countKey(itemId), count).apply()
    }

    fun markCorrect(itemId: String) {
        val next = wrongIds().toMutableSet()
        next.remove(itemId)
        prefs.edit().putStringSet(KEY_IDS, next).apply()
    }

    fun wrongCount(itemId: String): Int {
        return prefs.getInt(countKey(itemId), 0)
    }

    fun clearAll() {
        prefs.edit().clear().apply()
    }

    private fun countKey(itemId: String): String = "count_$itemId"

    companion object {
        private const val KEY_IDS = "ids"
    }
}
