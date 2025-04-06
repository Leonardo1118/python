lista = ["leo", "maria" , "pepe"]
print(lista[:])

#para agregar elemntos a la lista

lista.append("juan")  #lo agrega al final de la lista
print("lista con juan agregado al final:")
print(lista)

# ara isnertar un elemnto a una posicion(index)
lista.insert(2,"sandra")
print("lista con sandra en la posicion 2:")
print(lista)

#añadir una lsita a otra lista
'''
- **Propósito**: Agregar todos los elementos de otra lista a la lista original.
- **Modifica la lista original**: `extend` cambia directamente el contenido de la lista original añadiendo los elementos de otra lista.
- **Eficiencia**: Es más eficiente porque no crea una nueva lista, sino que modifica la existente

'''
lista2  =["ana" , "lucia"]

lista.extend(lista2)
print("lista 2 extntedia en lista 1")
print(lista)

#para concer el valor de un idnice dado
print("valor index de lucia en la lista:")
print(lista.index("lucia"))

#para saber si un elemnto se encuntra en uan lista
print("maria esta en la lista?:")
print("maria" in lista)

#se pueden almacener datos de diferente tipo
print("lista con difernetes tipos de variable: ")
lista_combinada=["maria",1 , True]
print(lista_combinada)

# para eliminar un elemnto de uan lista
lista.remove("maria")
print(lista)

#para eliminar el ultimo elemnto agregado
lista.pop()
print("eliminar ultimo elemnto:")
print(lista)

'''
sumar listas
- **Propósito**: Crear una nueva lista que combina los elementos de las listas involucradas.
- **No modifica las listas originales**: En lugar de cambiar alguna de las listas, da como resultado una nueva lista.
- **Eficiencia**: Es menos eficiente que `extend` porque crea un objeto lista completamente nuevo en memoria.

'''

lista3 = [1, 2, 3]
lista4 = [4, 5]

nueva_lista = lista3 + lista4 # No modifica lista1 ni lista2
print("sumar listas")
print(nueva_lista)  # Salida: [1, 2, 3, 4, 5]



#para reptir la lsita una x cantidad de veecs
print("lista repetida: ")
lista3 = [1, 2, 3] * 3
print(lista3)
