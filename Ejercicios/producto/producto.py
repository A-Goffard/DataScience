class Producto:
    def __init__(self, id, nombre, descripcion, precio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
    
    def __str__(self):
        return print(f"ID: {self.id} - {self.nombre}-{self.descripcion}-{self.precio}")
    
    def get_nombre(self):
        return self.nombre
    
    def get_descripcion(self):
        return self.descripcion
    
    def get_precio(self):
        return self.precio
    
    def set_id(self, id):
        self._id = id
        
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_descripcion(self, descripcion):
        self._descripcion = descripcion
    
    def set_precio(self, precio):
        self._precio = precio