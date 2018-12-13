#La forma de comentar en python solo una linea de codigo
# es con el signo "  #  "  ejemplo: #comentario1

#Para comentar mas de una linea se usa usa el texto en entre comillas triples un
# ejemplo: """  texto a comentar """
"""  Texto a comentar linea1
     Texto a comentar linea2
     Texto a comentar linea3

 """

"""Los tipos de datos que hay en python entre los cuales estan:
  Numericos: int y float son algunos tipos de datos con numeros
  List: Son conjuntos ordenados de  otros tipos de datos como String
  Complex: Son  tipos de datos variables
"""

#Los datos Numericos pueden ser flotantes o enteros ejemplos son:


#enteros
a = 12
b = 34
c = 3
print(a,b,c)
print(type(a))

#flotantes

x = 23.56
y = 12.4
z = 31.0

print(x,y,z)
print(type(x))

#Tambien se puede representar valores numericos en otros sistemas por ejemplo

#Binario:en Binario se tiene que poner antes del dato a asignar 0B

d = 0B1010
print(d)
print(type(d))

#Hexadecimal:en Binario se tiene que poner antes del dato a asignar 0X

e = 0XFF
print(e)
print(type(e))

#Complex:Para los datos complejos se pone al final de estos una " j " para indicar que son complejos
f = 3+5j
print(f)
print(type(f))

#Otro tipo de datos son los booleanos, los valores pueden ser: True o False
g = True
print(g)
print(type(g))
print(9>2)
print(9>11)
