class Rol:
    def __init__(self, nombre, tareas_permitidas):
        self._nombre = nombre
        self._tareas_permitidas = tareas_permitidas

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def tareas_permitidas(self):
        return self._tareas_permitidas

    @tareas_permitidas.setter
    def tareas_permitidas(self, tareas_permitidas):
        self._tareas_permitidas = tareas_permitidas

    def puede_realizar(self, tarea):
        return tarea in self.tareas_permitidas


# Definición de roles y sus tareas
ROLES = {
    "administrador": Rol("administrador", [
        "crear publicaciones", "editar contenido", "revisar documentos",
        "compartir publicaciones", "crear nuevos usuarios", "gestionar permisos",
        "eliminar usuarios", "generar métricas y reportes"
    ]),
    "editor": Rol("editor", [
        "crear publicaciones", "editar contenido", "revisar y aprobar publicaciones",
        "gestionar plantillas"
    ]),
    "colaborador": Rol("colaborador", [
        "proponer contenido", "colaborar en publicaciones", "compartir recursos multimedia"
    ])
}
