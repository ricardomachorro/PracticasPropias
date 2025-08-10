package com.example.viewmodelpracticaproyecto.views

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material3.FloatingActionButton
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.viewmodelpracticaproyecto.viewModels.LiveDataViemodel


@Composable
fun LiveDataView(navController: NavController,liveDataViewModel: LiveDataViemodel = viewModel()  ){
    Box(
        contentAlignment = Alignment.Center,
        modifier = Modifier
            .fillMaxSize()
            .padding(55.dp)


    ){
        Text(
            text= liveDataViewModel.contador.value.toString(),
            fontWeight = FontWeight.Bold,
            fontSize = 40.sp
        )
        FloatingActionButton(
            onClick = {liveDataViewModel.add()},
            modifier = Modifier
                .align(Alignment.BottomEnd)
                .padding(15.dp)
        ){
            Icon(
                imageVector = Icons.Default.Add,
                contentDescription = "Add",
                tint = Color.White
            )

        }

    }
}