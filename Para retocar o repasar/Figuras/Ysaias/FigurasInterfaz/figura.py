class Figura:
    def __init__(self, id, nombre, lados, color):
        self._id = id
        self._nombre = nombre
        self._lados = lados
        self._color = color

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_lados(self):
        return self._lados

    def set_lados(self, lados):
        self._lados = lados

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color
