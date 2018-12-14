print("""Este programa cifra o descifra un
mensjae mediante la cifra Cesar \n""")

import pyperclip

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
salida = ""

modo = input ("Deseas cifrar o descrifar (c/D)?")

texto = input("Introduce el texto:")
clave = int(input("Y la clave (1-25):"))

for simbolo in texto.upper():
    if simbolo in ALFABETO:
        pos = ALFABETO.find(simbolo)
        if modo == "c":
            pos = (pos + clave) % 26
        elif modo == "D":
            pos = (pos - clave) % 26
        salida += ALFABETO[pos]
    else:
        salida += simbolo
print(salida)
pyperclip.copy(salida)
