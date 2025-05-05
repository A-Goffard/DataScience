from abc import ABC, abstractmethod

class Operaciones(ABC):

    @abstractmethod
    def area(self, id):
        pass   

    @abstractmethod
    def perimetro(self, id):
        pass
    
    