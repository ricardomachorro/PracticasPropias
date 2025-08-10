package com.example.viewmodelpracticaproyecto.navigation

sealed class Screen(val route: String) {

    object Home: Screen("home_page")
    object StateViewModel: Screen("state_viewModel")
    object LiveDataViewModel:Screen("live_data_viewmodel")
}