class Plantilla:
    def __init__(self, id, titulo, tipo, contenido_base, fecha_creacion, ultima_modificacion, relaciones):
        self._id = id
        self._titulo = titulo
        self._tipo = tipo
        self._contenido_base = contenido_base
        self._fecha_creacion = fecha_creacion
        self._ultima_modificacion = ultima_modificacion
        self._relaciones = relaciones

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
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
