from dominios.plantilla import Plantilla

class Plantillas:
    
    def __init__(self):
        self.lista_plantillas = []

    def crear(self, plantilla: Plantilla):
        self.lista_plantillas.append(plantilla)
        return f"Plantilla '{plantilla.nombre}' creada exitosamente."

    def editar(self, id_plantilla, **kwargs):
        for plantilla in self.lista_plantillas:
            if plantilla.id == id_plantilla:
                for key, value in kwargs.items():
                    if hasattr(plantilla, key):
                        setattr(plantilla, key, value)
                return f"Plantilla '{plantilla.nombre}' editada exitosamente."
        return f"No se encontró la plantilla con ID '{id_plantilla}'."

    def eliminar(self, id_plantilla):
        for plantilla in self.lista_plantillas:
            if plantilla.id == id_plantilla:
                self.lista_plantillas.remove(plantilla)
                return f"Plantilla '{plantilla.nombre}' eliminada."
        return f"No se encontró la plantilla con ID '{id_plantilla}'."

    def buscar(self, palabra_clave):
        resultados = [
            plantilla for plantilla in self.lista_plantillas
            if palabra_clave in plantilla.nombre or palabra_clave in plantilla.descripcion
        ]
        if resultados:
            return [f"Plantilla '{p.nombre}' coincide con la búsqueda." for p in resultados]
        return f"No se encontraron coincidencias para la palabra clave '{palabra_clave}'."
