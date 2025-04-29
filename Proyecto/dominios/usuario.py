from rol import Rol

class Usuario:

    def __init__(self, id, nombre, apellido, correo, telefono, fecha_nacimiento, direccion, dni, cp, poblacion, pais, rol, preferencias):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.dni = dni
        self.cp = cp
        self.poblacion = poblacion
        self.pais = pais
        self.rol = rol
        self.preferencias = preferencias

    @property
    def dni(self):
        return self.dni
    @dni.setter
    def dni(self,dni):
        self.dni=dni

    @property
    def nombre(self):
        return self.nombre
    @nombre.setter
    def nombre(self,nombre):
        self.nombre=nombre

    @property
    def apellido(self):
        return self.apellido
    @apellido.setter
    def apellido(self,apellido):
        self.apellido=apellido

    @property
    def direccion(self):
        return self.direcion
    @direccion.setter
    def direccion(self,direccion):
        self.direccion=direccion

    @property
    def cp(self):
        return self.cp
    @cp.setter
    def cp(self, cp):
        self.cp=cp

    @property
    def poblacion(self):
        return self.poplacion
    @poblacion.setter
    def poblacion(self,poblacion):
        self.poblacion=poblacion

    @property
    def pais(self):
        return self.pais
    @pais.setter
    def pais(self, pais):
        self.pais=pais

    @property
    def edad(self):
        return self.edad
    @edad.setter
    def edad(self, edad):
        self.edad=edad

    @property
    def correo(self):
        return self.correo
    @correo.setter
    def correo(self, correo):
        self.correo = correo

    @property
    def telefono(self):
        return self.telefono
    @telefono.setter
    def telefono(self, telefono):
        self.telefono = telefono

    @property
    def fecha_nacimiento(self):
        return self.fecha_nacimiento
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    @property
    def rol(self):
        return self.rol
    @rol.setter
    def rol(self, rol):
        self.rol = rol

    @property
    def preferencias(self):
        return self.preferencias
    @preferencias.setter
    def preferencias(self, preferencias):
        self.preferencias = preferencias
