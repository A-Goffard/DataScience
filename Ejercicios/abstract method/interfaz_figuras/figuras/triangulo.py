from operaciones import Operaciones

class Triangulo(Operaciones):
    def area(self, base, altura):
        return (base * altura) / 2

    def perimetro(self, lado1, lado2, lado3):
        return lado1 + lado2 + lado3