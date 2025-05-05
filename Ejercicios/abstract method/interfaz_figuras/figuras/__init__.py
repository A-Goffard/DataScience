class Figuras:
    def __init__(self):
        self.figuras = []

    def agregar(self, figura):
        self.figuras.append(figura)

    def eliminar(self, id):
        self.figuras = [figura for figura in self.figuras if figura.id != id]

    def buscar(self, id):
        for figura in self.figuras:
            if figura.id == id:
                return figura
        return None

    def mostrar(self):
        return [(figura.id, figura.nombre, figura.lados, figura.color) for figura in self.figuras]
