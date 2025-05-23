class Frutas:
    def __init__(self):
        self.lista_frutas = []

    def crear_vacia(self):
        self.lista_frutas = []

    def agregar_fruta(self, fruta):
        self.lista_frutas.append(fruta)

    def eliminar_fruta(self, fruta):
        self.lista_frutas = [f for f in self.lista_frutas if f != fruta]

    def mostrar_frutas(self):
        return self.lista_frutas

    def buscar_fruta(self, fruta):
        for f in self.lista_frutas:
            if f == fruta:
                return f
        return None
