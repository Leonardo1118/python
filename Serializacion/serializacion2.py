import pickle


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



coche1 = Vehiculos("honda","civic")
cohe2 = Vehiculos("honda","crv")
coche3 = Vehiculos("honda","accord")

coches = [ coche1,cohe2,coche3]

fichero = open("vehiculos","wb")

pickle.dump(coches,fichero)

fichero.close()

del coches



