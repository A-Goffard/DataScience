from abc import ABC, abstractmethod

class UsuariosABC(ABC):

    @abstractmethod
    def buscar(self, clave):
        pass

    @abstractmethod
    def anadir(self, usuario):
        pass

    @abstractmethod
    def eliminar(self, clave):
        pass

    @abstractmethod
    def mostrarTodos(self):
        pass
