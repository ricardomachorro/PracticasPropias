package com.example.viewmodelpracticaproyecto.navigation

sealed class Screen(val route: String) {

    object Home: Screen("home_page")
    object StateViewModel: Screen("state_viewmodel")
    object LiveDataViewModel:Screen("live_data_viewmodel")

    object SavedStateHandlerViewModel_Screen:Screen("saved_state_handler_viewmodel_screen")


}