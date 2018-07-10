#include <stdio.h>

int main(){

   int opcion;
   float monto,saldo=100;

   printf("\tBienvenido al cajero virtual");
   printf("\n1. Ingreso cuenta");
   printf("\n2. Retirar dinero de la cuenta");
   printf("\n3. Salir");
   printf("\nOpcion:");
   scanf("%i",&opcion);

   switch(opcion){
     case 1:

     printf("\n Cuanto dinero quiere agregar:\n");
     scanf("%f",&monto);
     saldo+=monto;
     printf("\nEl saldo total es de: %.2f",saldo);

     break;

     case 2:

     printf("\n Cuanto dinero quiere retirar:\n");
     scanf("%f",&monto);
     if(monto>saldo){
       printf("\nSaldo insuficiente");
     }else{
       saldo-=monto;
       printf("El saldo total es de: %.2f",saldo);
     }


     break;

     case 3:

     printf("\n Gracias por su visita");

     break;

     default:

     printf("\n Opccion equivicada");

     break;
   }

  return 0;
}
