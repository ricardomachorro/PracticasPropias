#La funcion print tiene varias formas de ser empleado o modificada
#Un ejemplo es la de afectar separadores de dos varibales al imprimirlas

#Ejemplo se hace con " sep " como se muestra
a,b=12,3
print(a,b,sep="++++")
#Aqui sep indica con que se va a remplazar en print los signos " , " y
#se hace con sep e igualandola al simbolo que quiere poner

#Una forma de concatenar cadenas en python es separando los elementos con los signos " , "
#ejemplo
nombre="Rick"
edad=18
print("Hola me llamo:",nombre," y mi edad es de :",18)
#Otra forma es como se hace en lenhuajes como C por medio del operador " % "
# co %s para stings ,%i para integers, %f para flotantes, y despues de la cadena a poner se pone
#al final "%(variable1,variable2)" con todos las variables en orden a remplazar
print()
