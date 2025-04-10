class Coche:
    def __init__(self, matricula, marca, color, tipo):
        self._matricula = matricula
        self._marca = marca
        self._color = color
        self._tipo = tipo
    
    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, nueva_matricula):
        self._matricula = nueva_matricula  

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, nueva_marca):
        self._marca = nueva_marca  

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color 

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo  