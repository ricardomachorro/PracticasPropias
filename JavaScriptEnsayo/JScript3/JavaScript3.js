/*Condicionales */

/*Los condicionales tipicos  son if, else, else if*/
var temperatura=100;

/*Con if*/
if(temperatura==100){

  temperatura-=20;
  document.write("La temperatura actual es: "+ temperatura + "</br>");

}else if(temperatura==10){
   temperatura-=10;
  document.write("La temperatura actual es:"+ temperatura+"<br/>");
}else{
  document.write("La temperatura actual es:"+ temperatura+"<br/>");
}

/*Los condicionales se pueden tambien poner en las asignaciones con los condicionales de javascript*/

var temperaturaActual=(temperatura==100) ? temperatura-20:temperatura-10;

document.write(" La temperatura normal es: "+ temperatura + "<br/>");

document.write("La temperaturaActual es: "+ temperaturaActual +"<br/>")
