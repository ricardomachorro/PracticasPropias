/*Condicionales con operadores logicos*/

/*
Operadores logicos

   Operador       Significado
  -----------     -------------
     &&               and
     ||                or
      !                negacion
*/


var studentAge=18;
var studentGenedar="M";

if((studentAge >=18) && (studentGenedar=="M")){
    document.write("La edad del alumno es mas que 18  y es hombre");
}
 document.write("<br/>");
if((studentAge >=18) || (studentGenedar=="M")){
    document.write("La edad del alumno es mas que 18  y/o es hombre");
}
document.write("<br/>");
if(studentAge!=18){
  document.write("El alumno es mayor de edad");
}else{
  document.write("El alumno es menor de edad");
}
