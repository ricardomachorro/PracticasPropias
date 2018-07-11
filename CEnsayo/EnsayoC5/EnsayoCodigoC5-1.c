#include<stdio.h>
#include <stdlib.h>

int main(){

/*Una forma de evaluar  condicionales verdaderas y falsas  de manera sencilla con
pseudocodigo de la forma: condicion a evaluar ? pasos_si_es_verdadero : pasos_si_es_falso*/

int  x=34,y=24;

printf("%i, %i\n", 1 ? x : y, 0 ? x : y);
/*Este es muy util un ejemplo de este es de poder imprimir el mayor de 3 numeros*/
int big=0,a=4,b=12,c=7;
big= a > b ? (a > c ? a : c): (b > c ? b : c);
printf("\n%i",big);

/*Unos operandos especiales son loas Bitwise u Operadoes de Bits los cuales son:

& bitwise AND
| bitwise inclusive OR
^ bitwise exclusive OR (XOR)
~ bitwise not (one's complement)
<< logical left shift
>> logical right shift

*/

/*Un ejemplo  de como afectan estos operadores es de la siguinte forma:*/

unsigned int a1 = 29; /* 29 = 0001 1101   <====Nota: Es unsigned para asi evitar problemas con
 el signo que hace tener un bit de mas
*/
unsigned int b1 = 48; /* 48 = 0011 0000 */
 int c1 = 0;

/**/

 c1 = a1 & b1;/* 32 = 0001 0000 */
 printf("%d & %d = %d\n", a1, b1, c1 );
 c1 = a1 | b1; /* 61 = 0011 1101 */
 printf("%d | %d = %d\n", a1, b1, c1 );
 c1 = a1 ^ b1; /* 45 = 0010 1101 */
 printf("%d ^ %d = %d\n", a1, b1, c1 );
 c1 = ~a1; /* -30 = 1110 0010 */
 printf("~%d = %d\n", a1, c1 );
 c1 = a1 << 2; /* 116 = 0111 0100 */
 printf("%d << 2 = %d\n", a1, c1 );
 c1 = a1 >> 2; /* 7 = 0000 0111 */
 printf("%d >> 2 = %d\n", a1, c1 );

 /*Otra forma de poder el ' printf() ' es con secuencias de escape de la siguiente forma:

 \a <=====  caracter de alarma (Es decir que este hace sonido)
 \b <====   caracter de retroceso
 \f <====   caracter de avance de hoja
 \t <==== caracer de tabular horizontal
 */

 printf("\a Hola \n");//<===Hace sonido


return 0;
}
