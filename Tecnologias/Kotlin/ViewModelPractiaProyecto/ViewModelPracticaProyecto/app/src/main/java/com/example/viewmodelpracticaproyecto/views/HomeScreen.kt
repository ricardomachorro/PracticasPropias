package com.example.viewmodelpracticaproyecto.views

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.navigation.NavController
import com.example.viewmodelpracticaproyecto.navigation.Screen


@Composable
fun HomeScreen(navController: NavController) {

    val text by remember{mutableStateOf("")}

    Box(
        modifier =  Modifier.fillMaxSize()
    ){
        Row(
            modifier = Modifier.fillMaxSize(),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            Button(
                onClick = {
                    navController.navigate(Screen.ViewModelWithoutParameters.route)
                }
            ){
                 Text("ViewModel Without Parameters")
            }

        }
    }

}