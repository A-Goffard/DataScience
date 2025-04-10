class GestionCobros:
    precioHora = 2
    contador_id = 0

    def __init__(self):
        GestionCobros.contador_id += 1
        self.idCobro = GestionCobros.contador_id
        self.lista_cobros = [] 

    def crearCobro(self, matrCoche):
        if matrCoche not in self.lista_cobros:
            self.lista_cobros.append(matrCoche) 
    
    def calcularPrecio(self, horaEntrada, horaSalida):
        tiempoTotal = horaSalida - horaEntrada
        precio = tiempoTotal * self.precioHora
        return self.calcularBono(precio, horaEntrada, horaSalida)    

    def calcularBono(self, precio, horaEntrada, horaSalida):
        tiempoTotal = horaSalida - horaEntrada
        if tiempoTotal > 48:
            precio = 0
            self.avisoMAX()
        elif tiempoTotal > 8:
            precio = precio - (precio * 0.3) 
        elif tiempoTotal > 2:
            precio = precio - (precio * 0.2) 
        return precio

    def avisoMAX(self):
        print("El tiempo máximo de estancia es de 48 horas. Por favor, retire el coche.")
        return False