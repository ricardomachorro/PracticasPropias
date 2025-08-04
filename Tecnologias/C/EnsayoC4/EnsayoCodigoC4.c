#include<stdio.h>
#include<stdlib.h>

int main(){

   char codigo;

   printf("Borrar pantalla");
   printf("\n-------------------------------\n");
   printf("\n-------------------------------\n");
   printf("\n-------------------------------\n");
   printf("\n Digite el numero 1:\n");
   scanf("%c",&codigo);
   if(codigo=='1'){
     /*Para limpiar la pantalla se usa ' system("cls") ' ,esto es porque cls significa clear screem*/
     system("cls");
     printf("\nHa funcionado" );
   }else{
     fflush(stdin);/*Para limpiar el valor que tiene un dato osea el buffer se tiene que usar el
     el comando   '  fflush(stdin)  '*/
     printf("\nNo funciono");
     printf("\nDigite uno por favor:\n");
     scanf("%c",&codigo);
     if(codigo=='1'){
       system("cls");
       printf("\nFunciono");
     }else{
         printf("\nNo funciono");
     }

   }

  return 0;
}
