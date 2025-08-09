package com.example.viewmodelpracticaproyecto.navigation

sealed class Screen(val route: String) {

    object Home: Screen("home_page")
    object ViewModelWithoutParameters: Screen("viewModel_without_parameters")
}