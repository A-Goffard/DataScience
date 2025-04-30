from dominios.tema_ambiental import TemaAmbiental

class TemasAmbientales:
    def __init__(self):
        self.lista_temas = []

    def agregar_tema(self, tema: TemaAmbiental):
        self.lista_temas.append(tema)
        return f"Tema ambiental '{tema.nombre}' agregado exitosamente."

    def modificar_tema(self, id_tema, **kwargs):
        for tema in self.lista_temas:
            if tema.id == id_tema:
                for key, value in kwargs.items():
                    if hasattr(tema, key):
                        setattr(tema, key, value)
                return f"Tema ambiental '{tema.nombre}' modificado exitosamente."
        return f"No se encontró el tema ambiental con ID '{id_tema}'."

    def buscar_tema(self, id_tema):
        for tema in self.lista_temas:
            if tema.id == id_tema:
                return tema
        return None

    def eliminar_tema(self, id_tema):
        for tema in self.lista_temas:
            if tema.id == id_tema:
                self.lista_temas.remove(tema)
                return f"Tema ambiental '{tema.nombre}' eliminado."
        return f"No se encontró el tema ambiental con ID '{id_tema}'."
