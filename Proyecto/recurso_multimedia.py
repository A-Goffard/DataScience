class RecursoMultimedia:
    def __init__(self, id, tipo, titulo, fecha_subida, autor, relaciones):
        self._id = id
        self._tipo = tipo  # e.g., "imagen", "video", etc.
        self._titulo = titulo
        self._fecha_subida = fecha_subida
        self._autor = autor
        self._relaciones = relaciones

    @property
    def id(self):
        return self._id

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def fecha_subida(self):
        return self._fecha_subida

    @fecha_subida.setter
    def fecha_subida(self, fecha_subida):
        self._fecha_subida = fecha_subida

    def subir(self):
        return f"Recurso multimedia '{self.titulo}' subido exitosamente."

    def editar(self, tipo=None, titulo=None, fecha_subida=None):
        if tipo:
            self.tipo = tipo
        if titulo:
            self.titulo = titulo
        if fecha_subida:
            self.fecha_subida = fecha_subida
        return f"Recurso multimedia '{self.titulo}' editado exitosamente."

    def eliminar(self):
        return f"Recurso multimedia '{self.titulo}' eliminado."

    def buscar(self, criterio):
        if criterio in self.titulo or criterio in self.tipo:
            return f"Recurso multimedia '{self.titulo}' coincide con la búsqueda."
        return f"No se encontraron coincidencias en el recurso multimedia '{self.titulo}'."
