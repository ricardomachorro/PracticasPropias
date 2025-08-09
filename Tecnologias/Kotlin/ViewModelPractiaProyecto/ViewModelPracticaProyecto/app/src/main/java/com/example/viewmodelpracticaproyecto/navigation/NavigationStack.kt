package com.example.viewmodelpracticaproyecto.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.viewmodelpracticaproyecto.views.*


@Composable
fun Navigation_Stack(){


      val navController = rememberNavController()

      NavHost(navController = navController, startDestination = Screen.Home.route){
          composable(route=Screen.Home.route){
              HomeScreen(navController)
          }
          composable(route = Screen.ViewModelWithoutParameters.route){
              ViewModelWithoutParameters(navController)
          }
      }

}