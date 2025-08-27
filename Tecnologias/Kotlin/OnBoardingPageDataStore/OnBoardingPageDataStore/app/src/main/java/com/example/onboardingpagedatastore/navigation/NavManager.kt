package com.example.onboardingpagedatastore.navigation

import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.platform.LocalContext
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.onboardingpagedatastore.MainOnBoarding
import com.example.onboardingpagedatastore.dataStore.StoreBoarding
import com.example.onboardingpagedatastore.views.HomeView
import com.example.onboardingpagedatastore.views.SplashScreen


@Composable
fun NavManager(){

    val context = LocalContext.current
    val dataStore = StoreBoarding(context);
    val store = dataStore.getBoarding.collectAsState(initial = false)

    val navController = rememberNavController()
    NavHost(navController = navController, startDestination = if(store.value) "Home" else "Splash"){
        composable("OnBoarding"){
            MainOnBoarding(navController,dataStore)
        }
        composable("Home"){
            HomeView(navController)
        }

        composable("Splash"){
            SplashScreen(navController,store.value)

        }
    }
}