# 📖 MODOS DE APERTURA
# Modo	Significado
# 'r'	Leer (read)
# 'w'	Escribir (write, sobrescribe)
# 'a'	Agregar (append, sin borrar)
# 'r+'	Leer y escribir
# 'b'	Modo binario (ej: 'rb')


# ✍️ 1. Escribir en un archivo
# 🔸 Crear o sobrescribir un archivo
from io import open
archivo = open("archivo.txt", "w", encoding="utf-8")
archivo.write("Hola mundo\nSeré un gran programador")
archivo.close()

#Nota: si el archivo ya existe, lo sobrescribe.

#2. Leer un archivo
# Leer todo el contenido

archivo = open("archivo.txt", "r", encoding="utf-8")
contenido = archivo.read()
archivo.close()
print(contenido)


#Leer línea por línea

archivo = open("archivo.txt", "r", encoding="utf-8")
for linea in archivo:
    print(linea.strip())  # .strip() para quitar el salto de línea
archivo.close()


#3. Agregar contenido sin borrar lo anterior

archivo = open("archivo.txt", "a", encoding="utf-8")
archivo.write("\nSigo aprendiendo Python.")
archivo.close()


#4. Uso de with (recomendado)
#Con with, no necesitas cerrar el archivo manualmente:

with open("archivo.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()
    print(texto)
# 5. Leer líneas como lista

with open("archivo.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

print(lineas)  # ['Hola mundo\n', 'Seré un gran programador\n']







