// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import VueRouter from 'vue-router';
import Posts from './components/Posts.vue';
import Contact from './components/Contact.vue';


Vue.config.productionTip = false

Vue.use(VueRouter);

const routes=[
  {  path:"/",component:Posts},
  {path:"/Contact", component:Contact}

];

const router=new VueRouter({routes:routes});

/* eslint-disable no-new */
new Vue({
  el: '#app',/*Este identifica que elemnto va a recibir los templates que tendra la App principal ("index.html")*/
  components: { App },/*Aqui indica los componentes de que tendra la App principal ("index.html")*/
  template: '<App/>',/*Aqui se denota el componente-template*/
  router
})
