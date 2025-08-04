#include<stdio.h>
#include<math.h>/*Esta es la libreria para elementos matematicos*/

void main(){
  float n1,n2,suma=0,resta=0,multi=0,divi=0,hipo=0,cat1=0,cat2=0,baseMa,baseMe,alturaTra,areaTr;

  char variableUsuario1[70];
  printf("Escribe tu nombre \n");
    /*Para poder  leer un string de usuario con todo y espacios se hace con gets(variable_asignar)*/
  gets(variableUsuario1);
  printf("La variable es: %s \n", variableUsuario1);
  printf("Operaciones suma, ponga dos numeros\n");
  printf("Oprima el primero:\n");
  scanf("%f",&n1);
  printf("El segundo seria \n");
  scanf("%f",&n2);
  suma= n1+n2;
  resta=n1-n2;
  multi=n1*n2;
  divi=n1/n2;
  printf("La suma es : %.3f \n", suma );
  printf("La resta es : %.3f \n",resta);
  printf("La multiplicacion es: %.3f \n", multi);
  printf("La division es: %.3f \n",divi);
  printf("\n Ejercicio calculo de hipotenusa por catetos:");
  printf("\n Escriba el primer cateto:");
  scanf("%f",&cat1);
  printf("\n Escriba el segundo cateto:");
  scanf("%f",&cat2);
  /*Para poder elevar elementos a una cierta potencia se usa ' pow(base,potencia) ',
  y para sacar la raiz cuadrada se usa ' sqrt(numero)  ''*/
  hipo=sqrt(pow(cat1,2)+pow(cat2,2));
  printf("\n La hipotenusa es: %.2f", hipo);
  printf("\n Ejercicio de area de Trapecio:");
  printf("\n Escriba la base Mayor:");
  scanf("%f", &baseMa);
  printf("\n Escriba base menor:");
  scanf("%f",&baseMe);
  printf("\n Escriba La altura:");
  scanf("%f",&alturaTra);
  areaTr=((baseMa+baseMe)/2)*alturaTra;
  printf("\n El area es: %f", areaTr);
  float TotalCompra,descuento,precio;
  printf("\n Ejercicio  de descuento del 15 porciento de descuento por un total de compra");
  printf("\n Teclee el total de compra : \n");
  scanf("%f", &TotalCompra);
  descuento=TotalCompra*.15;
  precio=TotalCompra-descuento;
   printf("\n El total de compra es %.2f:",precio );

}
