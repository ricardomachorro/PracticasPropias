#include <stdio.h>

int main(){
  char nombre[30];
  printf("Hola me llamo:\n");
  gets(nombre);
  printf("Mi nombre es:%s \n",nombre);
  int num;
  printf("Escribe tu edad \n");
  scanf("%d",&num);
  printf("Tu edad es %d",num);
  return 0;
}
