from dominios.rol import Rol

class Roles:
    def __init__(self):
        self.lista_roles = []

    def agregar_rol(self, rol: Rol):
        self.lista_roles.append(rol)
        return f"Rol '{rol.nombre}' agregado exitosamente."

    def modificar_rol(self, nombre_rol, **kwargs):
        for rol in self.lista_roles:
            if rol.nombre == nombre_rol:
                for key, value in kwargs.items():
                    if hasattr(rol, key):
                        setattr(rol, key, value)
                return f"Rol '{rol.nombre}' modificado exitosamente."
        return f"No se encontró el rol con nombre '{nombre_rol}'."

    def buscar_rol(self, nombre_rol):
        for rol in self.lista_roles:
            if rol.nombre == nombre_rol:
                return rol
        return None

    def eliminar_rol(self, nombre_rol):
        for rol in self.lista_roles:
            if rol.nombre == nombre_rol:
                self.lista_roles.remove(rol)
                return f"Rol '{rol.nombre}' eliminado."
        return f"No se encontró el rol con nombre '{nombre_rol}'."
