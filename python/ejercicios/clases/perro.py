class Perro:
    # Atributo de clase
    especie = 'mamífero'

    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza, color):
        print(f"Creando perro {nombre}, {raza}, {color}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza
        self.color = color

    def ladra(self):
        print("Guau")

    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")

    def saltar(self):
        print(f"Salta")