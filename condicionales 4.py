print("programa de becas")

distancia = int(input("ingrese la distancia a recorrer en kilometros: "))

numero_hermanos = int(input("ingrese el numero de hermanos con los que vive: "))
salario = int(input("ingrese su salario: "))

if distancia >= 40 and numero_hermanos >= 2 or salario <= 50000:
    print("puede recibir la beca")
else:
    print("no puede recibir la beca")