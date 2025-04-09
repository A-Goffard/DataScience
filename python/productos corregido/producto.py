class Producto:
    def __init__(self, id, nombre, descripcion, precio):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        self._descripcion = nueva_descripcion

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        self._precio = nuevo_precio