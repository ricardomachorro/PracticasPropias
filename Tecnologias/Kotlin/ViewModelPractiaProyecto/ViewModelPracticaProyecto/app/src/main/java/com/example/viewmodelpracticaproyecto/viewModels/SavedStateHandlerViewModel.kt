package com.example.viewmodelpracticaproyecto.viewModels

import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel

class SavedStateHandlerViewModel( val savedStateHandle: SavedStateHandle): ViewModel() {

    var userId: String
        get()= savedStateHandle["userId"] ?: "unknown"
        set(value) {
            savedStateHandle["userId"] = value
        }
}