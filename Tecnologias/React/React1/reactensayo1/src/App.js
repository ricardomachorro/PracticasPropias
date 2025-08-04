import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
/*Esta importacion permitetraer componenetes del Elemento1 */
import Elemento1 from './componentes/Elemento1';

class App extends Component {

  componentDidMount(){
    console.log("mounted");
  }

  consosoleLog(){
    console.log("Funciona");
  }

  render() {
    /*Se pueden pasar variables de la siguiente forma*/
       var word="hello";
       var style1={fontSize:'20px'};
       var array=['Funciona','el','array','perfectamente'];
       var arraytoRender=[];
       /*Este es un valor constante o sea que no cambiara o podra volver aser asignada en el codigo*/
       const Pi="Constante";

       array.forEach(function(word){
          arraytoRender.push(
          /*En react para identificar elementos se usa " key={palabra_clave} "*/
           <p key={word}>{word}</p>
          )
       });

    return (

      /*<div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>*/



      <div>
          {/*Asi se comenta*/}

            {/*En vez de usar class=' ' se usa  className=' '*/}
            {/*Para el estilo css u style se ase con style={{css_caracteristica}}*/}
          <p style={{fontSize:'20px'}} className="text-large">Hi</p>
          <img src="none.jpg"></img>
            <div>
               <p>Hi</p>
               {/*Se puede remplazar luego las variables en la renderizacion*/}
               <p style={style1}>{word}</p>
                {/*La etiqueta siguiente la saca de la importacion de un componente Elemento1 */}
               <Elemento1></Elemento1>
               <hr></hr>
                 {/*Estas son formas de poder hacer eventos */}

                {/*Si solo se quiere hacer una accion simle se ase: */}
               <button onClick={()=>{console.log("Deus vault")}}>Presioname</button>
               <br></br>
               <br></br>
              {/*Si solo se quiere hacer una funcion de la App se ase: */}
                <button onClick={this.consosoleLog}>Presioname 2</button>
               <br></br>
               <br></br>
              {arraytoRender}
                <hr></hr>
                <br></br>
                <br></br>
                {/*Esta es otra forma de incluir una funcion de manera mejor integrada
                 se ase con array.map()  */}
                {array.map(word=>{
                  return(

                    <p key={word}>{word}</p>
                  )
                })}
                <br></br>
                <br></br>
                <hr></hr>
                <button onClick={()=>{console.log("presionado")}}>Presioname</button>
            </div>
      </div>

    );
  }
}

export default App;
