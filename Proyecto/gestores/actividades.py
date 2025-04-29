from dominios.actividad import Actividad

class Actividades:
    
    def __init__(self):
        self.lista_actividades = []

    def registrar(self, actividad: Actividad):
        self.lista_actividades.append(actividad)
        return f"Actividad '{actividad.nombre}' registrada exitosamente."

    def editar(self, id_actividad, **kwargs):
        for actividad in self.lista_actividades:
            if actividad.id == id_actividad:
                # Actualizar los atributos de la actividad según los argumentos proporcionados
                for key, value in kwargs.items():
                    if hasattr(actividad, key):
                        setattr(actividad, key, value)
                return f"Actividad '{actividad.nombre}' editada exitosamente."
        return f"No se encontró la actividad con ID '{id_actividad}'."

    def eliminar(self, id_actividad):
        for actividad in self.lista_actividades:
            if actividad.id == id_actividad:
                self.lista_actividades.remove(actividad)
                return f"Actividad '{actividad.nombre}' eliminada."
        return f"No se encontró la actividad con ID '{id_actividad}'."

    def generar_reporte(self, id_actividad):
        for actividad in self.lista_actividades:
            if actividad.id == id_actividad:
                return f"Reporte generado para la actividad '{actividad.nombre}'."
        return f"No se encontró la actividad con ID '{id_actividad}'."
