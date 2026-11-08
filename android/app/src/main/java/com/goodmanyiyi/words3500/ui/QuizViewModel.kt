package com.goodmanyiyi.words3500.ui

import android.app.Application
import android.speech.tts.TextToSpeech
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.AndroidViewModel
import com.goodmanyiyi.words3500.data.ContentRepository
import com.goodmanyiyi.words3500.data.WrongBookStore
import com.goodmanyiyi.words3500.domain.GradeVerdict
import com.goodmanyiyi.words3500.domain.Grader
import com.goodmanyiyi.words3500.domain.QuizEngine
import com.goodmanyiyi.words3500.domain.QuizItem
import com.goodmanyiyi.words3500.domain.QuizMode
import com.goodmanyiyi.words3500.domain.UnitMeta
import java.util.Locale

data class QuizUiState(
    val units: List<UnitMeta> = emptyList(),
    val selectedUnit: UnitMeta? = null,
    val mode: QuizMode = QuizMode.MIXED,
    val session: List<QuizItem> = emptyList(),
    val index: Int = 0,
    val input: String = "",
    val revealed: Boolean = false,
    val lastVerdict: GradeVerdict? = null,
    val correctCount: Int = 0,
    val answeredCount: Int = 0,
    val wrongIds: Set<String> = emptySet(),
    val finished: Boolean = false,
    val message: String = ""
)

class QuizViewModel(app: Application) : AndroidViewModel(app) {
    private val repo = ContentRepository(app)
    private val wrongBook = WrongBookStore(app)
    private var tts: TextToSpeech? = null

    var state by mutableStateOf(QuizUiState())
        private set

    init {
        tts = TextToSpeech(app) { status ->
            if (status == TextToSpeech.SUCCESS) {
                tts?.language = Locale.US
            }
        }
        val units = repo.loadManifest()
        state = state.copy(
            units = units,
            selectedUnit = units.firstOrNull(),
            wrongIds = wrongBook.wrongIds()
        )
    }

    fun selectUnit(unit: UnitMeta) {
        state = state.copy(selectedUnit = unit)
    }

    fun selectMode(mode: QuizMode) {
        state = state.copy(mode = mode)
    }

    fun startSession(count: Int = 25) {
        val unit = state.selectedUnit ?: return
        val bank = repo.loadUnit(unit.file)
        val pool = QuizEngine.filterByMode(bank.items, state.mode, wrongBook.wrongIds())
        val session = QuizEngine.pickSession(pool, count, state.mode)
        if (session.isEmpty()) {
            state = state.copy(message = "当前范围没有可抽题目")
            return
        }
        state = state.copy(
            session = session,
            index = 0,
            input = "",
            revealed = false,
            lastVerdict = null,
            correctCount = 0,
            answeredCount = 0,
            finished = false,
            message = "",
            wrongIds = wrongBook.wrongIds()
        )
    }

    fun updateInput(value: String) {
        state = state.copy(input = value)
    }

    fun submit() {
        val item = currentItem() ?: return
        if (state.revealed) return
        val verdict = Grader.grade(item, state.input)
        when (verdict) {
            GradeVerdict.CORRECT -> wrongBook.markCorrect(item.id)
            GradeVerdict.PARTIAL, GradeVerdict.WRONG -> wrongBook.markWrong(item.id)
        }
        val correctDelta = if (verdict == GradeVerdict.CORRECT) 1 else 0
        state = state.copy(
            revealed = true,
            lastVerdict = verdict,
            correctCount = state.correctCount + correctDelta,
            answeredCount = state.answeredCount + 1,
            wrongIds = wrongBook.wrongIds()
        )
    }

    fun reveal() {
        val item = currentItem() ?: return
        if (!state.revealed) {
            wrongBook.markWrong(item.id)
            state = state.copy(
                revealed = true,
                lastVerdict = GradeVerdict.WRONG,
                answeredCount = state.answeredCount + 1,
                wrongIds = wrongBook.wrongIds()
            )
        }
    }

    fun next() {
        val nextIndex = state.index + 1
        if (nextIndex >= state.session.size) {
            state = state.copy(finished = true)
            return
        }
        state = state.copy(
            index = nextIndex,
            input = "",
            revealed = false,
            lastVerdict = null
        )
    }

    fun speakAnswer() {
        val item = currentItem() ?: return
        val text = if (item.blanks.isNotEmpty()) {
            item.blanks.joinToString(" ") { it.answer }
        } else {
            item.answerPrimary
        }
        tts?.speak(text, TextToSpeech.QUEUE_FLUSH, null, item.id)
    }

    fun currentItem(): QuizItem? {
        return state.session.getOrNull(state.index)
    }

    fun exitSession() {
        state = state.copy(session = emptyList(), finished = false, message = "")
    }

    override fun onCleared() {
        tts?.shutdown()
        super.onCleared()
    }
}
