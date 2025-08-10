package com.example.viewmodelpracticaproyecto.views

import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.viewmodelpracticaproyecto.viewModels.SavedStateHandlerViewModel


@Composable
fun SavedStateHandlerView(navController: NavController, viewModel: SavedStateHandlerViewModel = viewModel ()) {
    Text("User ID: ${viewModel.userId}")
}