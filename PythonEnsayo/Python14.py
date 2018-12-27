import math, cmath, operator

#Algunas operaciones aritmeticas de python se pueden lograr o es necesario los modulos math,cmath u operator

print("\nOperaciones aritmeticas de python con modulos math, cmath y operator\n")
#Un ejemplo de estas formas son:

print("\nLa division\n")
#La division

print("\nOperator para divisiones flotantes\n")
print(operator.truediv(3,4))#Para divisiones flotantes
print("\nOperator para divisiones enteras\n")
print(operator.floordiv(4,3))#Para divisiones enteras

print("\nLa Suma\n")
#Suma

a,b = 1,2

print("\nOperator para suma \n")
print(operator.add(a,b))#Suma usando el modulo operator

#Sumando de manera rapida a un variable

print("\nSuma rapida \n")
print(a)
a += 2
print(a)


#Una forma de hacer la suma parecida a " += " con el modulo operator
print("\nSuma rapida con modulo Operator \n")
print(operator.iadd(a,b))

#Exponenciacion

print("\nExponenciacion\n")

#Para elevar una base a un exponente en Python normalmente se hace simplemente asi:

print("Exponenciacion rapida")
print(2**3)

print("Exponenciacion rapida 2")
print(pow(2,3))

#tambien se puede hacer raices o exponentes fraccionarios

print(8**(1/3))

print(pow(8,(1/3)))

#Raiz cuadrada

print("Raiz cuadrada")

print("Raiz cuadrada normal con math")

print(math.sqrt(4))

print("Raiz cuadrada  con numeros complejos con cmath")

print(cmath.sqrt(4+5j))

#Tambien se puede poner exponenciacion en base e con exp

print("Exponenciacion base e")

print(math.exp(0))
print(math.exp(1))

#Tambien se puede usar fucniones trigonometricas

print("Funciones trigonometricas")

print(math.sin(1))#Esta recibe y devuelve parametros en radianes

print(math.cos(1))

print(math.tan(1))

print(math.atan(math.pi))

print(math.acos(.67))

print(math.asin(.67))

#Tambien se puede usar el teorema de pitagoras

print("Teorema de pitagoras con 3 y 4 como catetos")

print(math.hypot(3,4))

#Se puede transformar grados a redianes y en reversa

print("Radianes:1 a Grados")
print(math.degrees(1))

print("Grados: 57.29577951308232 a radianes")
print(math.radians(57.29577951308232))

#Tambien se pueden acortar elementos o funciones

print("\nAcortar elementos \n")

#Adicion
a,b,c = 1,2,3
c += b
print(c)
#Resta
a -= c
print (a)
#Multiplicacion
b *= c
print(b)
#Division
a /= c
print(a)
#Division entera
b //= a
print(b)
#Modulo
c %= b
print(c)
#Exponenciacion
a **= c
print(b)

#Tambien se puede usar logaritmos

print("Tambien se puede usar logaritmos\n")

print(math.log(100,10))

#Por default es base e

print(math.log(3))

#Tmabien hay variantes base 2 y 10

print(math.log2(6))

print(math.log10(40))