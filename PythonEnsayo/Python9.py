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
print("Hola me llamo:%s y mi edad es de :%i"%(nombre,edad))
#otra forma es por medio del metodo format , donde se pone el sombolo " { } "
#donde se desee poner la variable y al final del stirng se pone dento del metodo
#format las variables a remplazar en orden
print("Hola me llamo {} y mi edad es de : {}".format(nombre,edad))
#Python tambie permite la entrada de datos con la funcion " input "
#Para asignarle el valor de entrada del teclado solamente con la funcion input
s=input()
print(s)
#Si se quiere desplegar un mensaje junto con la entrada de datos, se pone dentro
#de la funcion input el mensaje
d=input("Escriba su nombre:")
print(d)
#Para pasar puramente un dato numerico desde u input se hace con una concatenacion
number=int(input("Escribe tu edad:"))
print(number)
print(type(number))
#Python tambien puede leer multiples entradas de datos
#Esto lo hace con la funcion " split() "
#el metodo " split() " por default separa los elementos por espacios
listNumber=input("Ponga unos numeros:").split()
print(listNumber)
#Si se quiere poner un signo en especifico a separar en especifico se pasa
#dicho signo como parametro
listNumber2=input("Escriba otros numeros separados por coma:").split(",")
print(listNumber2)
