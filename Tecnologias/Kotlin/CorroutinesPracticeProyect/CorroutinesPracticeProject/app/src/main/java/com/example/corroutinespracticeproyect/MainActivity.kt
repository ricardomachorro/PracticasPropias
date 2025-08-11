package com.example.corroutinespracticeproyect

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.viewModels
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import com.example.corroutinespracticeproyect.ui.theme.CorroutinesPracticeProyectTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        val viewModel:ItemsViewModel  by viewModels()
        setContent {
            CorroutinesPracticeProyectTheme {
                Surface(modifier = Modifier.fillMaxSize()) {
                    ItemsView(viewModel) 
                }
            }
        }
    }
}

@Composable
fun Content(viewModel: MainViewModel){

    Column(
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ){
        BotonColor()
        if(viewModel.isLoading){
            CircularProgressIndicator()
        }else{
            Text(text=viewModel.resultState)
        }
        Button(
            onClick = { viewModel.fetchData() }
        ){
            Text(text = "Llamar API")
        }
    }

}



@Composable
fun BotonColor(){

    var color by remember { mutableStateOf(false)}

    Button(onClick = {color =!color}, colors = ButtonDefaults.buttonColors(
        containerColor = if (color) Color.Red else Color.Green
    )){
        Text("Cambiar color")
    }


}


@Composable

fun ItemsView(viewModel: ItemsViewModel){

    val itemList = viewModel.itemList

    Column(){
        if(viewModel.isLoading){
            CircularProgressIndicator()
        }else{
            LazyColumn{
               items(itemList){
                   item -> Text(text = item.name)
               }

            }
        }
    }

}
