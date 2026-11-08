package com.goodmanyiyi.words3500.data

import android.content.Context
import com.goodmanyiyi.words3500.domain.Blank
import com.goodmanyiyi.words3500.domain.QuizItem
import com.goodmanyiyi.words3500.domain.UnitBank
import com.goodmanyiyi.words3500.domain.UnitMeta
import org.json.JSONArray
import org.json.JSONObject

class ContentRepository(private val context: Context) {
    fun loadManifest(): List<UnitMeta> {
        val text = readAsset("content/manifest.json")
        val root = JSONObject(text)
        val units = root.getJSONArray("units")
        val list = mutableListOf<UnitMeta>()
        for (i in 0 until units.length()) {
            val u = units.getJSONObject(i)
            list.add(
                UnitMeta(
                    unitId = u.getString("unitId"),
                    name = u.getString("name"),
                    order = u.optInt("order", 0),
                    file = u.getString("file")
                )
            )
        }
        return list.sortedBy { it.order }
    }

    fun loadUnit(fileName: String): UnitBank {
        val text = readAsset("content/$fileName")
        val root = JSONObject(text)
        val itemsJson = root.getJSONArray("items")
        val items = mutableListOf<QuizItem>()
        for (i in 0 until itemsJson.length()) {
            items.add(parseItem(itemsJson.getJSONObject(i)))
        }
        return UnitBank(
            unitId = root.getString("unitId"),
            name = root.getString("name"),
            order = root.optInt("order", 0),
            items = items
        )
    }

    private fun parseItem(obj: JSONObject): QuizItem {
        return QuizItem(
            id = obj.getString("id"),
            unitId = obj.getString("unitId"),
            type = obj.getString("type"),
            prompt = obj.getString("prompt"),
            answerPrimary = obj.getString("answerPrimary"),
            answerAlts = obj.optJSONArray("answerAlts").toStringList(),
            blanks = obj.optJSONArray("blanks").toBlanks(),
            hint = obj.optString("hint", ""),
            tags = obj.optJSONArray("tags").toStringList(),
            relatedGroupId = obj.optString("relatedGroupId", ""),
            sourceRef = obj.optString("sourceRef", "")
        )
    }

    private fun JSONArray?.toStringList(): List<String> {
        if (this == null) return emptyList()
        val list = mutableListOf<String>()
        for (i in 0 until length()) {
            list.add(getString(i))
        }
        return list
    }

    private fun JSONArray?.toBlanks(): List<Blank> {
        if (this == null) return emptyList()
        val list = mutableListOf<Blank>()
        for (i in 0 until length()) {
            val b = getJSONObject(i)
            list.add(
                Blank(
                    index = b.getInt("index"),
                    answer = b.getString("answer"),
                    alts = b.optJSONArray("alts").toStringList()
                )
            )
        }
        return list
    }

    private fun readAsset(path: String): String {
        return context.assets.open(path).bufferedReader(Charsets.UTF_8).use { it.readText() }
    }
}
