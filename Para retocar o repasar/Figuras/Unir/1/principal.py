import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY, SUCCESS, DANGER, INFO, W
from figuras import Figuras
from figura import Figura
import tkinter as tk  # Import tkinter y alias como tk

class InterfazGrafica:
	def __init__(self, root):
		self.figuras = Figuras()
		self.root = root
		self.root.title("Gestión de Figuras")
		self.root.geometry("720x640")

		# Campos de entrada
		self.id_label = ttk.Label(root, text="Id:", bootstyle="primary")
		self.id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
		self.id_entry = ttk.Entry(root)  # Elimina bootstyle="rounded"
		self.id_entry.grid(row=0, column=1, padx=10, pady=5)

		self.nombre_label = ttk.Label(root, text="Nombre:", bootstyle="primary")
		self.nombre_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
		self.nombre_entry = ttk.Entry(root)  # Elimina bootstyle="rounded"
		self.nombre_entry.grid(row=1, column=1, padx=10, pady=5)

		self.lados_label = ttk.Label(root, text="lados:", bootstyle="primary")
		self.lados_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
		self.lados_entry = ttk.Entry(root)  # Elimina bootstyle="rounded"
		self.lados_entry.grid(row=2, column=1, padx=10, pady=5)

		self.color_label = ttk.Label(root, text="Color:", bootstyle="primary")
		self.color_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
		self.color_entry = ttk.Entry(root)  # Elimina bootstyle="rounded"
		self.color_entry.grid(row=3, column=1, padx=10, pady=5)

		# Botones
		self.agregar_button = ttk.Button(root, text="Añadir figura", command=self.agregar_figura, bootstyle="success-outline")
		self.agregar_button.grid(row=5, column=0, padx=10, pady=10)

		self.eliminar_button = ttk.Button(root, text="Eliminar figura", command=self.eliminar_figura, bootstyle="danger-outline")
		self.eliminar_button.grid(row=5, column=1, padx=10, pady=10)

		self.buscar_button = ttk.Button(root, text="Buscar figura", command=self.buscar_figura, bootstyle="info-outline")
		self.buscar_button.grid(row=6, column=0, padx=10, pady=10)

		self.mostrar_button = ttk.Button(root, text="Mostrar figuras", command=self.mostrar_figuras, bootstyle="primary-outline")
		self.mostrar_button.grid(row=6, column=1, padx=10, pady=10)

		# Área de texto para mostrar resultados
		self.resultado_text = tk.Text(root, height=12, width=85)  # Cambia ttk.Text a tk.Text y elimina bootstyle
		self.resultado_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

	def agregar_figura(self):
		id = self.id_entry.get()
		nombre = self.nombre_entry.get()
		lados = self.lados_entry.get()
		color = self.color_entry.get()

		if id and nombre and lados and color:
			figura = Figura(id, nombre, lados, color)
			self.figuras.agregar_figura(figura)
			self.resultado_text.insert(tk.END, f"figura con Id {id} añadido.\n")
		else:
			self.resultado_text.insert(tk.END, "Error: Todos los campos son obligatorios.\n")

	def eliminar_figura(self):
		id = self.id_entry.get()
		if id:
			figura = self.figuras.buscar_figura(id)
			if figura:
				self.figuras.eliminar_figura(id)
				self.resultado_text.insert(tk.END, f"figura con Id {id} eliminado.\n")
			else:
				self.resultado_text.insert(tk.END, f"Error: No existe el figura con Id {id}.\n")
		else:
			self.resultado_text.insert(tk.END, "Error: Debe ingresar una Id.\n")

	def buscar_figura(self):
		id = self.id_entry.get()
		if id:
			figura = self.figuras.buscar_figura(id)
			if figura:
				self.resultado_text.insert(tk.END, f"Id: {figura.id}, nombre: {figura.nombre}, lados: {figura.lados}, Color: {figura.color}\n")
			else:
				self.resultado_text.insert(tk.END, f"No se encontró el figura con Id {id}.\n")
		else:
			self.resultado_text.insert(tk.END, "Error: Debe ingresar una Id.\n")

	def mostrar_figuras(self):
		figuras = self.figuras.obtener_figuras()
		self.resultado_text.delete(1.0, tk.END)
		if figuras:
			for figura in figuras:
				self.resultado_text.insert(tk.END, f"Id: {figura['id']}, nombre: {figura['nombre']}, lados: {figura['lados']}, Color: {figura['color']}\n")
		else:
			self.resultado_text.insert(tk.END, "No hay figuras en la lista.\n")

if __name__ == "__main__":
	root = ttk.Window(themename="cosmo")  # Ventana con tema moderno
	app = InterfazGrafica(root)
	root.mainloop()
