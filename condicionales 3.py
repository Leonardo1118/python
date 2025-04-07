
#OPERADORES DE COMPARACION 
salario_presidente = int(input("Ingrese el salario del presidente: "))
print("el salario del presidente es de:", salario_presidente)

salario_director = int(input("Ingrese el salario del director: "))
print("el salario del director es de:", salario_director)

salario_jefe_Area = int(input("Ingrese el salario del jefe de area: "))
print("el salario del jefe de area es de:", salario_jefe_Area)

salario_administrador = int(input("Ingrese el salario del administrador: "))
print("el salario del administrador es de:", salario_administrador)


if salario_administrador<salario_jefe_Area<salario_director<salario_presidente:
     print("todo bien")
else:
    print("no es posible")