#Otro tipo de dato que existe en python y que sirve mucho para bucles
#es el tipo de dato range, ya que esta es  una coleccion ordenada de numeros que los puede
#controlar estricturas como el for

#se declara con la palabra reservada range:
#si se le pone solo un parametro este se toma como valor maximo
rang1 = range(6)
for i in rang1:
    print(i)
print("//////////////////////")
#si se le ponen dos parametros se toma el primero com valor minimo, y el ultimo como el maximo
rang2 = range(2,5)
for i in rang2:
    print(i)
print("//////////////////////")
#si se le ponen tres parametros se toma el primero com valor minimo,el segundo como valor maximo
# y el ultimo como el salto que se da entre numeros
rang3 = range(3,19,3)
for i in rang3:
    print(i)
print("///////////////////////")
