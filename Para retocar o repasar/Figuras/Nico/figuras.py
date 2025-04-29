class Listafiguras:
    def __init__(self):
        self.lista_figuras = []

    def agregar_figura(self, figura):
        self.lista_figuras.append(figura)
        print("figura añadida")

    def buscar_figura(self, id):
        for figura in self.lista_figuras:
            if figura.id == id:
                return figura
        return None

    def eliminar_figura(self, id):
        figura = self.buscar_figura(id)
        if figura:
            self.lista_figuras.remove(figura)
            print("figura eliminado")
            return True
        else:
            print("figura no encontrado")
            return False

    def mostrar_todos(self):
        if not self.lista_figuras:
            print("No hay figuras")
            return []
        return self.lista_figuras 
    
    def existe(self, id):
        for figura in self.lista_figuras:
            if figura.id == id:
                return True
        return False