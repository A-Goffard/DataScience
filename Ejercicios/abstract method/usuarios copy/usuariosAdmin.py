from usuariosABC import UsuariosABC
from usuario import Usuario

class UsuariosAdmin(UsuariosABC):
    def __init__(self):
        self.usuarios = {}

    def buscar(self, clave):
        usuario = self.usuarios.get(clave)
        return usuario["usuario"] if usuario else "Usuario no encontrado"

    def anadir(self, usuario):
        clave = usuario.get("clave")
        if clave in self.usuarios:
            return "El usuario ya existe"
        self.usuarios[clave] = usuario
        return "Usuario añadido correctamente"

    def eliminar(self, clave):
        if clave in self.usuarios:
            del self.usuarios[clave]
            return "Usuario eliminado correctamente"
        return "Usuario no encontrado"

    def mostrarTodos(self):
        return self.usuarios.values()
    
    def crearUsuario(self, usuario, nombre, apellido, anio_nac, passwd):
        nuevo_usuario = Usuario(usuario, nombre, apellido, anio_nac, passwd)
        self.anadir(nuevo_usuario)
        return nuevo_usuario


