class Frutas:
    def __init__(self):
        self.lista_frutas = []

    def crear_vacia(self):
        self.lista_frutas = []

    def agregar_fruta(self, fruta):
        self.lista_frutas.append(fruta)

    def eliminar_fruta(self, id_fruta):
        self.lista_frutas = [
            f for f in self.lista_frutas
            if (f.get_id() if hasattr(f, "get_id") else getattr(f, "_id", None)) != id_fruta
        ]

    def mostrar_frutas(self):
        return self.lista_frutas

    def buscar_frutas(self, nombre):
        return [
            f for f in self.lista_frutas
            if (
                (f.get_nombre().lower() if hasattr(f, "get_nombre") else getattr(f, "_nombre", "").lower())
                == nombre.lower()
            )
        ]

    def buscar_fruta_por_id(self, id_fruta):
        for f in self.lista_frutas:
            if (f.get_id() if hasattr(f, "get_id") else getattr(f, "_id", None)) == id_fruta:
                return f
        return None
