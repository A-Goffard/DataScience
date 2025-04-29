from figura import Figura

class Figuras:
    def __init__(self):
        self.figuras = []

    def agregar(self, figura):
        self.figuras.append(figura)
        print('Figura agregada correctamente.')

    def buscar(self, id):
        for figura in self.figuras:
            if figura.id == id:
                return figura
        return None

    def eliminar(self, id):
        figura = self.buscar(id)
        if figura:
            self.figuras.remove(figura)
            print('Figura eliminada correctamente.')
        else:
            print('Figura no encontrada.')

    def mostrar(self):
        return self.figuras

    def existe(self, id):
        for figura in self.figuras:
            if figura.id == id:
                return True
        return False
