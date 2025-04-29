class Figuras:
	def __init__(self):
		self.figuras = []

	def agregar(self, figura):
		self.figuras.append(figura)
		print(f"figura con id {figura.id} añadido")

	def eliminar(self, id):
		figura = self.buscar(id)
		if figura:
			self.figuras.remove(figura)
		else:
			print(f"No existe el figura con id {id} en la lista")

	def buscar(self, id):
		for figura in self.figuras:
			if figura.id == id:
				print(f"Encontrado el figura con id {id}")
				return figura
		print(f"figura con id {id} no encontrado")
		return None

	def existe(self, id):
		for figura in self.figuras:
			if figura.id == id:
				return True
			else:
				return False

	def mostrar(self):
		resultado = []
		for figura in self.figuras:
			resultado.append((figura.id, figura.nombre, figura.lados, figura.color))
		return resultado
