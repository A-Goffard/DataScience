class Usuario:
    def __init__(self, id, nombre, apellido, email, telefono, fecha_nacimiento, direccion, dni, cp, poblacion, pais, rol, preferencias):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._fecha_nacimiento = fecha_nacimiento
        self._direccion = direccion
        self._dni = dni
        self._cp = cp
        self._poblacion = poblacion
        self._pais = pais
        self._rol = rol
        self._preferencias = preferencias

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
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, cp):
        self._cp = cp

    @property
    def poblacion(self):
        return self._poblacion

    @poblacion.setter
    def poblacion(self, poblacion):
        self._poblacion = poblacion

    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, pais):
        self._pais = pais

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

    @property
    def preferencias(self):
        return self._preferencias

    @preferencias.setter
    def preferencias(self, preferencias):
        self._preferencias = preferencias