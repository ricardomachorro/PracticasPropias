#Otro tipo de dato  en python son los diccionarios estos a diferencia de los diferentes
#datos en conjunto tienen llaves acompañadas de los elementos a guardar

#Para declar diccionario se hace de la siguiente forma:
dict1={1:"John",2:"Bob",3:"Tree"}
print(dict1)
print(type(dict1))

#Con la funcion " items " se muestra los elementos mas las llaves de todos los elementos del diccionario
print(dict1.items())

#Para solo tener las llaves se usa la funcion " keys ", esta funcion regresa un dato range

k = dict1.keys()

for i in k:
    print(i)

print("////////////////")
#Para solo tener los elementos se usa la funcion " values ", esta funcion regresa un dato range
j = dict1.values()

for i in j:
    print(i)
print("////////////////")
#Para obtner solo un elemento en un diccionario se hace como si fuera un string, en vez de una posicion se
#usa las llavces de los elementos
print(dict1[2])
print("////////////////")

#Para eliminar elementos de un diccionario se usa la funcion " del " y poner como parametro
#el elemento a eliminar
del(dict1[2])
print(dict1)
