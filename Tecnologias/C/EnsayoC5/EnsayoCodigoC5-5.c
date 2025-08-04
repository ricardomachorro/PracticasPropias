#include<stdio.h>


/*Ejercicio encontrar multiplos de 3*/
int main(){


   int numero,contador=1;
   char multiplos[]="";

   printf("Escriba hasta que numero sera la comparacion : \n");
   scanf("%i",&numero);

   while(contador<=numero){
     if(contador%3==0){
      printf("%i \n",contador );
     }
     contador++;
   }
   //printf("Los multiplos de 3 del 1 al %d son: %s",numero,multiplos);

  return 0;
}
