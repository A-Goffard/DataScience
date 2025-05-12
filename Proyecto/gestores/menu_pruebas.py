from base_gestor import BaseGestor

class Item:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}"

class Gestor(BaseGestor):
    pass

def menu():
    gestor = Gestor()
    while True:
        print("\nMenú de Pruebas")
        print("1. Agregar Item")
        print("2. Modificar Item")
        print("3. Buscar Item")
        print("4. Eliminar Item")
        print("5. Mostrar Todos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID: ")
            nombre = input("Ingrese el nombre: ")
            descripcion = input("Ingrese la descripción: ")
            item = Item(id, nombre, descripcion)
            print(gestor.agregar(item))

        elif opcion == "2":
            id = input("Ingrese el ID del item a modificar: ")
            nombre = input("Ingrese el nuevo nombre (deje vacío para no modificar): ")
            descripcion = input("Ingrese la nueva descripción (deje vacío para no modificar): ")
            cambios = {}
            if nombre:
                cambios["nombre"] = nombre
            if descripcion:
                cambios["descripcion"] = descripcion
            print(gestor.modificar(id, **cambios))

        elif opcion == "3":
            id = input("Ingrese el ID del item a buscar: ")
            item = gestor.buscar(id)
            if item:
                print(item)
            else:
                print("Item no encontrado.")

        elif opcion == "4":
            id = input("Ingrese el ID del item a eliminar: ")
            print(gestor.eliminar(id))

        elif opcion == "5":
            if gestor.lista:
                for item in gestor.lista:
                    print(item)
            else:
                print("No hay items en la lista.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
