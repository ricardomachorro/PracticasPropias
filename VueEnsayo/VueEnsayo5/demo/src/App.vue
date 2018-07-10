
<!--En esta parte del template Principal se ponen todos los elementos que vendran en la app final
ademas que aqui se vera toda la parte hecha para la parte en html-->
<template>

  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <router-link class="nav-link" :to="'/'" >Contact</router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link" :to="'/Contact'" >Contact</router-link>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#">Disabled</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
    <router-view></router-view>
  </div>
</template>

<!--Esta parte es para las funciones en javascript-->
<script>
/*Aqui se dan las importaciones de los demas elementos que se utilizaran*/
import HelloWorld from './components/HelloWorld'
import PostExample from './components/Posts'
import Contact from './components/Contact'

export default {
  name: 'App',/*Aqui sera el nombre con el cual todo el template Principal para ser pasada a otras partes de la App */
  components: {
    HelloWorld,/*Aqui se ponen todos los componentes que se usaran en la parte html-template */
    PostExample,
    Contact
  }
}
</script>

<!--Aqui se ponen los elementos de css-->
<style>
   /*Aqui se importa la parte de css y bootstrap*/
   @import "../node_modules/bootstrap/dist/css/bootstrap.min.css";


</style>
