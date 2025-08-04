#include <stdio.h>

/*Ejercicio resta de pares y suma de impares hasta cierto numero*/
int main(){
    int suma=0,numero,contador=1;
    printf("Digite el numero:");
    scanf("%i",&numero);
    while(contador<=numero){
     contador%2==0 ? (suma-=contador):(suma+=contador);

      contador++;
    }
    printf("La suma es igual  %i \n", suma);



  return 0;
}
