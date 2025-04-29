class Figura:
    def __init__(self, id, nombre, lados, color):
        self._id = id
        self._nombre = nombre
        self._lados = lados
        self._color = color

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def lados(self):
        return self._lados

    @lados.setter
    def lados(self, lados):
        self._lados = lados

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Lados: {self.lados}, Color: {self.color}"

