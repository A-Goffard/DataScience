class Animales:
    def __init__(self, especie, color, nombre):
        print(f"Creando un animal de la especie {especie}, llamado {nombre}, de color {color}.")
        
        self.especie = especie
        self.color = color
        self.nombre = nombre
    
    def zona(self,lugar):
        print(f"Vive en la zona {lugar}")
    
    def come(self,dieta):
        print(f"Come {dieta}")
    
    def vuela(self, velocidad_vuelo):
        print(f"Vuela a {velocidad_vuelo} km por hora")
    
    def crias(self, n_crias):
        print(f"Suele tener {n_crias} crias por vez")
    
    def pico(self, tipo_pico):
        print(f"Su tipo de pico es: {tipo_pico}")

from Animales import Animal

class Ave(Animal):
    def __init__(self, especie, color, nombre, n_patas, tipo_pico):
        super().__init__(especie, color, nombre, n_patas)
        self.tipo_pico = tipo_pico
    
    def vuela(self, velocidad_vuelo):
        print(f"Vuela a {velocidad_vuelo} km por hora")
    
    def crias(self, n_crias):
        print(f"Suele tener {n_crias} crias por vez")
    
    def pico(self):
        print(f"Su tipo de pico es: {self.tipo_pico}")