from Animales import Animal

class Reptil(Animal):
    def __init__(self, especie, color, nombre, n_patas, tipo_escamas):
        super().__init__(especie, color, nombre, n_patas)
        self.tipo_escamas = tipo_escamas
    
    def muda(self):
        print(f"El reptil {self.nombre} está mudando su piel")
    
    def escamas(self):
        print(f"Su tipo de escamas es: {self.tipo_escamas}")
