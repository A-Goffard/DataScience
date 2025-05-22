class Fruta:
    def __init__(self, id, nombre, color, sabor):
        self._id = id
        self._nombre = nombre
        self._color = color
        self._sabor = sabor

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def sabor(self):
        return self._sabor

    @sabor.setter
    def sabor(self, value):
        self._sabor = value

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Color: {self._color}, Sabor: {self._sabor}"