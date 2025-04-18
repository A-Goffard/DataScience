from coche import Coche

class ListaCoches:
	def __init__(self):
		self.lista_coches = []

	def anadir_coche(self, coche):
		self.lista_coches.append(coche)
		print(f"Coche con matrícula {coche.matricula} añadido")

	def eliminar_coche(self, matricula):
		coche = self.buscar_coche(matricula)
		if coche:
			self.lista_coches.remove(coche)
		else:
			print(f"No existe el coche con matrícula {matricula} en la lista")

	def buscar_coche(self, matricula):
		for coche in self.lista_coches:
			if coche.matricula == matricula:
				print(f"Encontrado el coche con matrícula {matricula}")
				return coche
		print(f"Coche con matrícula {matricula} no encontrado")
		return None

	def existe_coche(self, matricula):
		for coche in self.lista_coches:
			if coche.matricula == matricula:
				return True
			else:
				return False

	def mostrar_coches(self):
		for coche in self.lista_coches:
			print(f"Matrícula: {coche.matricula}, Marca: {coche.marca}, Modelo: {coche.modelo}, Color: {coche.color}, Tamaño: {coche.tamanio}")

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
