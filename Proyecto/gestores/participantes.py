from dominios.participante import Participante

class Participantes:
    def __init__(self):
        self.lista_participantes = []

    def agregar_participante(self, participante: Participante):
        self.lista_participantes.append(participante)
        return f"Participante '{participante.nombre}' agregado exitosamente."

    def modificar_participante(self, id_participante, **kwargs):
        for participante in self.lista_participantes:
            if participante.id == id_participante:
                for key, value in kwargs.items():
                    if hasattr(participante, key):
                        setattr(participante, key, value)
                return f"Participante '{participante.nombre}' modificado exitosamente."
        return f"No se encontró el participante con ID '{id_participante}'."

    def buscar_participante(self, id_participante):
        for participante in self.lista_participantes:
            if participante.id == id_participante:
                return participante
        return None

    def eliminar_participante(self, id_participante):
        for participante in self.lista_participantes:
            if participante.id == id_participante:
                self.lista_participantes.remove(participante)
                return f"Participante '{participante.nombre}' eliminado."
        return f"No se encontró el participante con ID '{id_participante}'."
