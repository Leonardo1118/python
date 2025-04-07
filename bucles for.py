#bucle for
from itertools import count

# for i in ["primacera","verano", "otoño","invierno"]:
#     print(i)

# for i in [1,2,3,4,5]:
#     print("hola" , end= " ")   #el end aplcia como un modificador al final

# contador= 0
#
# for i in "leonardo@gmail.com":
#     if i == "@" or i == ".":
#         contador += 1
#
#
# if contador == 2:
#     print("es un correo valido")
#
# else:
#     print("no es un correo valido")


# for i in range(5,50,3):
#     print(f"valor de la variable {i}")

valido = False

email = input("ingrese su correo: ")

for i in range(len(email)):
    print(f"{i+1} valor: {email[i]}" , end=" , ")
    if email[i] == "@" :
        valido = True

if valido:
    print("correo valido")
else:
    print("correo invalido")