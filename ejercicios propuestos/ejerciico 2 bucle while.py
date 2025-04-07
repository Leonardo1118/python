"""
Ejercicio 2:
• Crea un programa que pida números positivos indefinidamente. El programa termina
cuando se introduce un número negativo. Finalmente el programa muestras la suma de
todos los números introducido

"""

numero = int(input("digita un numero positivo: "))

acumulador = 0


while numero >= 0:

    numero = int(input("digita un numero positivo: "))
    if numero < 0:
        break

    acumulador += numero

print("la suma de los numeros postivos es: ", acumulador)