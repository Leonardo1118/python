"""

Los **diccionarios** en Python son estructuras de datos que almacenan pares de **clave y valor** en un formato desordenado, lo que significa que no mantienen un orden específico de los elementos. Son **mutables**, lo que permite agregar, modificar o eliminar elementos después de haberlos creado.

### **Características principales de los diccionarios:**
1. **Estructura clave-valor**:
    - Cada elemento en un diccionario está compuesto por una **clave** y un **valor**.
    - Las claves deben ser únicas y **inmutables** (cadenas, números o tuplas).
    - Los valores pueden ser de cualquier tipo de datos, incluyendo listas, diccionarios u otros objetos.

2. **Acceso rápido**:
    - Los diccionarios tienen un acceso muy eficiente a los valores mediante las claves, similar a un índice en listas, pero usando nombres específicos en lugar de números.

3. **Definidos con llaves `{}`**:
    - Los diccionarios se representan mediante **llaves `{}`** y los pares de clave-valor se separan con dos puntos `:`.

4. **Desordenados**:
    - Antes de Python 3.7, los diccionarios no garantizaban un orden. Sin embargo, a partir de Python 3.7, los diccionarios mantienen el **orden de los elementos** según el momento en que son añadidos.


"""

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Colombia": "Bogota",
    "Chile": "Santiago"
}

print(paises)

#### **Acceso a elementos en un diccionario:**
#Se accede a los valores usando las claves entre corchetes `[]` o con el método `.get()`.


#para ver el valor de una clave
print("El pais de Argentina es:")
print(paises["Argentina"])

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

# Acceso por clave:
print(persona["nombre"])  # Salida: Juan

# Uso del método .get():
print(persona.get("edad"))  # Salida: 25

# Si buscamos una clave que no existe con .get(), devuelve None (no genera error)
print(persona.get("altura"))  # Salida: None

#si usamos diccionario["clave"]  y esta clave no existe ahi si genera un error
#print(persona["altura"])

"""
**Modificación de un diccionario:**
Puedes **agregar** nuevos pares clave-valor, **modificar** valores existentes o **eliminar** elementos.
a) Agregar o modificar elementos:

"""

persona2 = {"nombre": "Juan", "edad": 25}
print("diccionario original")
print(persona2)

# Agregar una nueva clave
persona2["ciudad"] = "Madrid"

# Modificar el valor de una clave existente
persona2["edad"] = 26

print("diccionario modificado")

print(persona2)
# Salida: {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Madrid'}


#para eliminar un elemento

del persona2["ciudad"]
print("se elimina la clave ciudad")
print(persona2)

# Eliminar usando pop()
edad= persona2.pop("edad")
print("se elimina la clave edad usando pop")
print(edad)  # Salida: 26
print(persona2)  # Salida: {'nombre': 'Juan'}


#limipar un direccionario ( eliminar todos los elementos ) :
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

persona.clear()
print(persona)  # Salida: {}

#podemos usar una listadentro de un direccionario

tupla  = ["España", "Francia", "Italia"]
diccionario = {tupla[0]: "Madrid", tupla[1]: "Paris", tupla[2]: "Roma"}
print(diccionario)

print(diccionario["Francia"])

midiccionario = {23:"Jordan", "Nombre": "Michael", "Equipo": "Chicago","anillos" : [1991, 1992, 1993, 1996, 1997 , 1998] }

print(midiccionario["anillos"])

"""
### **Operaciones comunes en diccionarios:**
#### 1. Obtener sólo las claves, valores o pares clave-valor:
- **`keys()`**: Devuelve todas las claves.
- **`values()`**: Devuelve todos los valores.
- **`items()`**: Devuelve pares clave-valor en forma de tuplas.

"""

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

# Obtener las claves
print(persona.keys())  # Salida: dict_keys(['nombre', 'edad', 'ciudad'])

# Obtener los valores
print(persona.values())  # Salida: dict_values(['Juan', 25, 'Madrid'])

# Obtener pares clave-valor
print(persona.items())  # Salida: dict_items([('nombre', 'Juan'), ('edad', 25), ('ciudad', 'Madrid')])


#recorrer diccionarios
#Puedes usar un bucle `for` para recorrer las claves o pares clave-valor.

#recorrer unicmanetes las claves
print("claves recorridas")
for clave in persona:
    print(clave)

#recorrer unicamentes los valores
print("valores recorridos")
for valor in persona.values():
    print(valor)

#recorrer clave y valor
print("pares clave-valor recorridos")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

### **Diccionarios anidados:**
#Un diccionario puede contener otros diccionarios, lo que permite trabajar con estructuras más complejas.


# Ejemplo de diccionario anidado
grupo = {
    "persona1": {"nombre": "Juan", "edad": 25},       #diccionario 1
    "persona2": {"nombre": "María", "edad": 30},      #diccionario 2
}

# Acceso a datos del diccionario anidado
print(grupo["persona1"]["nombre"])  # Salida: Juan
print(grupo["persona2"]["edad"])  # Salida: 30