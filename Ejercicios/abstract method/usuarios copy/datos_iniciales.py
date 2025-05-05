from usuario import Usuario
from usuariosAdmin import UsuariosAdmin

def obtener_usuarios_iniciales():
    return [
        Usuario("ainara", "Ainara", "De Miguel", "1977", "1234"),
        Usuario("joxe", "Joxe", "Zabaleta", "1988", "pass1234"),
        Usuario("luciag", "Lucía", "Gómez", "1992", "mypass789")
    ]

if __name__ == "__main__":
    gestor = UsuariosAdmin()
    for usuario in obtener_usuarios_iniciales():
        gestor.anadir({"clave": usuario.usuario, "usuario": usuario})
    print("Usuarios iniciales añadidos correctamente.")
