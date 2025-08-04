#include<stdio.h>

int main(){
/*Ejercicio suma de n primeros numeros- factorial n numeros*/

int contador=1, numeros,suma=0;

   printf("Escribe el total de numeros a sumar: \n");
   scanf("%i",&numeros);

   while(contador<=numeros ){
     suma+=contador;
     contador++;
   }

  printf("La suma o factorial es: %d", suma );


  return 0;
}
