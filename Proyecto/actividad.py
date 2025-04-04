class Actividad:
    def __init__(self, id, tipo, nombre, fecha_ejecucion, descripcion, responsable, duracion, coste_economico, coste_horas, facturacion, resultados, valoracion, modificaciones):
        self._id = id
        self._tipo = tipo
        self._nombre = nombre
        self._fecha_ejecucion = fecha_ejecucion
        self._descripcion = descripcion
        self._responsable = responsable
        self._duracion = duracion
        self._coste_economico = coste_economico
        self._coste_horas = coste_horas
        self._facturacion = facturacion
        self._resultados = resultados
        self._valoracion = valoracion
        self._modificaciones = modificaciones

    @property
    def id(self):
        return self._id

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self.tipo = tipo
        
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def fecha_ejecucion(self):
        return self._fecha_ejecucion

    @fecha_ejecucion.setter
    def fecha_ejecucion(self, fecha_ejecucion):
        self._fecha_ejecucion = fecha_ejecucion

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def responsable(self):
        return self._responsable

    @responsable.setter
    def responsable(self, responsable):
        self._responsable = responsable

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, duracion):
        self._duracion = duracion

    @property
    def coste_economico(self):
        return self._coste_economico

    @coste_economico.setter
    def coste_economico(self, coste_economico):
        self._coste_economico = coste_economico

    @property
    def coste_horas(self):
        return self._coste_horas

    @coste_horas.setter
    def coste_horas(self, coste_horas):
        self._coste_horas = coste_horas

    @property
    def facturacion(self):
        return self._facturacion

    @facturacion.setter
    def facturacion(self, facturacion):
        self._facturacion = facturacion

    @property
    def resultados(self):
        return self._resultados

    @resultados.setter
    def resultados(self, resultados):
        self._resultados = resultados

    @property
    def valoracion(self):
        return self._valoracion

    @valoracion.setter
    def valoracion(self, valoracion):
        self._valoracion = valoracion

    @property
    def modificaciones(self):
        return self._modificaciones

    @modificaciones.setter
    def modificaciones(self, modificaciones):
        self._modificaciones = modificaciones

    def registrar(self):
        return f"Actividad '{self.nombre}' registrada exitosamente."

    def editar(self, nombre=None, descripcion=None, responsable=None, duracion=None, coste_economico=None, coste_horas=None, facturacion=None, resultados=None, valoracion=None, modificaciones=None):
        if nombre:
            self.nombre = nombre
        if descripcion:
            self.descripcion = descripcion
        if responsable:
            self.responsable = responsable
        if duracion:
            self.duracion = duracion
        if coste_economico:
            self.coste_economico = coste_economico
        if coste_horas:
            self.coste_horas = coste_horas
        if facturacion:
            self.facturacion = facturacion
        if resultados:
            self.resultados = resultados
        if valoracion:
            self.valoracion = valoracion
        if modificaciones:
            self.modificaciones = modificaciones
        return f"Actividad '{self.nombre}' editada exitosamente."

    def eliminar(self):
        return f"Actividad '{self.nombre}' eliminada."

    def generar_reporte(self):
        return f"Reporte generado para la actividad '{self.nombre}'."
