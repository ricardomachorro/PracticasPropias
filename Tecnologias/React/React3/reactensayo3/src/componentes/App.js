import React, { Component } from 'react';
//import logo from './logo.svg';
//import './App.css';
/*Para poder usar bootstrap en React se tiene primero  que descargar la libreria esto se hace con:
         'npm install --save react-bootstrap'
   después de eso se tiene que importar los elementos de la libreria eso se hace asi:
    'import {Elementos_importados} from "react-bootstrap" '
 */
import {Navbar,Nav,NavItem,NavDropdown,MenuItem,Table} from "react-bootstrap";


/*Para dar eleementos seleccionables se usa la libreria  de react-select*/
/*Para esto se descarga la libreria primero con:
   'npm install --save react-bootstrap'

despues se  importa la libreria con:
import Select from "react-select";
import "react-select/dist/react-select.css" <---'Esto es para el css de la libreria'
*/
import Select from "react-select";
import "react-select/dist/react-select.css"

import {connect} from 'react-redux';
import {fetchInfo} from '../actions/actions_info'

class AppComponent extends Component {
/*Este es la forma de crear un elemento  que seria algo como una variable de un elemento en */
/*En este caso se ase con un constructor*/
 constructor(props){
   super(props);/*Esta parte es el constructor del elementod entro del DOM */
   /*Para definir las variables con constructor es con
   'this.state={variable1:contenido_variable1,variable2:contenido_variable2}'*/
   this.state={
     array:['Array','fix','bugs'],
     user_name:'Rick',
     profesion:'Programador',
     selectedOption: '',
     jsonList:[]
   };
 }

 componentDidMount() {
   /*fetch es un metodo de json para poder obtener elementos de un objeto json */
   /*fetch('http://www.json-generator.com/api/json/get/bVDxTQSDQO?indent=2', {
       method: 'GET'
     })
     .then(response => response.json())
     .then(json => {
      this.setState({
        jsonList:json
      });
     })
     .catch(error => console.log(error));*/
    fetchInfo();
   }


 handleChange  (selectedOption) {
    this.setState({
         selectedOption: selectedOption ? selectedOption:''
    });
		// selectedOption can be null when the `x` (close) button is clicked

		/*if (selectedOption) {
    	console.log(`Selected: ${selectedOption.label}`);
		}*/
  }

 handleClick(){
   /*'setState' es un metodo por el cul se pueden acceder y cmabiar las variables de estado del DOM*/
     this.setState({
       user_name:'Ricardo Machorro',
       profesion:'Web Tester'
     });
 }


  render() {

    console.log(this.props.info);

    /*En esta parte se pasan los elementos del state a una constante que
    se podra usar en todo el Render*/
   const {array2}=this.state


   /*Para poder convertir el array json de un a una estructura apta para el elemento select  */
    const selectList=this.props.info.map(json=>{
      return {value:json.name,label:json.name}
    });

    return (

      <div>
            {/*Para poder usar los elementos se usan como cualquier otro*/}
            <Navbar inverse collapseOnSelec>
            <Navbar.Header>
              <Navbar.Brand>
                <a href="#home">Rick@com</a>
              </Navbar.Brand>
            </Navbar.Header>
            <Nav>
              <NavItem eventKey={1} href="#">
                Link
              </NavItem>
              <NavItem eventKey={2} href="#">
                Link
              </NavItem>
              <NavDropdown eventKey={3} title="Dropdown" id="basic-nav-dropdown">
                <MenuItem eventKey={3.1}>Action</MenuItem>
                <MenuItem eventKey={3.2}>Another action</MenuItem>
                <MenuItem eventKey={3.3}>Something else here</MenuItem>
                <MenuItem divider />
                <MenuItem eventKey={3.4}>Separated link</MenuItem>
              </NavDropdown>
            </Nav>
              <Nav pullRight>
              <NavItem eventKey={1} href="#">
                Link Right
              </NavItem>
              <NavItem eventKey={2} href="#">
                Link Right
              </NavItem>
            </Nav>
      </Navbar>;
            <div className="container">
              <div className="row">
                <div className="col-sm-12">
                  <h1>Mi pagina web</h1>
                  <p>por ricardo</p>
                </div>

              </div>
            </div>
            <div>
              <div className="row">
                <div className="col-sm-3">
                  <Select
                     name="form-field-name"
                     value={this.state.selectedOption.value}
                     onChange={this.handleChange.bind(this)}
                     options={selectList}

                   />{/*Aqui se llena el componente Select con  el Array selectList ya en un formato para el selet*/}
                </div>
              </div>

             <hr></hr>


             <Table striped bordered condensed hover>
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Address</th>
                  <th>Age</th>
                  <th>Company</th>
                </tr>
              </thead>
              <tbody>
                {this.props.info.map(item=>{
                  if(item.name===this.state.selectedOption.value || item.name==="")
                  return(
                      <tr>
                      <td>{item.name}</td>
                      <td>{item.address}</td>
                      <td>{item.age}</td>
                      <td>{item.company}</td>
                    </tr>
                  )
                })}
              </tbody>
            </Table>


            </div>
      </div>
    );
  }
}

const mapStateToProps= state =>{
  return state;
}

const App = connect(mapStateToProps)(AppComponent);

export default App;
