#Un tipo de dato en python son las listas que permite almecanr datos repetidos
#y de diferente forma

#Para declarar una lista se pone despues d ela asignacion y el nombre los simbolos
# " [] " y  despues se le pone el contenido

#un ejemplo de esto es:
list=[12,12,30,"Hola",13.4]
print(list)
#como en un string se puede seleccionar cierta seccion de esta

#Para seleccionar solo un elemento
print(list[2])

#Para seleccionar una porcion de esta
print(list[1:4])

#Para imprimir la list cierto numero de veces
print(list*3)

#Para imprimir el tamaño de la lista
print(len(list))

#tambien a una lista se le puede agregar un elemento al final con la funcion append como
#en ejemplo:
list.append("Rick")
print(list)
