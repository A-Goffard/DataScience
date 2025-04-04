from Animal import Animal

class Animales():
    def __init__(self):
        self.animales = []

    def agregar_animal(self, nuevo_animal):
        
        self.animales.append(nuevo_animal)
        

    def mostrar_animales(self):
        print("Lista de Animales:")
        for i, animal in enumerate(self.animales, 1):
            print(f"{i}. Nombre: {animal.nombre}, Edad: {animal.edad}, Especie: {animal.especie}")

    