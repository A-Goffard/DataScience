from usuariosABC import UsuariosABC

class UsuariosBasic(UsuariosABC):
    def __init__(self):
        self.usuarios = {}

    def buscar(self, clave):
        return self.usuarios.get(clave, "Usuario no encontrado")

    def anadir(self):
        return ("No puedo añadir usuarios porque no tengo permisos")

    def eliminar(self, clave):
        if clave in self.usuarios:
            del self.usuarios[clave]
            return "Usuario eliminado correctamente"
        return "Usuario no encontrado"

    def mostrarTodos(self):
        return self.usuarios.values()

