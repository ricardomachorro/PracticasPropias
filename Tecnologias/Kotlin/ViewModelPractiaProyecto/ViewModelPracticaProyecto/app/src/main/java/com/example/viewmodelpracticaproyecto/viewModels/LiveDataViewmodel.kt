package com.example.viewmodelpracticaproyecto.viewModels

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel


class LiveDataViemodel: ViewModel(){

    private val _contador = MutableLiveData<Int>()
    val contador: LiveData<Int> get()= _contador

    fun add(){
        _contador.value++

    }

}