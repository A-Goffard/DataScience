from figura import Figura

class Figuras:
    def __init__(self):
        self.lista_figuras = []

    def anadirFigura(self, figura):
        self.lista_figuras.append(figura)

    def eliminarFigura(self, figura):
        if figura in self.lista_figuras:
            self.lista_figuras.remove(figura)

    def buscarFigura(self, figura):
        try:
            return self.lista_figuras.index(figura)
        except ValueError:
            return -1

    def existeFigura(self, figura):
        return figura in self.lista_figuras
