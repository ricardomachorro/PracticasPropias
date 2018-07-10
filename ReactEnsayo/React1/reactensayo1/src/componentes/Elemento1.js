import React, { Component } from 'react';
/*Esto es un comonente de la App principal*/

class Elemento1 extends Component {

  componentDidMount(){
    console.log("mounted");
  }

  render() {
    /*Se pueden pasar variables de la siguiente forma*/
       var word="hello";
       var style1={fontSize:'20px'};

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
          <p>Ricardo</p>
          
      </div>

    );
  }
}

export default Elemento1;
