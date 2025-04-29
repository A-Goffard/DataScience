from dominios.recurso_multimedia import RecursoMultimedia

class RecursosMultimedia:
    
    def __init__(self):
        self.lista_recursos = []

    def agregar(self, recurso: RecursoMultimedia):
        self.lista_recursos.append(recurso)
        return f"Recurso multimedia '{recurso.nombre}' agregado exitosamente."

    def editar(self, id_recurso, **kwargs):
        for recurso in self.lista_recursos:
            if recurso.id == id_recurso:
                for key, value in kwargs.items():
                    if hasattr(recurso, key):
                        setattr(recurso, key, value)
                return f"Recurso multimedia '{recurso.nombre}' editado exitosamente."
        return f"No se encontró el recurso multimedia con ID '{id_recurso}'."

    def eliminar(self, id_recurso):
        for recurso in self.lista_recursos:
            if recurso.id == id_recurso:
                self.lista_recursos.remove(recurso)
                return f"Recurso multimedia '{recurso.nombre}' eliminado."
        return f"No se encontró el recurso multimedia con ID '{id_recurso}'."

    def buscar(self, palabra_clave):
        resultados = [
            recurso for recurso in self.lista_recursos
            if palabra_clave in recurso.nombre or palabra_clave in recurso.descripcion
        ]
        if resultados:
            return [f"Recurso multimedia '{r.nombre}' coincide con la búsqueda." for r in resultados]
        return f"No se encontraron coincidencias para la palabra clave '{palabra_clave}'."
