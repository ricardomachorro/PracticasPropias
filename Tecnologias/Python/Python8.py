#Las operaciones aritmeticas basicas dque se pueden hacer con python son


a,b = 10,5.3

#Suma
print("Suma:",a+b)
#Resta
print("Resta:",a-b)
#Multiplicación
print("Multiplicacion:",a*b)
#División entera
print("Division entera:",a//b)
#Modulo
print("Division entera:",a%b)
#Exponente
print("Exponente:",a**b)
#Division decimal
print("Division decimal:",a/b)

#En pyhton tambien se puede dar asignaciones multiples
d=e=f=10
print(d,e,f)
x,y=10,5
#Sumar de manera mas corta
x+=5
print(x)
#Restar de manera mas corta
y-=5
print(y)
#Multiplicar de manera mas corta
x*=2
print(x)
#dividir de manera mas corta
x/=2
print(x)
#dividir de manera mas corta
x//=2
print(x)
#subir un elemnto a una potencia de manera mas corta
x**=2
print(x)
#obtener el modulo de un elemnto  de manera mas corta
x%=2
print(x)

#Sus camparadores son los mismos

#Igual
print(23==2)
#Difrente
print(23!=2)
#Mayor
print(23>2)
#Mayot o Igual
print(23>=2)
#Menor
print(23<2)
#Menor o Igual
print(23<=2)

#Una rareza de python son sun operadores logicos los cuales son:

x=23
y=24
#and
print((x==23 and y==23))
#or
print((x==24 or y==24))
#not
print(not(x==23 and y==23))
