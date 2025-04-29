from figura import Figura

class Figuras:
    def __init__(self):
        self.figuras = []  

    def agregar(self, figura):  
        self.figuras.append(figura)

    def eliminar(self, figura):  
        if figura in self.figuras:
            self.figuras.remove(figura)

    def buscar(self, figura):  
        try:
            return self.figuras.index(figura)
        except ValueError:
            return -1

    def mostrar(self):  
        return "\n".join(str(figura) for figura in self.figuras)

    def existe(self, figura):  
        return figura in self.figuras
