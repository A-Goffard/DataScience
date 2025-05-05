from usuario import Usuario

def obtener_usuarios_iniciales():
    return [
        Usuario("ainara", "Ainara", "De Miguel", "1977", "1234"),
        Usuario("joxe", "Joxe", "Zabaleta", "1988", "pass1234"),
        Usuario("luciag", "Lucía", "Gómez", "1992", "mypass789")
    ]

if __name__ == "__main__":
    usuarios_iniciales = obtener_usuarios_iniciales()
    with open("usuarios.txt", "w") as archivo:
        for usuario in usuarios_iniciales:
            archivo.write(usuario.to_linea() + "\n")
    print("Archivo usuarios.txt creado con datos iniciales.")
