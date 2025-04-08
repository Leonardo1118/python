
#excepciones consecutivas

"""
el bloque `finally` se utiliza en la gestión de excepciones para **especificar un conjunto de acciones que deben ejecutarse siempre**, sin importar si ocurrió una excepción en el bloque `try` o no. Es decir, el código dentro de `finally` se ejecuta **sí o sí**, sin importar el resultado del programa.


"""
def dividir():

    try:
        op1=float(input("Ingrese el primer numero: "))
        op2=float(input("Ingrese el segundo numero: "))
        print("la division es: ",op1/op2)
    except ValueError:
        print("Ingresaste un valor no numerico")

    except ZeroDivisionError:
        print("No se puede dividir entre 0")

    finally:
        print("fin del programa")


dividir()          