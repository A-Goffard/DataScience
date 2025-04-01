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

    def agregar_participante(self, participante):
        """Agrega un participante a la lista de participantes."""
        # Implementación para agregar un participante
        pass

    def modificar_participante(self, id_participante, nuevos_datos):
        """Modifica los datos de un participante existente."""
        # Implementación para modificar un participante
        pass

    def buscar_participante(self, id_participante):
        """Busca un participante por su ID."""
        # Implementación para buscar un participante
        pass

    def eliminar_participante(self, id_participante):
        """Elimina un participante por su ID."""
        # Implementación para eliminar un participante
        pass

    def agregar_actividad(self, actividad):
        """Agrega una actividad a la lista de actividades."""
        # Implementación para agregar una actividad
        pass

    def modificar_actividad(self, id_actividad, nuevos_datos):
        """Modifica los datos de una actividad existente."""
        # Implementación para modificar una actividad
        pass

    def buscar_actividad(self, id_actividad):
        """Busca una actividad por su ID."""
        # Implementación para buscar una actividad
        pass

    def eliminar_actividad(self, id_actividad):
        """Elimina una actividad por su ID."""
        # Implementación para eliminar una actividad
        pass

    def agregar_documento(self, documento):
        """Agrega un documento a la lista de documentos."""
        # Implementación para agregar un documento
        pass

    def modificar_documento(self, id_documento, nuevos_datos):
        """Modifica los datos de un documento existente."""
        # Implementación para modificar un documento
        pass

    def buscar_documento(self, id_documento):
        """Busca un documento por su ID."""
        # Implementación para buscar un documento
        pass

    def eliminar_documento(self, id_documento):
        """Elimina un documento por su ID."""
        # Implementación para eliminar un documento
        pass

    def agregar_tema_ambiental(self, tema):
        """Agrega un tema ambiental a la lista de temas."""
        # Implementación para agregar un tema ambiental
        pass

    def modificar_tema_ambiental(self, id_tema, nuevos_datos):
        """Modifica los datos de un tema ambiental existente."""
        # Implementación para modificar un tema ambiental
        pass

    def buscar_tema_ambiental(self, id_tema):
        """Busca un tema ambiental por su ID."""
        # Implementación para buscar un tema ambiental
        pass

    def eliminar_tema_ambiental(self, id_tema):
        """Elimina un tema ambiental por su ID."""
        # Implementación para eliminar un tema ambiental
        pass

    def agregar_plantilla(self, plantilla):
        """Agrega una plantilla a la lista de plantillas."""
        # Implementación para agregar una plantilla
        pass

    def modificar_plantilla(self, id_plantilla, nuevos_datos):
        """Modifica los datos de una plantilla existente."""
        # Implementación para modificar una plantilla
        pass

    def buscar_plantilla(self, id_plantilla):
        """Busca una plantilla por su ID."""
        # Implementación para buscar una plantilla
        pass

    def eliminar_plantilla(self, id_plantilla):
        """Elimina una plantilla por su ID."""
        # Implementación para eliminar una plantilla
        pass

    def agregar_recurso_multimedia(self, recurso):
        """Agrega un recurso multimedia a la lista de recursos."""
        # Implementación para agregar un recurso multimedia
        pass

    def modificar_recurso_multimedia(self, id_recurso, nuevos_datos):
        """Modifica los datos de un recurso multimedia existente."""
        # Implementación para modificar un recurso multimedia
        pass

    def buscar_recurso_multimedia(self, id_recurso):
        """Busca un recurso multimedia por su ID."""
        # Implementación para buscar un recurso multimedia
        pass

    def eliminar_recurso_multimedia(self, id_recurso):
        """Elimina un recurso multimedia por su ID."""
        # Implementación para eliminar un recurso multimedia
        pass

    def agregar_tag_palabra_clave(self, tag):
        """Agrega un tag o palabra clave a la lista."""
        # Implementación para agregar un tag o palabra clave
        pass

    def modificar_tag_palabra_clave(self, id_tag, nuevos_datos):
        """Modifica los datos de un tag o palabra clave existente."""
        # Implementación para modificar un tag o palabra clave
        pass

    def buscar_tag_palabra_clave(self, id_tag):
        """Busca un tag o palabra clave por su ID."""
        # Implementación para buscar un tag o palabra clave
        pass

    def eliminar_tag_palabra_clave(self, id_tag):
        """Elimina un tag o palabra clave por su ID."""
        # Implementación para eliminar un tag o palabra clave
        pass

    def agregar_publicacion(self, publicacion):
        """Agrega una publicación a la lista de publicaciones."""
        # Implementación para agregar una publicación
        pass

    def modificar_publicacion(self, id_publicacion, nuevos_datos):
        """Modifica los datos de una publicación existente."""
        # Implementación para modificar una publicación
        pass

    def buscar_publicacion(self, id_publicacion):
        """Busca una publicación por su ID."""
        # Implementación para buscar una publicación
        pass

    def eliminar_publicacion(self, id_publicacion):
        """Elimina una publicación por su ID."""
        # Implementación para eliminar una publicación
        pass


