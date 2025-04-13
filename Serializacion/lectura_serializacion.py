import pickle

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

fichero = open("vehiculos","rb")
coches = pickle.load(fichero)

fichero.close()

for coche in coches:
    coche.estado()
