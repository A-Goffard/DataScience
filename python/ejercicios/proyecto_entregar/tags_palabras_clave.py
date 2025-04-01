class Tag:
    def __init__(self, id, palabra_clave, categoria, frecuencia_uso, relaciones):
        self._id = id
        self._palabra_clave = palabra_clave
        self._categoria = categoria 
        self._frecuencia_uso = frecuencia_uso
        self._relaciones = relaciones

    @property
    def id(self):
        return self._id

    @property
    def palabra_clave(self):
        return self._palabra_clave

    @palabra_clave.setter
    def palabra_clave(self, palabra_clave):
        self._palabra_clave = palabra_clave

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria

    @property
    def frecuencia_uso(self):
        return self._frecuencia_uso

    @frecuencia_uso.setter
    def frecuencia_uso(self, frecuencia_uso):
        self._frecuencia_uso = frecuencia_uso
