#Una caracteristica de python es la de recibir funciones como parametro

def display(fun):
    return "Hello " + fun
def name():
    return "Rick"

print(display(name()))

#Uso del while en python

x = 12

while (x<20):
    print("value:",x,"\n")
    x += 1

print("valor final:",x,"\n")

