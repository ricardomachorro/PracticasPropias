#Set es un arreglo de elementos que no permite repeticion pero que si permite ser modificada

#Set puede tener varia operaciones con otros set como

print("Operaciones con sets")

#Interseccion entre sets

print("\nInterseccion sets {1,2,3,4,5} y {3,4,5} \n")
#Forma 1:
print("Interseccion 1:",{1,2,3,4,5}.intersection({3,4,5}))

#Forma 2:
print("Interseccion 2:",{1,2,3,4,5}&{3,4,5})

#Union
print("\nUnion sets {1,2,3,4} y {5,6,7,8} \n")
#Forma 1:
print("Union 1:",{1,2,3,4}.union({5,6,7,8}))

#Forma 2:
print("Union 2:",{1,2,3,4}|{5,6,7,8} )

#Diferencia
print("\nDiferencia sets {1,2,3,4,5,6} y {3,4,5} \n")
#Forma 1:
print({1,2,3,4,5,6}.difference({3,4,5}))

#Forma 2:
print({1,2,3,4,5,6}-{3,4,5})

#Diferencia simetrica

print("\nDiferencia Simetrica sets {1,2,3,4,5,6,7} y {1,2,6,7} \n")

#Forma 1:
print({1,2,3,4,5,6,7}.symmetric_difference({1,2,6,7}))

#Forma 2:
print({1,2,3,4,5,6,7}^{1,2,6,7})

#Superset

print("\nSuperset sets {1,2} y {1,2,3} \n")

#Forma 1:
print({1,2}.issuperset({1,2,3}))

#Forma 2:

print({1,2} >= {1,2,3})

#Subset
print("\nSubset sets {1,2} y {1,2,3} \n")


#Forma 1:
print({1,2}.issubset({1,2,3}))

#Forma 2:

print({1,2} <= {1,2,3})

#Set disjuntos
print("\nSet disjuntos \n")

print({1,2}.isdisjoint({3,4}))
print({1,2,3}.isdisjoint({3,4}))

#Los set tambien pueden hacer operaciones con elementos simples como:


print("\nOperaciones con sets y elementos simples\n")

print("\nChecar que dicho elemento este en el set\n")

#Checar que dicho elemento este en el set

print(2 in {1,2,3})
print(4 in {1,2,3})
print(4 not in {1,2,3})

#Agregar un elemento
print("\nAgregar un elemento en el set {1,2,3}\n")
s = {1,2,3}
print(s)
s.add(4)
print(s)

#Descartar un elemento
print("\nDescartar un elemento en el set {1,2,3}\n")
s = {1,2,3}
print(s)
s.discard(2)
print(s)

#Eliminar un elemento
print("\nEliminar un elemento en el set {1,2,3}\n")
s = {1,2,3}
print(s)
s.remove(2)
print(s)

#Algunas de las operaciones de sets sobre sets s epueden resumir como lo son:

print("\n Operaciones de sets sobre sets \n")

#Adicion
print("\n Adicicon a = {1,2,3,4} y b = {4,5,6,7}\n")
a = {1,2,3,4}
b = {4,5,6,7}
a |=b
print(a)

#Interseccion
print("\nInterseccion a = {1,2,3,4} y b = {3,4,5,6}\n")
a = {1,2,3,4}
b = {3,4,5,6}
a &=b
print(a)

#Diferencia

print("\nDiferencia a = {1,2,3,4} y b = {2,3,4,5,6}\n")
a = {1,2,3,4}
b = {2,3,4,5,6}
a -=b
print(a)

#Diferencia Simetrica

print("\nDiferencia Simetrica a = {1,2,3,4} y b = {3,4,5,6}\n")
a = {1,2,3,4}
b = {3,4,5,6}
a ^=b
print(a)

#Actualizar un set

print("\nActualizar un set a = {1,2,3,4}")
a = {1,2,3,4}
b = {3,4,5,6}
a.update(b)
print(a)


#Tambien se puede tener sets dentro de set per para ello hay que convertir dichos set en frozenset
print("\nSets dentro de sets\n")
c= {frozenset({1,2}),frozenset({3,4})}
print(c)

