package com.example.viewmodelpracticaproyecto.views

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.viewmodelpracticaproyecto.viewModels.SavedStateHandlerViewModel


@Composable
fun SavedStateHandlerView(navController: NavController, viewModel: SavedStateHandlerViewModel = viewModel ()) {

    var textoInput by remember{mutableStateOf("")}

    Box(
        modifier = Modifier
            .fillMaxSize()
    ){
        Column(
            modifier=Modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ){
            Text("User ID: ${viewModel.userId}")

            TextField(
                value = textoInput,
                onValueChange = {
                    textoInput= it
                }
            )

            Button(onClick = {
                viewModel.userId = "textoInput"
            }) {
                Text("Update")
            }

        }
    }


}