#Una coleccion de datos que permite python es el de los "  set " , el cual
# a diferencia de las listas no permite repetociones, pero a diferencias
#de las tuplas permite modificacion

#Para declarar los set set se hace con corchetes " { contenido }" despues de la declaracion
#ejemplo:

set1 = {12,34,22,"Yeah"}
print(set1)
print(type(set1))

#Para poder agregar un elemento a un set se usa el metodo " update " en el cual
# se pone como parametro entre signos " [] " el contenido a ingresar

#ejemplo:

set1.update([55,2,3])
print(set1)

#para eliminar elementos se usa el metodo " remove "
#ejemplo:

set1.remove(34)
print(set1) 
