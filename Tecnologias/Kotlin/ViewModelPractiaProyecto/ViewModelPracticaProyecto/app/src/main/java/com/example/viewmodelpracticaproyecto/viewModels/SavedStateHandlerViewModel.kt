package com.example.viewmodelpracticaproyecto.viewModels

import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel

class SavedStateHandlerViewModel( savedStateHandle: SavedStateHandle): ViewModel() {

    val userId: String = savedStateHandle["userId"] ?: "unknown"
}