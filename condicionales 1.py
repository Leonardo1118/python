
def evaluacion_estudiante(nota1,nota2):
    valoracion = "aprobado"
    promedo =( nota1 + nota2 )/ 2
    if promedo < 3:
        valoracion = "suspenso"
    return valoracion, promedo
print("prgrama de evaluacion de estudiantes")

nota1=int(input("ingrese la primera nota: "))
nota2=int(input("ingrese la segunda nota: "))



valoracion, promedio = evaluacion_estudiante(nota1,nota2)

print(f"el promedio es: {promedio}")
print(f"el estudiante se encuentra en: {valoracion}")
