import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ListaCoches import ListaCoches
from coche import Coche
import tkinter as tk  

class InterfazGrafica:
	def __init__(self, root):
		self.lista_coches = ListaCoches()
		self.root = root
		self.root.title("Gestión de Coches")
		self.root.geometry("355x550")

		# Campos de entrada
		self.matricula_label = ttk.Label(root, text="Matrícula:", bootstyle="primary")
		self.matricula_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
		self.matricula_entry = ttk.Entry(root)
		self.matricula_entry.grid(row=0, column=1, padx=10, pady=5)

		self.marca_label = ttk.Label(root, text="Marca:", bootstyle="primary")
		self.marca_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
		self.marca_entry = ttk.Entry(root)
		self.marca_entry.grid(row=1, column=1, padx=10, pady=5)

		self.modelo_label = ttk.Label(root, text="Modelo:", bootstyle="primary")
		self.modelo_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
		self.modelo_entry = ttk.Entry(root)
		self.modelo_entry.grid(row=2, column=1, padx=10, pady=5)

		self.color_label = ttk.Label(root, text="Color:", bootstyle="primary")
		self.color_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
		self.color_entry = ttk.Entry(root)
		self.color_entry.grid(row=3, column=1, padx=10, pady=5)

		self.tamanio_label = ttk.Label(root, text="Tamaño:", bootstyle="primary")
		self.tamanio_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
		self.tamanio_entry = ttk.Entry(root)
		self.tamanio_entry.grid(row=4, column=1, padx=10, pady=5)

		# Botones
		self.anadir_button = ttk.Button(root, text="Añadir Coche", command=self.anadir_coche, bootstyle="success-outline")
		self.anadir_button.grid(row=5, column=0, padx=10, pady=10)

		self.eliminar_button = ttk.Button(root, text="Eliminar Coche", command=self.eliminar_coche, bootstyle="danger-outline")
		self.eliminar_button.grid(row=5, column=1, padx=10, pady=10)

		self.buscar_button = ttk.Button(root, text="Buscar Coche", command=self.buscar_coche, bootstyle="info-outline")
		self.buscar_button.grid(row=6, column=0, padx=10, pady=10)

		self.mostrar_button = ttk.Button(root, text="Mostrar Coches", command=self.mostrar_coches, bootstyle="primary-outline")
		self.mostrar_button.grid(row=6, column=1, padx=10, pady=10)

		# Área de texto para mostrar resultados
		self.resultado_text = tk.Text(root, height=10, width=40)
		self.resultado_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

	def anadir_coche(self):
		matricula = self.matricula_entry.get()
		marca = self.marca_entry.get()
		modelo = self.modelo_entry.get()
		color = self.color_entry.get()
		tamanio = self.tamanio_entry.get()

		if matricula and marca and modelo and color and tamanio:
			coche = Coche(matricula, marca, modelo, color, tamanio)
			self.lista_coches.anadir_coche(coche)
			self.resultado_text.insert(tk.END, f"Coche con matrícula {matricula} añadido.\n")
		else:
			self.resultado_text.insert(tk.END, "Error: Todos los campos son obligatorios.\n")

	def confirmar_eliminacion(self, matricula):
		"""Muestra un cuadro de confirmación personalizado."""
		confirmacion = tk.Toplevel(self.root)
		confirmacion.title("Confirmar Eliminación")
		confirmacion.geometry("300x150")
		confirmacion.transient(self.root)
		confirmacion.grab_set()

		# Etiqueta de mensaje
		mensaje = ttk.Label(confirmacion, text=f"¿Eliminar coche con matrícula {matricula}?", bootstyle="primary")
		mensaje.pack(pady=10)

		 # Contenedor para los botones
		boton_frame = ttk.Frame(confirmacion)
		boton_frame.pack(pady=10)

		# Botones de confirmación y cancelación
		boton_si = ttk.Button(boton_frame, text="Sí", bootstyle="success-outline", 
		                      command=lambda: self.eliminar_coche_confirmado(matricula, confirmacion))
		boton_si.pack(side=tk.LEFT, padx=5)  # Reduce el padding horizontal

		boton_no = ttk.Button(boton_frame, text="No", bootstyle="danger-outline", 
		                      command=confirmacion.destroy)
		boton_no.pack(side=tk.LEFT, padx=5)  # Reduce el padding horizontal

	def eliminar_coche_confirmado(self, matricula, ventana):
		"""Elimina el coche después de la confirmación."""
		coche = self.lista_coches.buscar_coche(matricula)
		if coche:
			self.lista_coches.eliminar_coche(matricula)
			self.resultado_text.insert(tk.END, f"Coche con matrícula {matricula} eliminado.\n")
		else:
			self.resultado_text.insert(tk.END, f"Error: No existe el coche con matrícula {matricula}.\n")
		ventana.destroy()

	def eliminar_coche(self):
		matricula = self.matricula_entry.get()
		if matricula:
			self.confirmar_eliminacion(matricula)
		else:
			self.resultado_text.insert(tk.END, "Error: Debe ingresar una matrícula.\n")

	def buscar_coche(self):
		matricula = self.matricula_entry.get()
		if matricula:
			coche = self.lista_coches.buscar_coche(matricula)
			if coche:
				self.resultado_text.insert(tk.END, f"Matrícula: {coche.matricula}, Marca: {coche.marca}, Modelo: {coche.modelo}, Color: {coche.color}, Tamaño: {coche.tamanio}\n")
			else:
				self.resultado_text.insert(tk.END, f"No se encontró el coche con matrícula {matricula}.\n")
		else:
			self.resultado_text.insert(tk.END, "Error: Debe ingresar una matrícula.\n")

	def mostrar_coches(self):
		coches = self.lista_coches.obtener_coches()
		self.resultado_text.delete(1.0, tk.END)
		if coches:
			for coche in coches:
				self.resultado_text.insert(tk.END, f"Matrícula: {coche['matricula']}, Marca: {coche['marca']}, Modelo: {coche['modelo']}, Color: {coche['color']}, Tamaño: {coche['tamanio']}\n")
		else:
			self.resultado_text.insert(tk.END, "No hay coches en la lista.\n")

if __name__ == "__main__":
	root = tk.Tk() 
	style = ttk.Style(theme="cosmo")  
	app = InterfazGrafica(root)
	root.mainloop()

