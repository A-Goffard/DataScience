from planta import Planta

class Plantas:
	def __init__(self):
		self.lista_plantas = []

	def agregarPlanta(self, planta):
		self.lista_plantas.append(planta)
		print(f"Planta con id {planta.id} añadida")

	def eliminarPlanta(self, id):
		planta = self.buscar(id)
		if planta:
			self.lista_plantas.remove(planta)
		else:
			print(f"No existe la planta con id {id} en la lista")

	def buscarPlanta(self, id):
		for planta in self.lista_plantas:
			if planta.id == id:
				print(f"Planta con id {id} encontrada")
				return planta
		print(f"Planta con id {id} no encontrada")
		return None

	def existePlanta(self, id):
		for planta in self.lista_plantas:
			if planta.id == id:
				return True
			else:
				return False

	def mostrarPlanta(self):
		resultado = []
		for planta in self.lista_plantas:
			resultado.append((planta.id, planta.especie, planta.color))
		return resultado