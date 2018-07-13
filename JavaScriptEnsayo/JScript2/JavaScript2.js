/*Para poder declaración de varaibles en javascript se usa la palabra
reservada ' var  ' y la asignación de la variable es:
'   var nombre_variable="valor_variable"  '

   ---Nota:Esto no indica el tipo de dato que sera la variable
*/
var variable1="Hello boy";
var variable2="Hello again";
document.write(variable1);
/*tambien se puede usar ' document.write();  ' para escribir etiquetas html*/
document.write("<br/>");
document.write(variable2);

/*Tmabien se puede declarar variables sin la palabra reservada ' var ' aunque esta es una mala practica*/
variable3="Hello you";

/*Tambien se puede declarar varias variables a la vez*/
var x,y,z;
x=10;
y=35;
z=23;
document.write("<br/>");
document.write("Los numeros son: "+x+","+y+","+z);

/* Hay palabras reservadas para la declaracion de variables, las cuales son:

 -var  ejemplo: var var="Hola";
 -with  ejemplo: var youwithme:"Hola";
 -%     ejemplo: var variable1&:"Hola";
 -&     ejemplo: var you&me:"Hola";
 -iniciar con numeros   ejemplo: var 66order:"Hola";

*/

/*JavaScript es un lenguaje de CaseSensitive es decir que diferencia entre variables,funciones,
eventos, etc.. con nombres iguales,pero con diferentes letras*/

var firstName="Ricardo";

var firstname="Rick";
document.write("<br/>");
document.write("Variable numero1: "+firstName);
document.write("<br/>");
document.write("Variable numero2: "+ firstname);

/*Un estandar en programación en la declaración de variables es la d eponer el primer nombre
 con todo minusculas y los siguiente nombres con Mayusculas

 ejemplo:

   -myFirstname
   -stateOf
 */

/* Las operaciones basicas  en javascript son:
   @ la suma: +
   @ la resta: -
   @ la mmultiplicacion: *
   @ la division: /
   @ modulus: %
   @ incrementos: ++
   @ decrementos: --
*/
 var a=10,b=34;

var suma=a+b,resta=a-b,multi=a*b;div=a/b,modu=a%b;

/*Suma*/
document.write("<br/>");
document.write("Suma:");
document.write(a+"+"+b+"="+suma);

/*Resta*/
document.write("<br/>");
document.write("Resta:");
document.write(a+"-"+b+"="+resta);

/*Multiplicacion*/
document.write("<br/>");
document.write("Multiplicacion:");
document.write(a+"*"+b+"="+multi);

/*Division*/
document.write("<br/>");
document.write("Division:");
document.write(a+"/"+b+"="+div);

/*Modulo*/
document.write("<br/>");
document.write("Modulo:");
document.write(a+"%"+b+"="+modu);

/*Incrementos*/
document.write("<br/>");
a++;
document.write("Incrementos:" +a);

/*Decrementos*/
document.write("<br/>");
b--;
document.write("Incrementos:" +b);


/* Operadores de asignacion

 Operador:

 @ =
 @ +=
 @ -=
 @ *=
 @



*/
