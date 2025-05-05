from figuras.triangulo import Triangulo
from figuras.cuadrado import Cuadrado
from figuras.circulo import Circulo

# Pruebas para Triángulo
triangulo = Triangulo()
print("Triángulo:")
print("Área:", triangulo.area(base=10, altura=5))  # Esperado: 25.0
print("Perímetro:", triangulo.perimetro(lado1=3, lado2=4, lado3=5))  # Esperado: 12

# Pruebas para Cuadrado
cuadrado = Cuadrado()
print("\nCuadrado:")
print("Área:", cuadrado.area(lado=4))  # Esperado: 16
print("Perímetro:", cuadrado.perimetro(lado=4))  # Esperado: 16

# Pruebas para Círculo
circulo = Circulo()
print("\nCírculo:")
print("Área:", circulo.area(radio=3))  # Esperado: 28.26
print("Perímetro:", circulo.perimetro(radio=3))  # Esperado: 18.84
