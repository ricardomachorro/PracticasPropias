<!--Para crear un template el archivo simepre debe terminar en ".vue"-->
<!--Esta es una template de otro elemento de la App que funciona parecidos -->

<!--En esta parte del template  se ponen todos los elementos que vendran en la app final
ademas que aqui se vera toda la parte hecha para la aprte en html-->
<template>
   <div class="container">
      <p>Hello</p>
      <br/>


      <br/>
      <table class="table table-striped mt-4">
        <thead>
          <tr>
            <th scope="col">Id</th>
            <th scope="col">Title</th>
            <th scope="col">Body</th>

          </tr>
        </thead>
        <tbody>
          <!--Un ejemplo de usar 'v-for:''-->
          <tr v-for="post in posts" :key="post.id">
            <th scope="row"></th>
            <td>{{post.id}}</td>
            <td>{{post.title}}</td>
            <td>{{post.body}}</td>
          </tr>

        </tbody>
      </table>
      <br/>
      <table class="table table-striped mt-4">
        <thead>
          <tr>
            <th scope="col">User Id</th>
            <th scope="col"> Id</th>
            <th scope="col">Title</th>
            <th scope="col">Body</th>

          </tr>
        </thead>
        <tbody>
          <!--Un ejemplo de usar 'v-for:''-->
          <tr v-for="post in posts2" :key="post.id">
            <th scope="row"></th>
            <td>{{post.id}}</td>
            <td>{{post.title}}</td>
            <td>{{post.body}}</td>
          </tr>

        </tbody>
      </table>

      <button class="btn btn-primary">button</button>
   </div>
</template>

<!--Esta parte es para las funciones en javascript-->
<script>

 /*Todas las templates tienen la estructura de export

  default{

    contenido

    return{

  }

}
*/

/*axios es un libreria especial de js para poder manejar objetos asincronos
con promesas para poder instalarla se usa ' npm install axios ' en la linea de comandos,
ademas  y para usarlo  se usa  ' import axios from 'axios' ' */

import axios from 'axios'

  export default{
      name:'PostExample',/*<==A todo elemento de una App en Vue hay que darle un nombre esto con el parametro
      "name :'nombre_elementoVue'"*/
      data(){ /*Esto da los parametros dados en el elemento*/
           return{ /*<== El ' return ' e spor el hecho de que este regresa un objeto*/


              posts:[
                {id:1,title:'Post1',body:'Body1'},
                {id:2,title:'Post2',body:'Body2'},
                {id:3,title:'Post3',body:'Body3'},
                {id:4,title:'Post4',body:'Body4'},
                {id:5,title:'Post5',body:'Body5'},
              ],
              posts2:[]
           }
      },
      /*Creted es lo que se hace cuando se carga un componente vue, todo es parte del ciclo de vida de un
      componente Vue, esto se puede ver mas en el LifeCycle de la documentacion de Vue.js*/
      created(){
        /*Aqui ahy un ejemplo del uso de axios con get */
          axios.get("https://jsonplaceholder.typicode.com/posts").then( post=>{
            this.posts2=post.data
          }

          );
      }
  }
</script>

<!--Aqui se ponen los elementos de css-->
<style>
</style>
