class Planta:
    def __init__(self, id, especie, color):
        self._id = id
        self._especie = especie
        self._color = color


    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def especie(self):
        return self._especie
    
    @especie.setter
    def especie(self, especie):
        self._especie = especie
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color