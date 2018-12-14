#Un tipo de dato en python son las listas que permite almecanr datos repetidos
#y de diferente forma

#Para declarar una lista se pone despues d ela asignacion y el nombre los simbolos
# " [] " y  despues se le pone el contenido

#Nota: Si una lista solo contiene un elemento para diferecir este de un string o
#un integer, se pone despues de este elemento una coma " ,"


#un ejemplo de esto es:
list=[12,12,30,"Hola",13.4,127,1]
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

#A una lista se le puede agregar un elemento al final con la funcion append como
#en ejemplo:
list.append("Rick")
print(list)

#tambien a una lista se le puede agregar un elemento en una posicion especifica con
#la funcion insert como en el ejemplo:
list.insert(3,"Dan")
print(list)

#tambien se puede eliminar elementos una forma es con remove y el elemento a eliminar:
list.remove(30)
print(list)
#otra forma es con la funcion " del " y el  elemento a eliminar:
del(list[4])
print(list)
list2=[12,30,13.4,127,1]
#Tambien se puede seleccionar el minimo y maximo numericos de una lista
#para el maximo se usa la  funcion max
print(max(list2))
#para el minimo se usa la  funcion min
print(min(list2))
#para ordenar elementos numericos de menor a mayor,en una lista se hace son la funcion sort
list2.sort()
print(list2)
#para ordenar elemntos numericos de mayor a menor,en una lista se hace son la funcion sort
#y poner como parametro " reverse=True "
list2.sort(reverse=True)
print(list2)
