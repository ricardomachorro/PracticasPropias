#include<stdio.h>

int main(){
   int numero;
   char vocal;
   printf("Teclee un numero de (1-3)\n");
   /*Un if en C++ y C se usa solo ints, Strings o chars*/
   scanf("%i",&numero);
   switch(numero){
       case 1:
         printf("Eligio el numero 1");
      break;
      case 2:
         printf("Eligio el numero 2");
      break;
      case 3:
         printf("Eligio el numero 3");
      break;
      default:
        printf("Eliga un numero entre 1-3");
      break;
   }
  fflush(stdin);/*Es importante recordar de no olvidar el comando fflush(stdin) para limpiar la memoria*/
   printf("\n Ahora teclee una vocal\n" );
   scanf("%c",&vocal);
   switch(vocal){
     case 'a':
     printf("Escribio a\n");
     break;
     case 'e':
     printf("Escribio e\n");
     break;
     case 'i':
     printf("Escribio i\n");
     break;
     case 'o':
     printf("Escribio o\n");
     break;
     case 'u':
     printf("Escribio u\n");
     break;
     default:
     printf("Escriba una vocal\n");
     break;
   }



  return 0;
}
