/*
Condicionales con Operadores

Operador         Significado

==                 igual a
===                igual a y del mismo tipo de dato
!=                 no igual
!==                no igual o del mismo tipo de dato
>                  mas grande
<                  menor que
>=                 igual o mas grande
<=                 igual o menor que

*/

var student=18,studentheight=34;

if(student==18){

  document.write("La edad del alumno es 18  <br/>");
}

if(student===18){
  document.write("La edad y tipo del alumno es 18 <br/>");
}

if(studentheight!=35){
  document.write("No tiene la altura necesaria <br/>");
}

if(studentheight!=="34"){
  document.write("No tiene la altura necesaria, ni el dato correcto <br/>");
}
