#import <stdio.h>

/*Ejercico de Nota por medio de switch*/
int main(){
   char nota;

   printf(" Digite  su nota:\n ");
   scanf("%c",&nota);
   switch(nota){

      case 'A':
         printf("\nExcelente");
      break;

      case 'B':
         printf("\nNotable");
      break;

      case 'C':
         printf("\nPasable");
      break;

      case 'F':
         printf("\nReprobado");
      break;

      default:
        printf("\nNota no reconocida");
      break;

   }

  return 0;
}
