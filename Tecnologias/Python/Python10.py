import math
#Ejemplo de programa de promedio de tres numeros con python 
print("Ejemplos Numero 1 \n")
a,b,c = [int(x) for x in input("Escriba 3 numeros:\n").split()]
average = (a+b+c)/3
print("Promedio de 3 numeros:",average)
#Ejemplo Numero de codigo python
#Ejemplo del area de un circulo
radio1 = float(input("Escriba el area del circulo:\n"))
Pi1= 22/7
area1 = Pi1*(radio1**2)
print("El area del circulo es:",area1,"\n")
#El mismo ejemplo 2 del circulo con el modulo math
radio2 = float(input("Escriba el area del circulo:\n"))
area2 = math.pi*(radio2**2)
print("El area del circulo es:",area2,"\n")