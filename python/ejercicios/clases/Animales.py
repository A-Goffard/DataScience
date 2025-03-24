class Animal:
    def __init__(self, especie, color, nombre, n_patas):
        print(f"Creando un animal de la especie {especie}, llamado {nombre}, de color {color} y tiene {n_patas} patas.")
        
        self.especie = especie
        self.color = color
        self.nombre = nombre
        self.n_patas = n_patas
    
    def come(self, dieta):
        print(f"Come {dieta}")
    
    def se_mueve(self, tipo_movimiento):
        print(f"Se mueve {tipo_movimiento}")
    
    def respira(self, tipo_respiracion):
        print(f"Respira {tipo_respiracion}")
    
    def reproduce(self, reproduccion):
        print(f"Su tipo de reproducción es: {reproduccion}")