from coche import Coche

class ListaCoches:
	def __init__(self):
		self.lista_coches = []
		self.mensajes = []  # Lista para almacenar mensajes

	def anadir_coche(self, coche):
		self.lista_coches.append(coche)
		self.mensajes.append(f"Coche con matrícula {coche.matricula} añadido")

	def eliminar_coche(self, matricula):
		coche = self.buscar_coche(matricula)
		if coche:
			self.lista_coches.remove(coche)
			self.mensajes.append(f"Coche con matrícula {matricula} eliminado")
		else:
			self.mensajes.append(f"No existe el coche con matrícula {matricula} en la lista")

	def buscar_coche(self, matricula):
		for coche in self.lista_coches:
			if coche.matricula == matricula:
				self.mensajes.append(f"Encontrado el coche con matrícula {matricula}")
				return coche
		self.mensajes.append(f"Coche con matrícula {matricula} no encontrado")
		return None

	def existe_coche(self, matricula):
		for coche in self.lista_coches:
			if coche.matricula == matricula:
				return True
		return False

	def mostrar_coches(self):
		for coche in self.lista_coches:
			self.mensajes.append(
				f"Matrícula: {coche.matricula}, Marca: {coche.marca}, Modelo: {coche.modelo}, Color: {coche.color}, Tamaño: {coche.tamanio}"
			)

	def obtener_coches(self):
		return [
			{
				"matricula": coche.matricula,
				"marca": coche.marca,
				"modelo": coche.modelo,
				"color": coche.color,
				"tamanio": coche.tamanio,
			}
			for coche in self.lista_coches
		]

	def obtener_mensajes(self):
		return self.mensajes

	def limpiar_mensajes(self):
		self.mensajes = []
