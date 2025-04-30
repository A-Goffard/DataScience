from dominios.publicacion import Publicacion

class Publicaciones:
    def __init__(self):
        self.lista_publicaciones = []

    def agregar_publicacion(self, publicacion: Publicacion):
        self.lista_publicaciones.append(publicacion)
        return f"Publicación '{publicacion.titulo}' agregada exitosamente."

    def modificar_publicacion(self, id_publicacion, **kwargs):
        for publicacion in self.lista_publicaciones:
            if publicacion.id == id_publicacion:
                for key, value in kwargs.items():
                    if hasattr(publicacion, key):
                        setattr(publicacion, key, value)
                return f"Publicación '{publicacion.titulo}' modificada exitosamente."
        return f"No se encontró la publicación con ID '{id_publicacion}'."

    def buscar_publicacion(self, id_publicacion):
        for publicacion in self.lista_publicaciones:
            if publicacion.id == id_publicacion:
                return publicacion
        return None

    def eliminar_publicacion(self, id_publicacion):
        for publicacion in self.lista_publicaciones:
            if publicacion.id == id_publicacion:
                self.lista_publicaciones.remove(publicacion)
                return f"Publicación '{publicacion.titulo}' eliminada."
        return f"No se encontró la publicación con ID '{id_publicacion}'."
