class Cliente:

    def __init__(self,dni,nombre,apellido,direccion,cp,poblacion,pais,edad):
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido
        self.direccion=direccion
        self.cp=cp
        self.poblacion=poblacion
        self.pais=pais
        self.edad=edad

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