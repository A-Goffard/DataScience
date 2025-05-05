from operaciones import Operaciones

class Cuadrado(Operaciones):
    def area(self, lado):
        return lado * lado

    def perimetro(self, lado):
        return 4 * lado