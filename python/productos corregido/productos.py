from producto import Producto

class Productos:
    def __init__(self):
        self.lista_productos = []

    def anadir_producto(self, producto):
        self.lista_productos.append(producto)
        print("Producto agregado correctamente.")

    def buscar_producto(self, id):
        for producto in self.lista_productos:
            if producto.id == id:
                return producto
        return None

    def eliminar_producto(self, id):
        producto = self.buscar_producto(id)
        if producto:
            self.lista_productos.remove(producto)
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def existe_producto(self, id):
        return any(producto.id == id for producto in self.lista_productos)

    def mostrar_productos(self):
        if not self.lista_productos:
            print("No hay productos en la lista.")
        else:
            print("\nLista de productos:")
            for producto in self.lista_productos:
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Descripción: {producto.descripcion}, Precio: {producto.precio}")