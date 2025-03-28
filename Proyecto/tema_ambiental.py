class TemaAmbiental:
    def __init__(self, id, nombre, descripcion, relevancia, relacion_actividades, relacion_publicaciones):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._relevancia = relevancia
        self._relacion_actividades = relacion_actividades
        self._relacion_publicaciones = relacion_publicaciones

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def relevancia(self):
        return self._relevancia

    @relevancia.setter
    def relevancia(self, relevancia):
        self._relevancia = relevancia

    def crear(self):
        return f"Tema ambiental '{self.nombre}' creado exitosamente."

    def editar(self, nombre=None, descripcion=None, relevancia=None):
        if nombre:
            self.nombre = nombre
        if descripcion:
            self.descripcion = descripcion
        if relevancia:
            self.relevancia = relevancia
        return f"Tema ambiental '{self.nombre}' editado exitosamente."

    def eliminar(self):
        return f"Tema ambiental '{self.nombre}' eliminado."

    def buscar(self, criterio):
        if criterio in self.nombre or criterio in self.descripcion:
            return f"Tema ambiental '{self.nombre}' coincide con la búsqueda."
        return f"No se encontraron coincidencias en el tema ambiental '{self.nombre}'."
