class Participante:
    def __init__(self, id, nombre, apellido, correo, telefono, rol, actividades):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._telefono = telefono
        self._rol = rol
        self._actividades = actividades

    @staticmethod
    def crear_participante(id, nombre, apellido, correo, telefono, rol, actividades):
        return Participante(
            id=id,
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            telefono=telefono,
            rol=rol,
            actividades=actividades
        )

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
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

    @property
    def actividades(self):
        return self._actividades

    @actividades.setter
    def actividades(self, actividades):
        self._actividades = actividades

    def __str__(self):
        return (
            f"ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, "
            f"Correo: {self.correo}, Teléfono: {self.telefono}, Rol: {self.rol}, Actividades: {self.actividades}"
        )
