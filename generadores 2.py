"""


   ### **¿Qué es `yield from`?**
El propósito principal de **`yield from`** es delegar automáticamente la iteración en otro generador o cualquier objeto iterable.
En lugar de usar un bucle `for` para iterar sobre un generador o iterable y luego usar múltiples declaraciones `yield` para devolver los valores al generador principal, puedes usar `yield from`.
Esto hace que el código sea más limpio, más corto y más eficiente.


"""


def devuelve_ciudades(*ciudades):
    for elemento in ciudades:  #bucle padre
        #for subelemneto in elemento:#este serio el bucle hijo
            yield from elemento      #con yield drom nos ahorramos el uso de otro bucle , ya obtiene los subelemtnos del elemotn principal
        

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Lisboa")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))