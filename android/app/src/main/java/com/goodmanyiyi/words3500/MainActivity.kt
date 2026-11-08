package com.goodmanyiyi.words3500

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import com.goodmanyiyi.words3500.ui.HomeScreen
import com.goodmanyiyi.words3500.ui.QuizViewModel

class MainActivity : ComponentActivity() {
    private val vm: QuizViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                Surface {
                    HomeScreen(vm)
                }
            }
        }
    }
}
