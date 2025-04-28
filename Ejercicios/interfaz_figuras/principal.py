import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk

from figura import Figura
from figuras import Figuras

class InterfazGrafica:
	def __init__(self, root):
		self.figuras = Figuras()
		self.root = root
		self.root.title("Gestión de Figuras")
		self.root.geometry("335x440")
		self.root.configure(bg="#ebdef0")  # Cambiar el color de fondo a rosa pálido

		# Campos de entrada
		self.id_label = ttk.Label(root, text="Id:", bootstyle="info", background="#ebdef0")
		self.id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
		self.id_entry = ttk.Entry(root)  # Elimina bootstyle="rounded"
		self.id_entry.grid(row=0, column=1, padx=10, pady=5)

		self.marca_label = ttk.Label(root, text="Nombre:", bootstyle="info", background="#ebdef0")
		self.marca_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
		self.marca_entry = ttk.Entry(root)
		self.marca_entry.grid(row=1, column=1, padx=10, pady=5)

		self.modelo_label = ttk.Label(root, text="Lados:", bootstyle="info", background="#ebdef0")
		self.modelo_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
		self.modelo_entry = ttk.Entry(root)
		self.modelo_entry.grid(row=2, column=1, padx=10, pady=5)

		self.color_label = ttk.Label(root, text="Color:", bootstyle="info", background="#ebdef0")
		self.color_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
		self.color_entry = ttk.Entry(root)  # Elimina bootstyle="rounded"
		self.color_entry.grid(row=3, column=1, padx=10, pady=5)

		# Botones
		self.agregar_button = ttk.Button(root, text="Añadir Figura", command=self.agregar, bootstyle="success-outline")
		self.agregar_button.grid(row=5, column=0, padx=10, pady=10)

		self.eliminar_button = ttk.Button(root, text="Eliminar Figura", command=self.eliminar, bootstyle="danger-outline")
		self.eliminar_button.grid(row=5, column=1, padx=10, pady=10)

		self.buscar_button = ttk.Button(root, text="Buscar Figura", command=self.buscar, bootstyle="info-outline")
		self.buscar_button.grid(row=6, column=0, padx=10, pady=10)

		self.mostrar_button = ttk.Button(root, text="Mostrar Figuras", command=self.mostrar, bootstyle="primary-outline")
		self.mostrar_button.grid(row=6, column=1, padx=10, pady=10)

		# Área de texto para mostrar resultados
		self.resultado_text = tk.Text(root, height=10, width=50)  # Cambia ttk.Text a tk.Text y elimina bootstyle
		self.resultado_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

	def agregar(self):
		id = self.id_entry.get()
		nombre = self.marca_entry.get()
		lados = self.modelo_entry.get()
		color = self.color_entry.get()

		if id and nombre and lados and color:
			figura = Figura(id, nombre, lados, color)
			self.figuras.agregar(figura)
			self.resultado_text.insert(tk.END, f"Figura con Id {id} añadida.\n")
		else:
			self.resultado_text.insert(tk.END, "Error: Todos los campos son obligatorios.\n")

	def eliminar(self):
		id = self.id_entry.get()
		if id:
			figura = self.figuras.buscar(id)
			if figura:
				self.figuras.eliminar(id)
				self.resultado_text.insert(tk.END, f"Figura con Id {id} eliminada.\n")
			else:
				self.resultado_text.insert(tk.END, f"Error: No existe la figura con Id {id}.\n")
		else:
			self.resultado_text.insert(tk.END, "Error: Debe ingresar una Id.\n")

	def buscar(self):
		id = self.id_entry.get()
		if id:
			figura = self.figuras.buscar(id)
			if figura:
				self.resultado_text.insert(tk.END, f"Id: {figura.id}, Nombre: {figura.nombre}, Lados: {figura.lados}, Color: {figura.color}\n")
			else:
				self.resultado_text.insert(tk.END, f"No se encontró la figura con Id {id}.\n")
		else:
			self.resultado_text.insert(tk.END, "Error: Debe ingresar una Id.\n")

	def mostrar(self):
		figuras = self.figuras.obtener()
		self.resultado_text.delete(1.0, tk.END)
		if figuras:
			for figura in figuras:
				self.resultado_text.insert(tk.END, f"Id: {figura['id']}, Nombre: {figura['nombre']}, Lados: {figura['lados']}, Color: {figura['color']}\n")
		else:
			self.resultado_text.insert(tk.END, "No hay figuras en la lista.\n")

if __name__ == "__main__":
	root = ttk.Window(themename="cosmo")  # Ventana con tema moderno
	app = InterfazGrafica(root)
	root.mainloop()
