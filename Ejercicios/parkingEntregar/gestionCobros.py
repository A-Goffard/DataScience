from coche import Coche
from listaCoches import ListaCoches

class GestionCobros:
    precioHora = 2

    def __init__(self,idCobro):
        self.idCobro = idCobro

    def crearCobro(self, idCobro, matrCoche,horaEntrada,horaSalida):
        return self.calcularPrecio(horaEntrada, horaSalida)
    
    def calcularPrecio(self, horaEntrada, horaSalida):
        tiempoTotal = horaSalida - horaEntrada
        precio = tiempoTotal * self.precioHora
        return self.calcularBono(self,precio, horaEntrada, horaSalida)    

    def calcularBono(self, precio, horaEntrada, horaSalida):
        
        tiempoTotal = horaSalida - horaEntrada
        if (tiempoTotal > 48):
            precio=0
            self.avisoMAX()
        elif tiempoTotal > 8:
            precio = precio - (precio * 0.3) #descuento del 30%
        elif tiempoTotal > 2:
            precio = precio - (precio * 0.2) #descuento del 20%
        else:
            precio= precio *1

        return precio

    def avisoMAX(self):
        print("El tiempo máximo de estancia es de 48 horas. Por favor, retire el coche.")
        return False    