class Figura:
	def __init__(self, id, nombre, lados, color):
		self._matricula = id
		self._nombre = nombre
		self._lados = lados
		self._color = color

	@property
	def id(self):
		return self._matricula

	@id.setter
	def id(self, nueva_matricula):
		self._matricula = nueva_matricula

	@property
	def nombre(self):
		return self._nombre

	@nombre.setter
	def nombre(self, nueva_nombre):
		self._nombre = nueva_nombre

	@property
	def lados(self):
		return self._lados

	@lados.setter
	def lados(self, nuevo_lados):
		self._lados = nuevo_lados

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, nuevo_color):
		self._color = nuevo_color
