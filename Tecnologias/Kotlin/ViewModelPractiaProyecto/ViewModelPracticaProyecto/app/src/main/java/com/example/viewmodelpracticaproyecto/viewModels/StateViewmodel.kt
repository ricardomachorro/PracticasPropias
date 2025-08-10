package com.example.viewmodelpracticaproyecto.viewModels

import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.State
import androidx.lifecycle.ViewModel


class StateViewModel : ViewModel(){


    private val _contador = mutableStateOf(0)
    val contador: State<Int> get()= _contador

    fun add(){
        _contador.value++

    }


}