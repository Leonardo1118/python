"""
Las instrucciones `continue` y `pass` en Python son dos palabras clave que se utilizan para controlar el flujo del programa dentro de bucles, aunque tienen propósitos diferentes. Aquí te explico cada una:


### **1. Instrucción `pass`**
La instrucción `pass` en Python no realiza ninguna acción. Es esencialmente un "marcador de posición" que se utiliza cuando se requiere una declaración sintácticamente pero no se desea realizar ninguna operación.


#### **Cuándo usar `pass`**
- Cuando estás escribiendo código y deseas que una estructura exista sintácticamente, pero no estés listo para implementarlo todavía.
- En clases o funciones vacías mientras las defines.
- Para evitar errores de sintaxis si dejas un bloque de control vacío



"""

# Ejemplo en un bucle
for i in range(5):
    pass  # Aquí el bucle no hace nada


# Ejemplo en clases
class MiClase:
    pass  # Clase vacía como marcador de posición

"""
En el ejemplo anterior, Python no hará absolutamente nada donde se utiliza `pass`. Esto resulta útil en algunas situaciones, como trabajar en código en desarrollo.

"""

"""
### **2. Instrucción `continue`**
La instrucción `continue` se utiliza para interrumpir la iteración actual en un bucle (como `for` o `while`) y continuar con la siguiente iteración, sin ejecutar el resto del código dentro del bucle para esa iteración.
#### **Cuándo usar `continue`**
- Cuando deseas omitir ciertas iteraciones de un bucle en función de una condición.

"""

for letra in "Python":

    if letra == "h":
        continue
    print(letra)
#en este ejmplo cuando se encuntra con  la letra h la gnora y continua con la sigueinte interaccion


nombre = "leonardo Alvarez"

longitud = len(nombre)

print(longitud)

print("conteo de solo carctaeres de letras")

contador = 0

for i in nombre:
    if i== " ":
        continue
    contador += 1
print(contador)


"""
### **Cómo funciona el `else` en bucles**
La cláusula `else` en un bucle `for` o `while` se ejecuta **solo si el bucle no se interrumpe mediante la instrucción `break`**. Si se ejecuta un `break` dentro del bucle, se salta el bloque del `else`.
#### Regla clave:
- Si el bucle se completa **naturalmente** (es decir, iterando todos los elementos en un `for` o ejecutando mientras la condición sea verdadera en un `while`), se ejecuta el bloque `else`.
- Si el bucle se **rompe** prematuramente mediante `break`, el bloque `else` no se ejecuta.

"""



#en este ejepplo aplicaremos un break a proposito , el else no se ejecuta

print("ejemplo de bucle usando break y else")
for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("Bucle finalizado sin interrupciones.")
  #- En este caso, el `break` interrumpe el bucle cuando `i == 3`, por lo que el bloque `else` **no se ejecuta**.



print("ejemplo de bucle sin break y else")

for i in range(5):
    print(i)
else:
    print("Se ha completado el bucle")

#omo el bucle se completa ahi si ejecuta el else
