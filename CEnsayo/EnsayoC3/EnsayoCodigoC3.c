#include<stdio.h>

int main(){
  /*Ejercicio sentencia if-else*/
  float nota;
  printf("Ejercicio if-else   ");

  printf("\nDigite la nota del examen:");
  scanf("%f",&nota);
  if(nota>6){
    /*Los puts es una forma de imprimir datos dentor de los condicionales */
    puts("El alumno aprobo");
  }else{
    puts("El alumno reprobo");
  }
  char  nombre[30],signo[20];
  printf("Ejercicio Aries \n");
  printf("\nEscriba su nombre:\n");
  scanf("%s",&nombre);
  printf("\nEscriba su signo zodiacal\n");
  scanf("%s",&signo);
  printf("\nFunciona");
  printf("\n Tu nombre es: %s y tu signo es: %s ",nombre,signo);
  /*Una forma de comparar cadenas de string son iguales ' strcmp(cadena1,cadena2)'
    esta funcion regresa uno por si las cadenas son iguales  regresa 0, si es contrario  regresa 1
  */
  if(strcmp("aries",signo)==0){
       printf("\nEres Aries\n");
  }else{
       printf("\nNo eres Aries\n");
  }
  return 0;
}
