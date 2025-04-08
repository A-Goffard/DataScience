class Usuarios():
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, nuevo_usuario):
        self.usuarios.append(nuevo_usuario)
    
    def eliminar_usuario(self, nombre_usuario):
        usuario_encontrado = None
        for usuario in self.usuarios:
            if usuario.nombre == nombre_usuario:
                usuario_encontrado = usuario
                break
        
        if usuario_encontrado:
            self.usuarios.remove(usuario_encontrado)
            print(f"Usuario '{nombre_usuario}' eliminado de la lista.")
        else:
            print(f"Usuario '{nombre_usuario}' no encontrado en la lista.")
            
    def buscar_usuario(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre == nombre_usuario:
                print(f"Usuario '{nombre_usuario}' encontrado en la lista.")
                print(f" Nombre: {usuario.nombre}, Apellido: {usuario.apellido}, email: {usuario.email}, teléfono: {usuario.telefono}, fecha de nacimiento: {usuario.fecha_nacimiento}, dirección: {usuario.direccion}, DNI: {usuario.dni}, código postal: {usuario.cp}, población: {usuario.poblacion}, país: {usuario.pais}, rol: {usuario.rol}, preferencias: {usuario.preferencias}")
                return usuario  # Salimos del método si encontramos al usuario
        # Este mensaje solo se imprimirá si no se encontró al usuario
        print(f"Usuario '{nombre_usuario}' no encontrado en la lista.")
        return None
        
    def mostrar_usuarios(self):
        print("Lista de usuarios:")
        for i, usuario in enumerate(self.usuarios, 1):
            print(f"{i}. Nombre: {usuario.nombre}, Apellido: {usuario.apellido}, email: {usuario.email}, teléfono: {usuario.telefono}, fecha de nacimiento: {usuario.fecha_nacimiento}, dirección: {usuario.direccion}, DNI: {usuario.dni}, código postal: {usuario.cp}, población: {usuario.poblacion}, país: {usuario.pais}, rol: {usuario.rol}, preferencias: {usuario.preferencias}")