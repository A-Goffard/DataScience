from actor import Actor

class Actores:
    def __init__(self):
        self.listaActores = []

    def agregarActor(self, actor):
        self.listaActores.append(actor)
        return self.listaActores

    def buscarActor(self, id):
        for actor in self.listaActores:
            if actor.id == id:
                return actor
        return None

    def eliminarActor(self, id):
        actor = self.buscarActor(id)
        if actor:
            self.listaActores.remove(actor)
        return self.listaActores

    def modificarActor(self, id, nombre=None, apellido=None, genero=None, edad=None):
        actor = self.buscarActor(id)
        if actor:
            if nombre is not None:
                actor.nombre = nombre
            if apellido is not None:
                actor.apellido = apellido
            if genero is not None:
                actor.genero = genero
            if edad is not None:
                actor.edad = edad
        return self.listaActores

    def existeActor(self, id):
        return any(actor.id == id for actor in self.listaActores)

    def mostrarActores(self):
        for actor in self.listaActores:
            print(actor)
