package com.goodmanyiyi.words3500.ui

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Button
import androidx.compose.material3.FilterChip
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier.Modifier
import androidx.compose.ui.unit.dp
import com.goodmanyiyi.words3500.domain.GradeVerdict
import com.goodmanyiyi.words3500.domain.QuizMode

@Composable
fun HomeScreen(vm: QuizViewModel) {
    val state = vm.state
    if (state.session.isNotEmpty() && !state.finished) {
        QuizScreen(vm)
        return
    }
    if (state.finished) {
        ResultScreen(vm)
        return
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        Text("3500 词汇抽背", style = MaterialTheme.typography.headlineMedium)
        Text("还原课堂：中译英 / 填空 / 混合抽查", style = MaterialTheme.typography.bodyMedium)

        Text("选择 Unit", style = MaterialTheme.typography.titleMedium)
        LazyColumn(modifier = Modifier.height(160.dp)) {
            items(state.units) { unit ->
                val selected = state.selectedUnit?.unitId == unit.unitId
                Text(
                    text = if (selected) "● ${unit.name}" else "○ ${unit.name}",
                    modifier = Modifier
                        .fillMaxWidth()
                        .clickable { vm.selectUnit(unit) }
                        .padding(vertical = 8.dp)
                )
            }
        }

        Text("抽背模式", style = MaterialTheme.typography.titleMedium)
        Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            ModeChip("中译英", state.mode == QuizMode.ZH2EN) { vm.selectMode(QuizMode.ZH2EN) }
            ModeChip("填空", state.mode == QuizMode.CLOZE) { vm.selectMode(QuizMode.CLOZE) }
            ModeChip("混合", state.mode == QuizMode.MIXED) { vm.selectMode(QuizMode.MIXED) }
            ModeChip("错题", state.mode == QuizMode.WRONG_ONLY) { vm.selectMode(QuizMode.WRONG_ONLY) }
        }

        Text("错题数：${state.wrongIds.size}")
        if (state.message.isNotEmpty()) {
            Text(state.message, color = MaterialTheme.colorScheme.error)
        }

        Button(onClick = { vm.startSession(25) }, modifier = Modifier.fillMaxWidth()) {
            Text("开始抽背（25题）")
        }
        TextButton(onClick = { vm.startSession(10) }) {
            Text("快速 10 题")
        }
    }
}

@Composable
private fun ModeChip(label: String, selected: Boolean, onClick: () -> Unit) {
    FilterChip(selected = selected, onClick = onClick, label = { Text(label) })
}

@Composable
fun QuizScreen(vm: QuizViewModel) {
    val state = vm.state
    val item = vm.currentItem() ?: return

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        Text(
            "第 ${state.index + 1}/${state.session.size} · ${item.type}",
            style = MaterialTheme.typography.labelLarge
        )
        Text(item.prompt, style = MaterialTheme.typography.headlineSmall)
        if (item.hint.isNotEmpty()) {
            Text("提示：${item.hint}", style = MaterialTheme.typography.bodySmall)
        }
        if (item.blanks.size > 1) {
            Text("多空请用 | 分隔，例如：on|under", style = MaterialTheme.typography.bodySmall)
        }

        OutlinedTextField(
            value = state.input,
            onValueChange = { vm.updateInput(it) },
            modifier = Modifier.fillMaxWidth(),
            enabled = !state.revealed,
            label = { Text("你的答案") }
        )

        if (state.revealed) {
            val verdictText = when (state.lastVerdict) {
                GradeVerdict.CORRECT -> "正确"
                GradeVerdict.PARTIAL -> "部分正确"
                GradeVerdict.WRONG -> "错误"
                null -> ""
            }
            Text("结果：$verdictText", style = MaterialTheme.typography.titleMedium)
            Text("参考答案：${item.answerPrimary}")
            if (item.answerAlts.isNotEmpty()) {
                Text("也可接受：${item.answerAlts.joinToString(" / ")}")
            }
        }

        Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            if (!state.revealed) {
                Button(onClick = { vm.submit() }) { Text("提交") }
                TextButton(onClick = { vm.reveal() }) { Text("不会 / 揭晓") }
            } else {
                Button(onClick = { vm.next() }) { Text("下一题") }
                TextButton(onClick = { vm.speakAnswer() }) { Text("发音") }
            }
        }

        Spacer(modifier = Modifier.height(8.dp))
        TextButton(onClick = { vm.exitSession() }) { Text("结束本轮") }
    }
}

@Composable
fun ResultScreen(vm: QuizViewModel) {
    val state = vm.state
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        Text("本轮结束", style = MaterialTheme.typography.headlineMedium)
        Text("正确 ${state.correctCount} / ${state.answeredCount}")
        Text("当前错题本：${state.wrongIds.size} 题")
        Button(onClick = { vm.exitSession() }, modifier = Modifier.fillMaxWidth()) {
            Text("返回首页")
        }
        Button(onClick = { vm.startSession(25) }, modifier = Modifier.fillMaxWidth()) {
            Text("再来一轮")
        }
    }
}
