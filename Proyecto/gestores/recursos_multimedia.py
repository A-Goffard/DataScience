from dominios.recurso_multimedia import RecursoMultimedia

class RecursosMultimedia:
    def __init__(self):
        self.lista_recursos = []

    def agregar_recurso(self, recurso: RecursoMultimedia):
        self.lista_recursos.append(recurso)
        return f"Recurso multimedia '{recurso.descripcion}' agregado exitosamente."

    def modificar_recurso(self, id_recurso, **kwargs):
        for recurso in self.lista_recursos:
            if recurso.id == id_recurso:
                for key, value in kwargs.items():
                    if hasattr(recurso, key):
                        setattr(recurso, key, value)
                return f"Recurso multimedia '{recurso.descripcion}' modificado exitosamente."
        return f"No se encontró el recurso multimedia con ID '{id_recurso}'."

    def buscar_recurso(self, id_recurso):
        for recurso in self.lista_recursos:
            if recurso.id == id_recurso:
                return recurso
        return None

    def eliminar_recurso(self, id_recurso):
        for recurso in self.lista_recursos:
            if recurso.id == id_recurso:
                self.lista_recursos.remove(recurso)
                return f"Recurso multimedia '{recurso.descripcion}' eliminado."
        return f"No se encontró el recurso multimedia con ID '{id_recurso}'."
