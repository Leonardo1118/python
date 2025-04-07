
"""
Ejercicio 1:
• Crea un programa que pida números infinitamente. Los números introducidos deben
ser cada vez mayores El programa finalizará cuando se introduce un número menor que
el anterior.
"""
# estado = False
# numero_comparacion = int(input("digita un numero: "))
# while estado == False :
#     numero = int(input("digita un numero: "))
#
#     if  numero > numero_comparacion :
#         numero_comparacion= numero
#         estado = False
#     else:
#         estado = True
#
# print("el numero que introdiciste fue: " , numero,"y es menor que:" , numero_comparacion )


numero_comparacion = int(input("Introduce el primer número: "))  # Pedimos el primer número
while True:
    numero = int(input(f"Introduce un número mayor que {numero_comparacion}: "))
    if numero <= numero_comparacion:
        print(f"El número {numero} es menor o igual que {numero_comparacion}. Fin del programa.")
        break  # Salimos del bucle
    numero_comparacion = numero  # Actualizamos el número de comparación
