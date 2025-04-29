class Figura:

	def __init__(self):
		self.id = 0
		self.nombre = ""
		self.lados = 0
		self.color = ""


	def __init__(self, id, nombre, lados, color):
		self.id = id
		self.nombre = nombre
		self.lados = lados
		self.color = color

@property
def id(self):
	return self.id

@id.setter
def id(self, nuevoId):
	self.id = nuevoId

@property
def nombre(self):
	return self.nombre

@nombre.setter
def nombre(self, nuevoNombre):
	self.nombre = nuevoNombre

@property
def lados(self):
	return self.lados

@lados.setter
def lados(self, nuevoLados):
	self.lados = nuevoLados

@property
def color(self):
	return self.color

@color.setter
def color(self, nuevoColor):
	self.color = nuevoColor
