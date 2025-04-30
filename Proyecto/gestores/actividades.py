from dominios.actividad import Actividad

class Actividades:
    def __init__(self):
        self.lista_actividades = []

    def registrar_actividad(self, actividad: Actividad):
        self.lista_actividades.append(actividad)
        return f"Actividad '{actividad.nombre}' registrada exitosamente."

    def modificar_actividad(self, id_actividad, **kwargs):
        for actividad in self.lista_actividades:
            if actividad.id == id_actividad:
                for key, value in kwargs.items():
                    if hasattr(actividad, key):
                        setattr(actividad, key, value)
                return f"Actividad '{actividad.nombre}' modificada exitosamente."
        return f"No se encontró la actividad con ID '{id_actividad}'."

    def buscar_actividad(self, id_actividad):
        for actividad in self.lista_actividades:
            if actividad.id == id_actividad:
                return actividad
        return None

    def eliminar_actividad(self, id_actividad):
        for actividad in self.lista_actividades:
            if actividad.id == id_actividad:
                self.lista_actividades.remove(actividad)
                return f"Actividad '{actividad.nombre}' eliminada."
        return f"No se encontró la actividad con ID '{id_actividad}'."
