import pickle

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        print("se creo un objeto de la clase persona, con el nombre ", self.nombre)

    def __str__(self):  #convierte en cadadena del texto la informacion de un objeto
        return f'{self.nombre} {self.apellido} {self.edad}'


class ListaPersonas:
    personas = []

    def __init__(self):
        listadePersonas = open("personas","ab+")  #ab -> agregar informacion binaria
        listadePersonas.seek(0)


        try:
            self.personas = pickle.load(listadePersonas)
            print("se cargaron {} las personas del archivo".format(len(self.personas)))
        except:
            print("no hay personas en el archivo")

        finally:
            listadePersonas.close()


    def   agregarPersona(self, persona):
        self.personas.append(persona)
        self.guardarPersonas()

        
    
    def mostrarPersonas(self):
        for persona in self.personas:
            print(persona)

    def guardarPersonas(self):
        listadePersonas = open("personas","wb")
        pickle.dump(self.personas, listadePersonas)
        listadePersonas.close()
        del listadePersonas

    def mostrarPersonasArchivo(self):
        listadePersonas = open("personas","rb")
        personas = pickle.load(listadePersonas)
        print("la informacion de las personas del archivo es:")
        for persona in personas:
            print(persona)

miLista = ListaPersonas()
persona1 = Persona("Juan", "Perez", 25)
miLista.agregarPersona(persona1)
persona2 = Persona("Ana", "Gonzalez", 23)
miLista.agregarPersona(persona2)
persona3 = Persona("Miguel", "Garcia", 21)
miLista.agregarPersona(persona3)


miLista.mostrarPersonas()


miLista.mostrarPersonasArchivo()



    