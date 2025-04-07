from unicodedata import digit

# edad = int(input("ingrese su edad: "))
#
# while edad<5 or edad>100:
#     print("edad invalida")
#     edad = int(input("ingrese su edad: "))
#
# print("edad ingresada" , edad)
#

import math

print("programa de calcual de raiz cuadrada")

numero = int(input("ingrese un numero: "))


intentos = 1

while numero< 0:
    print("no se puede ingresar un numero negativo")
    if intentos == 2:
        print("debe ingresar un numero positivo")
        break
    numero = int(input("ingrese un numero: "))
    intentos += 1

    
if intentos < 2:
    solucion = math.sqrt(numero)
    print("la raiz cuadrada de", numero, "es", solucion)
else:
    print("se te acabaron los intentos")
