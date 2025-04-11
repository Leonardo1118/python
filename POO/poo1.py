class Coche():
    #propiedades  ( atributos )

    def __init__(self):    #este es el constructor
        
        self.__largoChasis = 175
        self.__anchoChasis = 120
        #encapsular es como roteger para qu eno sea accesible desde el exteriro de la clase
        self.__ruedas = 4
        self.__enmarcha = False


    #metodos

    # self es un paramtro pro defecto , hace referencia al propio objeto pertenenciente a la clase
    def arrancar(self,arrancamos):

        self.__enmarcha = arrancamos

        if self.__enmarcha:

            chequeo = self.__check_interno()

        if self.__enmarcha and chequeo:
            return "el coche esta en marcha"

        elif self.__enmarcha and not chequeo:
            return "algo ha ido mal en el chequeo"

        else:
            return "el coche esta parado"

    def estado(self):
        print("el coche tiene" , self.__ruedas , "ruedas")
        print("el largo del chasis es" , self.__largoChasis)
        print("el ancho del chasis es" , self.__anchoChasis)

    def __check_interno(self):
        print("realizando ckequeo interno")

        self.gasolina = "ok"
        self.aceite = "nel"
        self.puerta = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puerta == "cerradas":
            return True
        else:
            return False


print("primer objeto")

Coche1 = Coche()  #INSTANCIAR UNA CLASE

print(Coche1.arrancar(True))

Coche1.estado()



print("a continuacion un nuevo objeto")

Coche2=Coche()

print(Coche2.arrancar(False))


# como ruedas esta encapsulada de nada sirve modifcarlo por aca ya que no es ACCESIBLE
#Coche2.__ruedas = 2

Coche2.estado()





          


    