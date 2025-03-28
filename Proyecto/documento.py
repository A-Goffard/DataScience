class Documento:
    def __init__(self, id, titulo, descripcion, fecha_subida, tipo, tematica):
        self._id = id
        self._titulo = titulo
        self._descripcion = descripcion
        self._fecha_subida = fecha_subida
        self._tipo = tipo  # e.g., "PDF", "Word", etc.
        self._tematica = tematica

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
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def fecha_subida(self):
        return self._fecha_subida

    @fecha_subida.setter
    def fecha_subida(self, fecha_subida):
        self._fecha_subida = fecha_subida

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def tematica(self):
        return self._tematica

    @tematica.setter
    def tematica(self, tematica):
        self._tematica = tematica

    def subir(self):
        return f"Documento '{self.titulo}' subido exitosamente."

    def editar(self, titulo=None, descripcion=None, tipo=None, tematica=None):
        if titulo:
            self.titulo = titulo
        if descripcion:
            self.descripcion = descripcion
        if tipo:
            self.tipo = tipo
        if tematica:
            self.tematica = tematica
        return f"Documento '{self.titulo}' editado exitosamente."

    def eliminar(self):
        return f"Documento '{self.titulo}' eliminado."

    def buscar(self, palabra_clave):
        if palabra_clave in self.titulo or palabra_clave in self.descripcion or palabra_clave in self.tematica:
            return f"Documento '{self.titulo}' coincide con la búsqueda."
        return f"No se encontraron coincidencias en el documento '{self.titulo}'."

    def asociar_a_publicacion(self, publicacion):
        return f"Documento '{self.titulo}' asociado a la publicación '{publicacion.titulo}'."
