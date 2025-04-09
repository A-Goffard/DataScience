from producto import Producto
class Productos:
    def __init__(self):
        self.lista_productos = []

    def anadir_producto(self, producto):
        if not self.existe_producto(producto.id):
            self.lista_productos.append(producto)
            print("Producto añadido!!")
        else:
            print("El producto con ese id ya existe")

    def eliminar_producto(self, id):
        for producto in self.lista_productos:
            if producto.id == id:
                self.lista_productos.remove(producto)
                print("Producto eliminado")
            else:
                print("Producto no encontrado")
                
    def buscar_producto(self, id):
        for producto in self.lista_productos:
            if producto.id == id:
                return producto
            else:
                print("Producto no encontrado")

    def existe_producto(self, id):
        for producto in self.lista_productos:
            if producto.id == id:
                print("El producto existe")
            else:
                print("El producto no existe")

    def mostrar_lista_productos(self):
        if  len(self.lista_productos)==0:
            print("La lista está vacía")
        else:
            for producto in self.lista_productos:
                print(producto.id,"-", producto.nombre,"-", producto.precio,"-",  producto.descripcion)
                
    