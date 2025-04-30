from dominios.plantilla import Plantilla

class Plantillas:
    def __init__(self):
        self.lista_plantillas = []

    def agregar_plantilla(self, plantilla: Plantilla):
        self.lista_plantillas.append(plantilla)
        return f"Plantilla '{plantilla.titulo}' agregada exitosamente."

    def modificar_plantilla(self, id_plantilla, **kwargs):
        for plantilla in self.lista_plantillas:
            if plantilla.id == id_plantilla:
                for key, value in kwargs.items():
                    if hasattr(plantilla, key):
                        setattr(plantilla, key, value)
                return f"Plantilla '{plantilla.titulo}' modificada exitosamente."
        return f"No se encontró la plantilla con ID '{id_plantilla}'."

    def buscar_plantilla(self, id_plantilla):
        for plantilla in self.lista_plantillas:
            if plantilla.id == id_plantilla:
                return plantilla
        return None

    def eliminar_plantilla(self, id_plantilla):
        for plantilla in self.lista_plantillas:
            if plantilla.id == id_plantilla:
                self.lista_plantillas.remove(plantilla)
                return f"Plantilla '{plantilla.titulo}' eliminada."
        return f"No se encontró la plantilla con ID '{id_plantilla}'."
