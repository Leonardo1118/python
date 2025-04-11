class Persona:
    def __init__(self, nombre , edad ,  lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia


    def descripcion(self):
        print(f'Nombre: {self.nombre} \nEdad: {self.edad} \nResidencia: {self.lugar_residencia}')


class Empleado(Persona):
    def __init__(self , salario, antiguedad , nombre_empleado = None , edad_empleado = None , residencia_empleado = None):

        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)       # vealo como un conectar entre dos clases 

        self.salario = salario
        self.antiguedad = antiguedad
        
    def descripcion(self):
        super().descripcion()
        print(f'Salario: {self.salario} \nAntiguedad: {self.antiguedad}')


antonio = Empleado(1500, 15 , 'Antonio' , 25 , 'Saltillo')

pedro = Empleado(1000, 20 , 'Pedro' , 30 , 'Saltillo')

antonio.descripcion()

pedro.descripcion()

print(isinstance(antonio,Empleado))


# isinstance() nos ayuda a verificar si una instancia (objeto) pertenece a una clase en particular.
# En este caso, "antonio" es un Empleado, pero también es una Persona debido a la herencia.


     