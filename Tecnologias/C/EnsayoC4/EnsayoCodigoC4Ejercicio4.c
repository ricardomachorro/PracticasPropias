#include <stdio.h>

int main(){

  /*Una forma de usar condicionales simples  con ' ? ' , la estrucutra de estos condicionales es la siguiente

' (parametro o condicion a evaluar) ? acciones_si_es_cierta : acciones_si_no_es_cierta '*/
/*En rl rjmplo siguiente se usa el de reconocer si un numero inresado es primo*/
int numero;
  printf("  Ejercicio de  Par e Impar \n  ");

  printf(" Escriba un numero \n");

  scanf("%i",&numero);

  (numero%2==0) ? printf("Es un numero par\n") : printf("Es un numero impar\n");

  return 0;
}
