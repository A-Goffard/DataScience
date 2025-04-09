from productos import Productos
from producto import Producto

class Menu:
    def __init__(self):
        self.productos = Productos()

    def mostrar_menu(self):
        while True:
            print("\n---- Menú ----")
            print("1. Agregar producto")
            print("2. Buscar producto")
            print("3. Eliminar producto")
            print("4. Mostrar todos los productos")
            print("5. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.agregar_producto()
            elif opcion == "2":
                self.buscar_producto()
            elif opcion == "3":
                self.eliminar_producto()
            elif opcion == "4":
                self.productos.mostrar_lista_productos()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

    def agregar_producto(self):
        id = input("ID del producto: ")
        nombre = input("Nombre del producto: ")
        descripcion = input("Descripción del producto: ")
        precio = float(input("Precio del producto: "))
        nuevo_producto = Producto(id, nombre, descripcion, precio)
        self.productos.anadir_producto(nuevo_producto)

    def buscar_producto(self):
        id = input("ID del producto a buscar: ")
        producto = self.productos.buscar_producto(id)
        if producto:
            print(f"Producto encontrado: ID: {producto.id}, Nombre: {producto.nombre}, Descripción: {producto.descripcion}, Precio: {producto.precio}")
        else:
            print("Producto no encontrado.")

    def eliminar_producto(self):
        id = input("ID del producto a eliminar: ")
        self.productos.eliminar_producto(id)

if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()