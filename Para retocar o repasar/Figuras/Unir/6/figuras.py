class Figuras:

	def __init__ (self):
		self.lista_figuras=[ ]

	def anadir_figura(self,figura):
		self.lista_figuras.append(figura)

	def eliminar_figura(self,id):
		if self.existe_figura(id):
			self.lista_figuras.remove(self.buscar_figura(id))
			return print("Figura eliminada correctamente.")
		return print("Figura no encontrada.")


	def buscar_figura(self,id):
		for figura in self.lista_figuras:
			if figura.id==id:
				return figura
		return None

	def existe_figura (self, id):
		for figura in self.lista_figuras:
			if figura.id == id:
				return True
		return False

	def mostrar_lista_figuras(self):
		for figura in self.lista_figuras:
			print(f"ID: {figura.id} Nombre: {figura.nombre} Lados: {figura.lados} Color: {figura.color}")

