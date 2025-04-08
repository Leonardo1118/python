def dividir(a, b):
    try:
        return a / b  # Intentar la división normalmente
    except ZeroDivisionError:
        return None    # no devuvle nada


while True:
    try:
        op1 = float(input("Ingrese el primer número: "))
        op2 = float(input("Ingrese el segundo número: "))

        # Resultado de la división
        resultado = dividir(op1, op2)

        # Validar si hubo error (por división entre 0)
        if resultado is None:
            print("No se puede dividir entre 0. Intenta nuevamente.")
            continue  # Pide nuevos números
        else:
            print(f"El resultado de la división es: {resultado}")
            break  # Salir del bucle si todo salió bien

    except ValueError:
        print("Ingresaste un valor no numérico. Intenta nuevamente.")

print("Ejecución normal")