
"""
🧠 ¿Qué es la serialización?
La serialización es el proceso de convertir un objeto de Python (como listas, diccionarios, clases, etc.) en un formato que pueda ser guardado en un archivo o enviado por una red, como por ejemplo un archivo .json o .bin.

🔁 Lo contrario (recuperarlo) se llama deserialización.

🧩 ¿Para qué sirve?
Guardar el estado de un programa (por ejemplo, los datos de una app) en un archivo.

Enviar datos a través de internet (por ejemplo, en APIs).

Compartir datos entre programas o con otros lenguajes.

Guardar objetos complejos como si fueran texto o bytes.


 Formatos más comunes de serialización:
Formato	Descripción	Librería en Python
.json	Texto legible, ideal para humanos y web	json
.bin (binario)	No legible, ideal para guardar objetos tal cual	pickle

🔐 Diferencias importantes
Característica

JSON
formato texto plano
es legible para los humanos
Portabilida es Muy buena (otros lenguajes lo leen)
Seguridad	✅ (si conoces el origen)




Pickle:
formato Binario
no es legible para los humanos
Solo Python la puede usar
❌ (no usar con datos de desconocidos, puede ejecutar código malicioso)


En resumen:
Serializar = Guardar objetos como texto o binario.

Deserializar = Recuperarlos para volver a usarlos.

Usa json si es algo simple y legible.

Usa pickle si necesitas guardar cualquier tipo de objeto, incluso clases.




"""

import pickle
# lista_nombres = ["Juan", "Pedro", "Ana", "leo"]
#
# ## con esto guardamos un objeto en el fichero binario
# fichero_binario = open("nombres", "wb")  #wb = escritura binaria
#
# pickle.dump(lista_nombres, fichero_binario)
#
# fichero_binario.close()
#
# del fichero_binario

fichero= open("nombres", "rb")

lista_nombres = pickle.load(fichero)
print(lista_nombres)