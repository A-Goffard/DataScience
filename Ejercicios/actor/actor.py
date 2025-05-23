class Actor:
    def __init__(self, id, nombre, apellido, genero, edad):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._genero = genero
        self._edad = edad

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
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        self._genero = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre} {self.apellido}, Género: {self.genero}, Edad: {self.edad}"
