class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

        self.enmarcha = False
        self.acelerando = False
        self.frenando = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelerando = True

    def frenar(self):
        self.frenando = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo)
        print("En marcha: ", self.enmarcha, "\nAcelerando: ", self.acelerando, "\nFrenando: ", self.frenando)


class Furgoneta(Vehiculos):

    def Carga(self, carga):
        self.cargado = carga

        if self.cargado:
            return "La carga es satisfactoria"
        else:
            return "Carga insuficiente"


class Velectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


class Moto(Vehiculos):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "voy haciedno un caballito"

    # esramos sobrescribienod el metodo estado de la clase padre : vehiculos
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo)
        print("En marcha: ", self.enmarcha, "\nAcelerando: ", self.acelerando, "\nFrenando: ", self.frenando,
              "\nHace caballito: ", self.hcaballito)


