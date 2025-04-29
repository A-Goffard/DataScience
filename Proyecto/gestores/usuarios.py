from dominios.usuario import Usuario

class Usuarios:
    
    def __init__(self):
        self.lista_usuarios = []

    def registrar(self, usuario: Usuario):
        self.lista_usuarios.append(usuario)
        return f"Usuario '{usuario.nombre}' registrado exitosamente."

    def editar(self, id_usuario, **kwargs):
        for usuario in self.lista_usuarios:
            if usuario.id == id_usuario:
                for key, value in kwargs.items():
                    if hasattr(usuario, key):
                        setattr(usuario, key, value)
                return f"Usuario '{usuario.nombre}' editado exitosamente."
        return f"No se encontró el usuario con ID '{id_usuario}'."

    def eliminar(self, id_usuario):
        for usuario in self.lista_usuarios:
            if usuario.id == id_usuario:
                self.lista_usuarios.remove(usuario)
                return f"Usuario '{usuario.nombre}' eliminado."
        return f"No se encontró el usuario con ID '{id_usuario}'."