from figura import Figura

class Figuras:
    #Constructor objetos de clase gestora de dominio
    #Creamos lista vacia listaFiguras    
    def __init__(self):
        self._listaFiguras = []
    
    #Metodos gestores
    def agregar(self, figura):
        if figura not in self._listaFiguras:
            print(f"La figura de id {figura.id} fue añadida con éxito en la lista de figuras")                     
            return self._listaFiguras.append(figura)
        else:
            return None

    def eliminar(self, id):
        figura = self.buscar(id)
        if self.existe(figura):
            self._listaFiguras.remove(figura)
            print(f"La figura de id {figura.id} fue borrada con éxito de la lista de figuras")                     
        else:
            print(f"No fue posible borrar la figura de id {id} de la lista de figuras")

    def buscar(self, id):
        for figura in self._listaFiguras:
            if figura.id == id:
                return figura
        return None

    def existe(self, figura):
        if figura is not None:
            if figura in self._listaFiguras:
                return True
            return False
        return False

    def mostrar(self):
        if len(self._listaFiguras)>0:
            print("--- Lista de Figuras ---")
            for figura in self._listaFiguras:
                print(f"Figura con id {figura.id} es {figura.nombre} de {figura.lados} lados de color {figura.color}")                
        else:
            print("Lista de Figuras está vacía.")
        return self._listaFiguras
           
