from usuarios import Usuarios
from usuario import Usuario

class Menu:
    def __init__(self):
        self.usuarios = Usuarios()

    def menu(self):
        while True:
            print("\n---- Menú ----")
            print("1. Agregar nuevo usuario")
            print("2. Eliminar usuario")
            print("3. Buscar usuario")
            print("4. Mostrar lista de usuarios")
            print("5. Salir")
            opcion = input("Inserta una opción: ")

            if opcion == "1":
                id = input("Inserta el ID del usuario: ")
                dni = input("Inserta el DNI del usuario: ")
                nombre = input("Inserta el nombre del usuario: ")
                apellido = input("Inserta el apellido del usuario: ")
                email = input("Inserta el email del usuario: ")
                telefono = input("Inserta el teléfono del usuario: ")
                fecha_nacimiento = input("Inserta la fecha de nacimiento del usuario: ")
                direccion = input("Inserta la dirección del usuario: ")
                cp = input("Inserta el código postal del usuario: ")
                poblacion = input("Inserta la población del usuario: ")
                pais = input("Inserta el país del usuario: ")
                rol = input("Inserta el rol del usuario: ")
                preferencias = input("Inserta las preferencias del usuario: ")

                nuevo_usuario = Usuario(id, nombre, apellido, email, telefono, fecha_nacimiento, direccion, dni, cp, poblacion, pais, rol, preferencias)
                self.usuarios.agregar_usuario(nuevo_usuario)
                print("Usuario agregado correctamente.")
                
            elif opcion == "2":
                nombre_usuario = input("Inserta el nombre del usuario a eliminar: ")
                self.usuarios.eliminar_usuario(nombre_usuario)
                
            elif opcion == "3":
                nombre_usuario = input("Inserta el nombre del usuario a buscar: ")
                self.usuarios.buscar_usuario(nombre_usuario)

            elif opcion == "4":
                self.usuarios.mostrar_usuarios()

            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, elije una opción válida.")