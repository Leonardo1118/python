from io import *

archivo = open("archivo.txt", "r+")   #lectura y escritura al tiempo


#archivo.seek(1)  #posicona el puntero


# archivo.seek(len(archivo.readline()))
#
# print(archivo.read())



#print(archivo.readlines())


listatexto = archivo.readlines()


listatexto[2]= "re la comes sin pretexto\n"

archivo.seek(0)

archivo.writelines(listatexto)

archivo.close()


"""
📄 Manejo de Archivos de Texto en Python con Librería io
📍 Y qué es un PUNTERO de archivo
🧠 ¿Qué es un puntero de archivo?
Cuando trabajamos con archivos en Python, cada vez que los abrimos, Python coloca un puntero que marca la posición actual dentro del archivo.

Ese puntero indica dónde se va a leer o escribir.

Cuando abres un archivo, el puntero empieza en la posición 0 (el inicio).

A medida que lees o escribes, el puntero avanza automáticamente.

Puedes consultar o mover el puntero para leer o escribir desde un punto específico.

📚 Comandos clave
Comando	Descripción
archivo.read(n)	Lee n caracteres desde donde esté el puntero. Si no pasas nada, lee todo desde allí hasta el final.
archivo.write("texto")	Escribe texto desde la posición actual del puntero.
archivo.tell()	Muestra en qué posición está el puntero.
archivo.seek(pos)	Mueve el puntero a la posición pos. Ideal para releer o sobrescribir desde cierto punto.
🔧 Ejemplo práctico con explicaciones
"""
# Importamos 'open' desde 'io' (opcional, puedes usar solo open() también)
from io import open

# Abrimos el archivo en modo lectura ('r')
archivo = open("archivo.txt", "r")

# Mostramos dónde está el puntero (inicio del archivo)
print("Posición inicial:", archivo.tell())  # ➝ 0

# Leemos los primeros 10 caracteres
texto = archivo.read(10)
print("Leído:", texto)

# Mostramos nuevamente la posición del puntero (ya avanzó)
print("Nueva posición del puntero:", archivo.tell())  # ➝ 10

# Volvemos al inicio con seek()
archivo.seek(0)

# Leemos todo el archivo desde el principio
print("Archivo completo desde el inicio:")
print(archivo.read())

archivo.close()
# Ejemplo con escritura

archivo = open("archivo.txt", "w")  # Modo escritura: sobrescribe el contenido

# Escribimos texto
archivo.write("Hola mundo\n")
archivo.write("Estoy aprendiendo Python y manejo de archivos.\n")

archivo.close()
#Ahora, si luego haces una lectura:

archivo = open("archivo.txt", "r")
print(archivo.read())  # Lee todo desde el inicio
archivo.close()
