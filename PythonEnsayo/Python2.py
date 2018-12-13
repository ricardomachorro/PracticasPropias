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
