
#operador in

"""
El operador **`in`** en Python se utiliza para comprobar **si un elemento está presente en una colección o iterable** (como una lista, tupla, string, conjunto, o diccionario). También se puede usar en condicionales para realizar comprobaciones de existencia de manera sencilla.
### **Funcionamiento del operador `in`**
El operador `in` devuelve:
- **`True`**: Si el elemento se encuentra en el iterable.
- **`False`**: Si el elemento no está presente en el iterable.

Además, el operador tiene una contraparte llamada **`not in`**, que devuelve el valor contrario.


"""
print("asginaturas 2025")

asginaturas = ["matematicas", "fisica", "quimica"]

for i in asginaturas:
    print(i)
asignatura = input("ingrese asignatura: ").lower()


if asignatura in asginaturas:
    print("la asignatura elegida es" , asignatura)
else:
    print("la asignatura no existe")