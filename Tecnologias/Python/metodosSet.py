#Metodos para metodos set -Lista
#Para obtener un set-Lista
ejemploSet={1,2,3,4,5} #Forma tradicional de crear un det
print(ejemploSet)

#Forma alterna con set ([grupo de datos])
ejemploSet2=set([1,"rick",3.4,5,6])
print(ejemploSet2)

#Metodo .add
"""Añade un elemento que se ingresa como argumento al  objeto tipo set. 
Si ya hay un objeto equivalente, no se agrega uno nuevo"""

print("ConjuntoA")
conjuntoA={1,'dos', 3.0, '4'}
conjuntoA.add(False)
print(conjuntoA)

#Metodo .remove

"""Busca y elimina al elemento que se ingresa como argumento. En caso
 de no encontrarlo, envía un mensaje de error"""
print("ConjuntoB")
conjuntoB={1,'dos', 3.0, '4'}
conjuntoB.remove(1)
print(conjuntoB)

#Metodo .discard
"""Busca y elimina al elemento que se ingresa como argumento.
 En caso de no encontrarlo, no regresa nada."""
print("ConjuntoC")
conjuntoC={1,'dos', 3.0, '4'}
conjuntoC.discard(3)
print(conjuntoC)

#Metodo .pop
"""Regresas y elimina un elemento del objeto tipo set. 
Cuando ya no existen elementos, se generan un error de tipo KeyError"""
print("ConjuntoD")
conjuntoD={1,'dos', 3.0, '4'}
conjuntoD.pop()
print(conjuntoD)
conjuntoD.pop()
print(conjuntoD)
#Metodo .copy()
"""Regresa una copia exacta del objeto contenido en el objeto tipo set. 
Es similar al rebanado completo de los objetos tipo list."""

print("ConjuntoE")
conjuntoE={1,'dos',3.0,'4'}
conjuntoEcopia={}
print(conjuntoE)
print(conjuntoEcopia)
conjuntoEcopia=conjuntoE.copy()
print(conjuntoEcopia)

#Metodo .clear()
"""Elimina todos los elementos del objeto tipo set."""

print("ConjuntoF")
conjuntoF={1,'dos',3.0,'4'}
print(conjuntoF)
conjuntoF.clear()
print(conjuntoF)

#Metodos para comparar conjuntos

#Metodo .disjoint
"""Evalúa si dos conjuntos no se intersectan. Si no existen elementos compartidos entre el objeto tipo
 set al que pertenece el método y el objeto set que se ingresa como argumento, se regresa el valor True.
  De lo contrario se regresa False."""
print("Metodo disjoint")
conjunto_a = set([1, 2, 3, 4])
conjunto_b = set([3, 4, 5, 6])
conjunto_c = set([5, 6, 7])

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

#Metodo  .issubset()

"""Si el objeto tipo set al que pertenece el método es 
subconjunto del objeto set que se ingresa como argumento, 
se regresa el valor True. De lo contrario se regresa False."""

print("Metodo subset")

conjunto_a = set([1, 2, 3, 4])
conjunto_b = set([1, 2, 4])
conjunto_c = set([1])

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

#Metodo issuperset().

"""Si el objeto tipo set que se ingresa como argumento es subconjunto del objeto tipo 
set al que pertenece el método, se regresa el valor True. De lo contrario se regresa False."""
print("Metodo superset")

conjunto_a = set([1, 2, 3, 4])
conjunto_b = set([1, 2, 4])
conjunto_c = set([1])

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))


#Metodo union

"""Regresa el resultado de la unión del objeto tipo 
set al que pertenece el método y el objeto tipo set que se ingresa como argumento"""

print("Metodo de Union")

conjunto_a = set([1, 2, 3, 4])
conjunto_b = set([3, 4, 5, 6])
conjunto_c = set([5, 6, 7])

print(conjunto_a.union(conjunto_b))
print(conjunto_a.union(conjunto_c))


#Metodo update().

"""Sustituye al objeto tipo set con el resultado de la unión de dicho objeto 
con el objeto tipo set que se ingresa como argumento."""

print("Metodo de update")
conjunto_a = set([1, 2, 3, 4])
conjunto_b = set([3, 4, 5, 6])
conjunto_c = set([5, 6, 7])
conjunto_a.update(conjunto_b)
print(conjunto_a)
conjunto_a.update(conjunto_c)
print(conjunto_a)

#Metodo .difference

"""Regresa el resultado de la diferencia entre el objeto tipo set al que pertenece 
el método y el objeto tipo set que se ingresa como argumento."""
print("Metodo de difference")

conjunto_a = set([1, 2, 3, 4])
conjunto_b = set([3, 4, 5, 6])
conjunto_c = set([5, 6, 7])

print(conjunto_a.difference(conjunto_b))

#Metodo .difference_update()

"""Sustituye al objeto tipo set al que pertenece el método con la diferencia entre
 dicho objeto y el objeto tipo set que se ingresa como argumento."""
print("Metodo de difference_update")

conjunto_a = set([1, 2, 3, 4])
conjunto_b = set([3, 4, 5, 6])

conjunto_a.difference_update(conjunto_b)

print(conjunto_a)

#metodo intersection()

"""Regresa el resultado de la intersección entre el objeto tipo set al que pertenece el 
método y el objeto tipo set que se ingresa como argumento"""
print("Metodo de intersecion")

conjunto_a = set([1, 2, 3, 4])
conjunto_b = set([3, 4, 5, 6])

print(conjunto_a.intersection(conjunto_b))

#Metodo intersection_update()

"""Sustituye al objeto tipo set al que pertenece el método con la intersección
 entre dicho objeto y el objeto tipo set que se ingresa como argumento"""
print("Metodo intersection_update()")
conjunto_a = set([1, 2, 3, 4])
conjunto_b = set([3, 4, 5, 6])
conjunto_a.intersection_update(conjunto_b)
print(conjunto_a)

#Metodo symmetric_difference()

"""Regresa el resultado de la diferencia simétrica entre el objeto tipo set al que pertenece el
 método y el objeto tipo set que se ingresa como argumento"""

print("Metodo intersection_update()")
conjunto_a = set([1, 2, 3, 4])
conjunto_b = set([3, 4, 5, 6])
print(conjunto_a.symmetric_difference(conjunto_b))


#Metodo symmetric_difference_update()

"""Sustituye al objeto tipo set al que pertenece el método con la diferencia simétrica 
entre dicho objeto y el objeto tipo set que se ingresa como argumento"""

print("Metodo symmetric_difference_update()")
conjunto_a = set([1, 2, 3, 4])
conjunto_b = set([3, 4, 5, 6])
conjunto_a.symmetric_difference_update(conjunto_b)
print(conjunto_a)