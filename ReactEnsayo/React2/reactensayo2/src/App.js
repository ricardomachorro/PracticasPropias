import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
/*Asi se importan elementos de otros scripts*/
import Elemento1 from "./componentes/Elemento1";

class App extends Component {
/*Este es la forma de crear un elemento  que seria algo como una variable de un elemento en */
/*En este caso se ase con un constructor*/
 constructor(props){
   super(props);/*Esta parte es el constructor del elementod entro del DOM */
   /*Para definir las variables con constructor es con
   'this.state={variable1:contenido_variable1,variable2:contenido_variable2}'*/
   this.state={
     array:['Array','fix','bugs'],
     user_name:'Rick',
     profesion:'Programador'
   };
 }

 handleClick(){
   /*'setState' es un metodo por el cul se pueden acceder y cmabiar las variables de estado del DOM*/
     this.setState({
       user_name:'Ricardo Machorro',
       profesion:'Web Tester'
     });
 }


  render() {

    /*En esta parte se pasan los elementos del state a una constante que
    se podra usar en todo el Render*/
   const {array2}=this.state

    return (

      <div>
        <div>
         {this.state.array.map(word=>{
           return(
             <p key={word}>{word}</p>
           )
         })}
         </div>
         <div>
           <p >{this.state.user_name}-{this.state.profesion}</p>

         </div>
         <br></br>
         <hr></hr>
         <br></br>
         <div>
           {/*Para acceder a funciones que no tienen acceso al state como la de  'hendelClick'
             se tiene que usar '.bind(this)' para que puedan acceder al State*/}
           <button onClick={this.handleClick.bind(this)}>Haz click</button>
         </div>

       <div>
         {/*Para pasar informción o data de a otros elementos se usa hace asi*/}
          <Elemento1 user_name="Rick"></Elemento1>
          {/*Se puede pasar mas de un  elemento como parametros de state*/}
          <Elemento1 user_name="Rick" profession={"Carpintero"}></Elemento1>
          {/*Tambien se puede pasar elementos sin que esten completos*/}
          <Elemento1 user_name="Rick"></Elemento1>

   <hr></hr>
   <hr></hr>
        {/*Esto sirve mucho para  cmabiar elementos desde el state*/}
        <Elemento1 user_name={this.state.user_name} profession={this.state.profesion}></Elemento1>

       </div>

      </div>
    );
  }
}

export default App;
