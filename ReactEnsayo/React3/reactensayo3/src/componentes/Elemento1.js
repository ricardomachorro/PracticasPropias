import React, { Component } from 'react';
/*Esto es un comonente de la App principal*/

class Elemento1 extends Component {


  constructor(props){
    super(props);
    this.state={
        nombre_desplegado:'Primer Nombre'
    };
  }
  componentDidMount(){
    console.log("mounted");
  }

  componentWillReceiveProps(nextProps){
       console.log(nextProps);
  }

  render() {
    /*Se pueden pasar variables de la siguiente forma*/
       var word="hello";
       var style1={fontSize:'20px'};

      /*Para obtener datos de otros elementos se usa 'this.props'*/
       const {user_name}=this.props;
       const {profession}=this.props;
       const {nombre_desplegado}=this.state;

    return (


      <div>
          <div>
            <p>Nombre: {user_name}</p>
          </div>
          <div>
            {/*Tambien se puede cambiar el comprtamientos de los elementos , dependiendo de los parametros
              que reciba un elemento de la clase , en el siguiente ejemplo se comprueba si el parametro
              'profession' esta vacio , si lo esta le da el valor de 'No hay profesion'*/}

            <p>Profesion:{profession ? profession: "No hay profesion"}</p>
          </div>
          <div>
            <p>{nombre_desplegado}</p>
          </div>
      </div>

    );
  }
}

export default Elemento1;
