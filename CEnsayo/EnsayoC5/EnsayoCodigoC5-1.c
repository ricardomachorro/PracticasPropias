#include<stdio.h>

int main(){

/*Una forma de evaluar  condicionales verdaderas y falsas  de manera sencilla con
pseudocodigo de la forma: condicion a evaluar ? pasos_si_es_verdadero : pasos_si_es_falso*/

int  x=34,y=24;

printf("%i, %i\n", 1 ? x : y, 0 ? x : y);
/*Este es muy util un ejemplo de este es de poder imprimir el mayor de 3 numeros*/
int big=0,a=4,b=12,c=7;
big= a > b ? (a > c ? a : c): (b > c ? b : c);
printf("\n%i",big);


 return 0;
}
