from dominios.publicacion import Publicacion

class Publicaciones:
    
    def __init__(self):
        self.lista_publicaciones = []

    def crear(self, publicacion: Publicacion):
        self.lista_publicaciones.append(publicacion)
        return f"Publicación '{publicacion.titulo}' creada exitosamente."

    def editar(self, id_publicacion, **kwargs):
        for publicacion in self.lista_publicaciones:
            if publicacion.id == id_publicacion:
                for key, value in kwargs.items():
                    if hasattr(publicacion, key):
                        setattr(publicacion, key, value)
                return f"Publicación '{publicacion.titulo}' editada exitosamente."
        return f"No se encontró la publicación con ID '{id_publicacion}'."

    def eliminar(self, id_publicacion):
        for publicacion in self.lista_publicaciones:
            if publicacion.id == id_publicacion:
                self.lista_publicaciones.remove(publicacion)
                return f"Publicación '{publicacion.titulo}' eliminada."
        return f"No se encontró la publicación con ID '{id_publicacion}'."

    def buscar(self, palabra_clave):
        resultados = [
            publicacion for publicacion in self.lista_publicaciones
            if palabra_clave in publicacion.titulo or palabra_clave in publicacion.contenido
        ]
        if resultados:
            return [f"Publicación '{p.titulo}' coincide con la búsqueda." for p in resultados]
        return f"No se encontraron coincidencias para la palabra clave '{palabra_clave}'."
