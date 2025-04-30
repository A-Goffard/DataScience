from dominios.usuario import Usuario

class Usuarios:
    
    def __init__(self):
        self.lista_usuarios = []

    def agregar_usuario(self, usuario: Usuario):
        self.lista_usuarios.append(usuario)
        return f"Usuario '{usuario.get_nombre()}' agregado exitosamente."

    def modificar_usuario(self, id_usuario, **kwargs):
        for usuario in self.lista_usuarios:
            if usuario.id == id_usuario:
                for key, value in kwargs.items():
                    if hasattr(usuario, key):
                        getattr(usuario, key)(value)
                return f"Usuario '{usuario.get_nombre()}' modificado exitosamente."
        return f"No se encontró el usuario con ID '{id_usuario}'."

    def buscar_usuario(self, id_usuario):
        for usuario in self.lista_usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None

    def eliminar_usuario(self, id_usuario):
        for usuario in self.lista_usuarios:
            if usuario.id == id_usuario:
                self.lista_usuarios.remove(usuario)
                return f"Usuario '{usuario.get_nombre()}' eliminado."
        return f"No se encontró el usuario con ID '{id_usuario}'."