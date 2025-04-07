"""
Las **tuplas** son un tipo de dato en Python que se utiliza para almacenar una colección de elementos ordenados. A diferencia de las listas, las tuplas son **inmutables**, lo que significa que **una vez creadas, no se pueden modificar** (no se pueden agregar, eliminar ni cambiar elementos).
### **Características principales de las tuplas:**
1. **Inmutables**:
    - Una vez que defines una tupla, sus elementos no se pueden cambiar.
    - Esto las hace ideales para almacenar datos que no deben ser modificados, como configuraciones o constantes.

2. **Ordenadas**:
    - Los elementos de una tupla tienen un orden fijo. Esto significa que puedes acceder a ellos mediante un índice, igual que en las listas.

3. **Pueden contener elementos de cualquier tipo de dato**:
    - Una tupla puede almacenar diferentes tipos de datos (números, cadenas, otros objetos, etc.).
    - También puede contener otras tuplas o listas dentro de ella, soportando anidación.

4. **Más rápidas que las listas**:
    - Al no poder modificarse, las tuplas son más ligeras en términos de memoria y procesamiento, lo que las hace más rápidas que las listas para operaciones específicas.

5. **Definidas con paréntesis `()`**:
    - Para declarar una tupla, se utilizan paréntesis redondos.



"""

# Una tupla vacía
tupla_vacia = ()

# Tupla con diferentes tipos de datos
tupla = (1, "Hola", 3.14, True)

print(tupla)  # Salida: (1, 'Hola', 3.14, True)

tupla = ("manzana", "naranja", "platano")

# Acceder al primer elemento
print("El primer elemento de la tupla es:")
print(tupla[0])  # Salida: 'manzana'

# Acceso negativo (empezando desde el final)
print("el ultimo elemento de la tupla es:")
print(tupla[-1])  # Salida: 'platano'


#para convertir de uan tupla a uan lista
lista=list(tupla)
print("tupla convertida a lista:")
print(lista)

#para convertir una lista en una tupla
lista=("moto","bicicleta","camioneta")
print("lista convertida a tupla:")
print(tuple(lista))


#para saber si un lemento está en la tupa
print("manzana es en la tupla:")
print("manzana" in tupla)


tupla = (1, 2, 3, 2, 2, 4)
print("tupla original:", tupla)
# Contar cuántas veces aparece un valor
print("la cantidad de veces que aprece el numeor 2 en la tupla:")
print(tupla.count(2))  # Salida: 3

# Encontrar el índice de un valor
print("el indice del valor 3 en la tupla:")
print(tupla.index(3))  # Salida: 2

tupla = (10, 20, 30)
print("el numero de elementos en la tupla:")
print(len(tupla))  # Salida: 3

"""### Tuplas con un solo elemento:** Al crear una tupla de un solo elemento, **debes incluir una coma
 (`,`) después del valor, de lo contrario, Python lo interpretará como un tipo de dato normal.

"""

# No es una tupla, es solo un número
no_tupla = (5)
print(type(no_tupla))  # Salida: <class 'int'>

# Esto sí es una tupla
si_tupla = (5,)
print(type(si_tupla))  # Salida: <class 'tuple'>


'''
desempaquetado de tuplas

El **desempaquetado de tupla** en Python es una característica que permite extraer los elementos de una tupla 
y asignarlos directamente a múltiples variables de manera simultánea. Esto resulta útil y elegante, especialmente 
cuando sabes exactamente cuántos elementos tiene la tupla que quieres desempaquetar.
### **Cómo funciona el desempaquetado de tuplas**
El desempaquetado consiste en asignar cada elemento de la tupla a una variable distinta de forma paralela.
La cantidad de variables debe coincidir exactamente con la cantidad de elementos en la tupla, o de lo contrario
se generará un error.


'''
# Definimos una tupla
tupla = (10, 20, 30)

# Desempaquetado en variables
a, b, c = tupla

print("desempaquetado en variables:")
# Mostramos los valores de las variables
print(a)  # Salida: 10
print(b)  # Salida: 20
print(c)  # Salida: 30

'''
### **Casos comunes del desempaquetado de tuplas**
#### 1. **Asignación paralela**
El desempaquetado lo puedes usar para asignar valores a múltiples variables en una sola línea, lo cual es más legible
que hacerlo en varias instrucciones separadas.

'''
# Uso en una sola línea
x, y, z = 1, 2, 3
print("asignacion de varibles en una sola linea:")

print(x)  # Salida: 1
print(y)  # Salida: 2
print(z)  # Salida: 3

'''
#### 2. **Intercambio de valores**
El desempaquetado facilita el intercambio de valores entre dos variables sin necesidad de usar variables auxiliares.

'''

a = 5
b = 10

# Intercambio usando desempaquetado
a, b = b, a
print("desempaquetado para intercambiar valores:")
print(a)  # Salida: 10
print(b)  # Salida: 5


'''
#### 3. **Uso con funciones**
Muchas funciones en Python retornan múltiples valores usando tuplas.
 El desempaquetado permite capturarlos directamente en variables.
'''
# Una función que retorna múltiples valores
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta  # Retorna una tupla


# Capturamos los valores con desempaquetado
resultado_suma, resultado_resta = operaciones(10, 5)
print("Operaciones con desempaquetado:")
print("Suma:", resultado_suma)  # Salida: Suma: 15
print("Resta:", resultado_resta)  # Salida: Resta: 5