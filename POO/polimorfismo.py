"""
Polimorfismo en Programación Orientada a Objetos
✅ ¿Qué es el polimorfismo?
El polimorfismo es cuando varias clases diferentes pueden usar un mismo método, pero cada una lo hace a su manera.

📌 Significa “muchas formas” (del griego poly = muchos, morph = forma).



"""


class Coche:

    def desplazamiento(self):
        print("Desplazamiento e 4 ruedas")


class Moto:
    def desplazamiento(self):
        print("Desplazamiento e 2 ruedas")


class Camion:
    def desplazamiento(self):
        print("Desplazamiento e 6 ruedas")




def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


desplazamientoVehiculo(Coche())

desplazamientoVehiculo(Moto())

desplazamientoVehiculo(Camion())