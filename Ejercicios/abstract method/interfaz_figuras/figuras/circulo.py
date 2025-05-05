from operaciones import Operaciones

class Circulo(Operaciones):
    def area(self, radio):
        return 3.14 * radio * radio

    def perimetro(self, radio):
        return 2 * 3.14 * radio
