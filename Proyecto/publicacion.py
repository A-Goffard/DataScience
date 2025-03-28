class Publicacion:
    def __init__(self, id, titulo, contenido, autor, fecha_creacion, estado, tags, palabras_clave):
        self._id = id
        self._titulo = titulo
        self._contenido = contenido
        self._autor = autor
        self._fecha_creacion = fecha_creacion
        self._estado = estado  # Possible values: "borrador", "publicado", "guardado"
        self._tags = tags
        self._palabras_clave = palabras_clave

    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def contenido(self):
        return self._contenido

    @contenido.setter
    def contenido(self, contenido):
        self._contenido = contenido

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @fecha_creacion.setter
    def fecha_creacion(self, fecha_creacion):
        self._fecha_creacion = fecha_creacion

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags):
        self._tags = tags

    @property
    def palabras_clave(self):
        return self._palabras_clave

    @palabras_clave.setter
    def palabras_clave(self, palabras_clave):
        self._palabras_clave = palabras_clave

    def crear(self, titulo, contenido, autor, tags, palabras_clave):
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.estado = "borrador"
        self.tags = tags
        self.palabras_clave = palabras_clave
        return f"Publicación '{self.titulo}' creada como borrador."

    def editar(self, titulo=None, contenido=None, tags=None, palabras_clave=None):
        if titulo:
            self.titulo = titulo
        if contenido:
            self.contenido = contenido
        if tags:
            self.tags = tags
        if palabras_clave:
            self.palabras_clave = palabras_clave
        return f"Publicación '{self.titulo}' editada."

    def publicar(self):
        if self.estado != "publicado":
            self.estado = "publicado"
            return f"Publicación '{self.titulo}' publicada."
        return f"Publicación '{self.titulo}' ya está publicada."

    def archivar(self):
        if self.estado != "guardado":
            self.estado = "guardado"
            return f"Publicación '{self.titulo}' archivada."
        return f"Publicación '{self.titulo}' ya está archivada."

    def eliminar(self):
        return f"Publicación '{self.titulo}' eliminada."

    def buscar(self, palabra_clave):
        if palabra_clave in self.palabras_clave or palabra_clave in self.tags:
            return f"Publicación '{self.titulo}' coincide con la búsqueda."
        return f"No se encontraron coincidencias en la publicación '{self.titulo}'."

    def asignar_recursos(self, recursos_multimedia, nuevas_palabras_clave):
        self.tags.extend(recursos_multimedia)
        self.palabras_clave.extend(nuevas_palabras_clave)
        return f"Recursos multimedia y palabras clave asignados a la publicación '{self.titulo}'."
