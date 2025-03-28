class Billete:

    def __init__(self,ref,origen,destino,fechaS,fechaL,horaL,cliente,nAsiento,equipaje,precio,descuento):  
        self.ref=ref
        self.origen=origen
        self.destino=destino
        self.fechaS=fechaS
        self.horaS=fechaS
        self.fechaL=fechaL
        self.horaL=fechaL
        self.cliente=cliente
        self.nAsiento=nAsiento
        self.equipaje=equipaje
        self.precio=precio
        self.descuento=descuento
@property       
def ref(self):
    return self.ref
@ref.setter
def ref(self,ref):
    self.ref=ref
    
@property
def origen(self):
    return self.origen
@origen.setter
def origen(self,origen):
    self.origen=origen
    
@property
def destino(self):
    return self.destino
@destino.setter
def destino(self,destino):
    self.destino=destino
    
@property
def fechaS(self):
    return self.fechaS
@fechaS.setter
def fechaS(self,fechaS):
    self.fechaS=fechaS
    
@property
def horaS(self):
    return self.horaS
@horaS.setter
def horaS(self,horaS):
    self.horaS=horaS
    
@property   
def fechaL(self):
    return self.fechaL
@fechaL.setter
def fechaL(self,fechaL):
    self.fechaL=fechaL
    
@property   
def horaL(self):
    return self.horaL
@fechaL.setter
def horaL(self,horaL):
    self.horaL=horaL
    
@property     
def cliente(self):
    return self.cliente
@cliente.setter
def cliente(self,cliente):
    self.cliente=cliente
    
@property    
def nAsiento(self):
    return self.nAsiento
@nAsiento.setter
def nAsiento(self,nAsiento):
    self.nAsiento=nAsiento
    
@property    
def equipaje(self):
    return self.equipaje
@equipaje.setter
def equipaje(self,equipaje):
    self.equipaje=equipaje
    
@property    
def precio(self):
    return self.precio
@precio.setter
def precio(self,precio):
    self.precio=precio
    
@property    
def descuento(self):
    return self.precio
@descuento.setter
def descuento(self,descuento):
    self.descuento=descuento

#operadores
def calcular_precio(self):
    # Calculate the final price after applying the discount
    return self.precio - (self.precio * self.descuento / 100)