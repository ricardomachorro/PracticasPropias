#Ejemplo de programa de promedio de tres numeros con python 
a,b,c = [int(x) for x in input("Escriba 3 numeros:\n").split()]
average = (a+b+c)/3
print("Promedio de 3 numeros:",average) 