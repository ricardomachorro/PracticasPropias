#Una Tupla en python es como una lista pero sin ser posible modificar esta
#Osea una coleccion de elementos fijos

#Para declar una tupla en python se hace con los simbolos
# "  ()  "

#Nota: Si una tupla solo contiene un elemento para diferecir este de un string o
#un integer, se pone despues de este elemento una coma " ,"

#un ejemplo de una tupla:
tupla=(1,34,24,"Rick",12,12)
print(tupla)
#al igual que una lista una tupla se puede seleccionar un elemento
#con poniendo al final " [i] " sinedo i el indice del elemento a seleccionar
print(tupla[2])
#tambien se puede repetir la tupla un numero de veces con " * "
print(tupla*4)
#tambien se puede contar el numero de elementos que encaguen en cierta descripcion
#con la funcion " count "
print(tupla.count(12))
#tambien se puede ver ele indice de un elemento con la funcion index
print(tupla.index("Rick"))
