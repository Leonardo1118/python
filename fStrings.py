"""
 🔤 ¿Qué son las f-strings?
Las f-strings (también llamadas formatted string literals) son una forma moderna y muy fácil de insertar variables dentro de cadenas de texto en Python.


Por qué usarlas?
Porque son:

Más legibles

Más rápidas

Más cómodas que otras formas de formatear texto



"""



nombre = "Carlos"
edad = 28

mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)
# ➜ Hola, mi nombre es Carlos y tengo 28 años.


x,y = 1,2

print(f"la suma de {x} + {y} es {x+y}")

pi=3.141516

print(f"el valor de pi es {pi:.2f}")




