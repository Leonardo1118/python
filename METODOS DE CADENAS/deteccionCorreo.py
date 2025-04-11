correo = input("Ingrese su correo: ")

conteo_arroba = correo.count("@")
posicion_arroba = correo.find("@")

termina_con_arroba = correo.endswith("@")
empieza_con_arroba = correo.startswith("@")

if conteo_arroba > 1:
    print("Email inválido: tiene más de 1 arroba")

elif posicion_arroba == -1:
    print("Email inválido: no tiene arroba")

elif termina_con_arroba:
    print("Email inválido: tiene una @ al final")

elif empieza_con_arroba:
    print("Email inválido: tiene una @ al inicio")

else:
    print("Email válido ✅")
