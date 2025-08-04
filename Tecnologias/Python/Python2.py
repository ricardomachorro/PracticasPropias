"""Python tambien puede tener datos ordenados en colecciones dentro
de estas colecciones estan :
  Listas:Es una coleccion de elementos que permite repeticion de elementos
  Sets:Es un coleccion de elementos que no permite la repeticion de elementos
  Diccionarios: Es una coleccion de elemtnos en pares con un elemento siendo considrrado
  como la llave o idnetificador a cierto elemento
"""
#Uno de estas listas son los string o conjunto de letras

#Los string se declaran con entrecomilas " " o con comillas simples ' '
a = "Hola a todos"
print(a)
"""Si se quiere usar string que repete los saltos de linea se les ponen entre
   comillas dobles triples """
b = """Respetas
los
espacios"""
print(b)
#tambien se puede selccionar que letra especifica poniendo el nombre de la variables
# y luego poner en ella los signos " [] " y dentro de estos el numero de la posicion de
# la letra que se requiere empezando desde el cero
print(a[0])
print(a[3])
#Para repetir un texto se usa despues de esta el signo " * " seguido del numero
#de veces que se va a repetir
print(a*2)
print(a*4)
print(a[0]*2)
print(a[0]*4)
#Para obtener el numero de elementos de una coleccion se usa len, que en el caso
# de un string regresa el numero de letras
c="a"
print(len(b))
print(len(c))
#Para imprimir cierto rango de un string se usa usa lo mismo que en un solo caracter
#excepto que en vez de poner solo un numero se pone un numero de donde se inicia
#seguido de dos puntos y luego el numero del final mas uno ejemplo: [0:4]
print(a)
print(a[2:6])
#si no se pone el primer digito lo imprime desde el inicio hasta el numero final
print(a[:6])
#si no se pone el ultimo digito lo imprime desde el numero asignado hasta el final
print(a[2:])
#tambien se puede hecer con simbolos negativos
print(a[-4:-1])
#Tambien se puede imprimir en saltos poniendo al final dos puntos y el numero de saltos
d = "Bienvenidos todos"
print(d[1:11:2])
#Tambien se puede dar salto en reversa con numeros negativos
print(d[::-1])
#Una forma de quitar los espacios inecesrios es con ls funcio strip
e = "  Hola    a    Todos    "
print(e.strip())
#Otras funciones con string son:

#find la cual encuentra la posicion de un subcadena y si no la encuentra da -1
print(d.find("ien",1,len(d)))
#count cuenta el numero de subcadenas a encontrar
print(d.count("e"))
#replace remplaza una subcadena por Otra
print(d.replace("en","yeah"))
#pasa a minusculas toda la cadena
print(d.lower())
#pasa a mayusculas toda la cadena
print(d.upper())
#pasa solo las primeras letras de cada palabra a mayusculas
print(d.title())
