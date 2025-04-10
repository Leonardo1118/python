

#excepciones personalizadas
# def evaluaEdad(edad):
#     if edad<0:
#         raise TypeError("no se permiten edades negativas")
# 
#     if edad < 20:
#         print("eres muy joven")
#     elif edad<40:
#         print("eres joven")
#     elif edad<65:
#         print("eres adulto")
#     elif edad<100:
#         print("eres mayor")
# 
# evaluaEdad(-15)


import math

def calcularRaiz(numero):
    if numero<0:
        raise ValueError("no se puede calcular la raiz de un numero negativo")

    else:
        return math.sqrt(numero)


op1=int(input("ingrese un numero: "))

try:
    print(calcularRaiz(op1))
except ValueError as e:
    print(e)

print("termino el programa")