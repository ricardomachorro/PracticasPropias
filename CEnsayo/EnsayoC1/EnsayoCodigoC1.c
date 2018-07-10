/*asi se importan librerias usando "#include<nombre_libreria>" en exte caso para imprimir texto en pantalla se
importar  se usa "#include<stdio.h>"  */
#include<stdio.h>

/*Si se quiere usar una varibale cuyo valor no va variar durante
todo momento se usa "#define nombre_variable valor_vaiable"*/
#define PI 3.1416

/*Esta es una variable global  es decir que solo se puede usar dentro de todo el script*/
int y=30;

/*Todo programa en C necesita un metodo main que se hace con el metodo main */
void main(){

  /*Esta es una variable local es decir que solo se puede usar dentro de la funcion
  en la que esta*/
  int x=10;

  /*Para imprimir texto se usa "printf('texto_a_imprimir');"*/
  /*Pra imprimri un salto de linea se ase con  "printf('\n');"*/
  printf("Hello Word\n");
  printf("Hello Word\n");

   /*Asi se asigna una variable*/
  int suma=x+PI;

  /*Para poder imprimir en pantalla un valor que no sea Sting es con 'printf("valor_string %tipo_de_valor ", valor);'*/
  printf("La suma de PI y x es:  %i \n",suma);

  float sumareal=x+PI;
  printf("La suma real de PI y x es %f",sumareal);

  /*Para poder controlar el numero de decimales que imprime el programa se usa esta estructura
  printf("mensaje %.numero_de_decimales+f", valor_a_imprimir) */
  printf("La suma de 2 deciamles de PI y x es %.3f \n",sumareal);


/*Aqui hay otras formas de imprimir otros tipos de datos*/

/* En caso del char*/
 char caracter='r';/* tamaño=1 byte Rango:0-255*/
 printf("Caracter unico %c \n", caracter);

 /*En caso del short*/
 short ejemploshort=-23;/*tamaño=2 bytes Rango: -128 - 127  */
 printf("Ejemplo de short %i \n", ejemploshort);

/*En caso del int*/
int ejemploint=1024;/*tamaño=2 bytes Rango:-32768 - 32767 */
printf("Ejemplo de int %i \n",ejemploint);

/*En caso de unsigned int  Nota:Para un unsigned int solo se aceptan numeros positivos*/
unsigned int ejemploIntpositivo=128;/*tamaño=2 bytes Rango 0-65535*/
printf("Ejemplo de int unsigned %i \n", ejemploIntpositivo);

/*En caso del long*/
long ejemploLong=123456;/*tamaño=4 bytes*/
printf("Ejemplo  de un long %li \n", ejemploLong);

/*En caso de float*/
float ejemploFloat=15.678;/*tamaño=4 bytes*/
printf("Ejemplo de un float %f \n",ejemploFloat);

/*En caso de double*/
double ejmploDouble=123123.123123;
printf("Ejemplo de un double %d \n", ejmploDouble);


/*Para poder desplegar muchos valores de diferente tipo se hace de la siguiente forma
 '  printf(" %tipo_de_dato1, %tipo_de_dato2, %tipo_de_dato2",dato1,dato2,dato3 )  '*/

 char dato1='a';
 int dato2=23;
 double dato3=15.4;

 printf("%c %i %d \n",dato1,dato2,dato3);

 /*Para poder leer los datos del usuario se hace con ' scanf ("tipo_de_dato",&variable_asignar)'*/
 int variableUsuario1;
 float variableUsuario2;
 char variableUsuario3;

printf("Escriba un numero: \n");
scanf("%i", &variableUsuario1);
printf("variable usuario 1: %i\n",  variableUsuario1);
printf("Ahora escriba un numero decimal:  \n");
scanf("%f",&variableUsuario2);
printf("La variable de usuario 2 es: %.3f \n", variableUsuario2);
/*Para poder ingresar elementos como palabras completa se hace se hace por medio de un char
 en forma de vector*/
char variableString1[50];

printf("La varibale String de usuario \n");
/*Para poder asignar el string sin espacios  se hace con 'scanf("%s", variable_asignada);' ya que scanf  registra
hasta que encuentra un espacio*/
scanf("%s", variableString1);

/*Para poder imprimir la variable de String  se hace con 'printf(" %s",variable_String)'*/
printf("La variable de String es: %s\n",variableString1 );

}
