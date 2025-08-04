#Cifrado atbash
import pyperclip
#Alfabetos empleados
CLARO = 'abcdefghijklmnopqrstuvwxyz '
CIFRADO = 'ZYXWUVTSRQPONMLKJIHGFEDCBA '

salida = ''
texto = input('Introduce el texto:')
for simbolo in texto.lower():
    if simbolo in CLARO:
        indice = CLARO.index(simbolo)
        salida += CIFRADO[indice]

print(salida)
pyperclip.copy(salida)
