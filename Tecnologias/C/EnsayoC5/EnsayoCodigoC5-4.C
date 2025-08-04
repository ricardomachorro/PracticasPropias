#include<stdio.h>

int main(){

  int contador=1,numero,resultado;
  printf("Digit un numero: \n");
  scanf("%i",&numero);
  if(numero>=10){
    while (contador<=numero){
      resultado=1;
      resultado*=contador;
    }
  }else{
    while (contador<=numero){
      resultado=0;
      resultado+=contador;
    }
  }

  printf("El resultado es %d: ", resultado);
  return 0;
}
