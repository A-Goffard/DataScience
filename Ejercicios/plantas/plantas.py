from planta import Planta

class Plantas:
    
    def __init__(self):
        self.lista_plantas=[]
        
    def agregarPlanta(self,planta):
        self.lista_plantas.append(planta)
        
    def eliminarPlanta(self, id):
        planta = self.buscarPlanta(id)
        if planta:
            self.lista_plantas.remove(planta)
            return True
        return False

    def buscarPlanta(self, id):
        for planta in self.lista_plantas:
            if planta.id == id:
                return planta
        return None

    def mostrarPlanta(self):
        return self.lista_plantas
    
    def existePlanta(self,planta):
        return planta in self.lista_plantas