from actores import Actores
from actor import Actor

def menu():
    actores = Actores()
    while True:
        print("\n--- Menú de Actores ---")
        print("1. Agregar actor")
        print("2. Buscar actor")
        print("3. Eliminar actor")
        print("4. Modificar actor")
        print("5. Mostrar todos los actores")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            genero = input("Género: ")
            while True:
                edad_input = input("Edad: ")
                try:
                    edad = int(edad_input)
                    break
                except ValueError:
                    print("Por favor, introduzca un número entero para la edad.")
            actor = Actor(id, nombre, apellido, genero, edad)
            actores.agregarActor(actor)
            print("Actor agregado.")
        elif opcion == "2":
            id = input("ID del actor a buscar: ")
            actor = actores.buscarActor(id)
            if actor:
                print(actor)
            else:
                print("Actor no encontrado.")
        elif opcion == "3":
            id = input("ID del actor a eliminar: ")
            if actores.existeActor(id):
                actores.eliminarActor(id)
                print("Actor eliminado.")
            else:
                print("El actor no existe.")
        elif opcion == "4":
            id = input("ID del actor a modificar: ")
            if actores.existeActor(id):
                print("Deje en blanco los campos que no desea modificar.")
                nombre = input("Nuevo nombre: ")
                apellido = input("Nuevo apellido: ")
                genero = input("Nuevo género: ")
                while True:
                    edad_input = input("Nueva edad: ")
                    if edad_input == "":
                        edad = None
                        break
                    try:
                        edad = int(edad_input)
                        break
                    except ValueError:
                        print("Por favor, introduzca un número entero para la edad o deje en blanco.")
                actores.modificarActor(
                    id,
                    nombre if nombre else None,
                    apellido if apellido else None,
                    genero if genero else None,
                    edad
                )
                print("Actor modificado.")
            else:
                print("El actor no existe.")
        elif opcion == "5":
            actores.mostrarActores()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
