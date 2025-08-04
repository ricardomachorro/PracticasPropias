#include<stdio.h>
#include<stdbool.h>/*Libreria para poder usat valorer booleanos*/
#include<string.h>/*Libreria para poder usar strings */

int main(){
  /*Para usar elementos del tipo binario en C por default se usa la estructura y declaracion de
  la siguiente forma:
  bool x=1; <==Verdadero
  bool y=0; <==Falso

  ademas de usar la libreria " stdbool.h "
  */

  bool x=1;
  bool y=0;

  if(x){
    printf("X es positivo \n");
  }
  if(!y){
    printf("Y es negativo \n");
  }

  /*Aparte de esto tambien se usa _Bool que se puede usar para poder tener usar datos
  booleanos */

  _Bool w=1;
  _Bool z=0;

  if(w){
    printf("W es positivo \n");
  }
  if(!z){
    printf("Z es negativo \n");
  }

  /*la función  strtok rompe caracteres de un string en otros mas pequeños por medio de
  delimitadores   */

  int toknum = 0;
   char src[] = "Hello,, world!";/*Esta es una forma declarar un String */
   const char delimiters[] = ",!";/*Estos son los delimitdores que separan el String*/
   char *token = strtok(src, delimiters);/*Este en realidad regresa el espacio de memoria donde esta ubicado el string
   ademas de remplezar los valores delimitdores con " /0" que al ser interpetados los toma como si el String hubiera
   terminado */
   while (token != NULL)
   {
   printf("%d: [%s]\n", ++toknum, token);/*Al ser impreso el string  por tener " /0"  en los elemenots donde antes habia delimitantes
   este los toma como el fin de estos */
   token = strtok(NULL, delimiters);/*Para la transformacion de esto se usa de la siguiente manera , pro el hecho de la funcion
    strtok no hace que el char token no almacena los cambios afuera del while*/

   }

   /*Una forma de poder tener tener el tamaño de un Strig es con la funcion ' strlen()  '*/

   char nombre[]="Ricardo";

  printf("El size de Ricardo es :%d \n", strlen(nombre));
  /*Una de las caracterisiticas  de los Strings es que estos no se pueden copiar como otro datos primitivos
   como int,double o floats, con el operador de asignacion ( = ) ya que esto solo hara que se copie la direccion de
   almacenamiento , para esto se usa funciones como strcpy()
   */

   char banda1[]="Green Day";
   char banda2[30];
   strcpy(banda2,banda1);
    printf("Las bandas son %s , %s \n", banda1,banda2);

    /*Otra  forma de copiar Strings limpiando el biffer de memoria  se usa la funcion ' snprintf() '*/

    char banda3[]="Maroon 5";
    char banda4[30];
    strcpy(banda4,banda3);
     printf("Las bandas son %s , %s \n", banda3,banda4);


  return 0;
}
