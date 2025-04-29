import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY, SUCCESS, DANGER, INFO
from plantas import Plantas
from planta import Planta

from tkinter import messagebox

class Principal:
    def __init__(self, root):
        self.lista_plantas = Plantas()
        self.root = root
        self.root.title("Sistema de Gestión de Plantas")
        self.root.geometry("500x500")

        # Campos de entrada
        self.id_label = ttk.Label(root, text="Id:", bootstyle=PRIMARY)
        self.id_label.grid(row=0, column=0, padx=10, pady=5, sticky="E")
        self.id_entry = ttk.Entry(root)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.especie_label = ttk.Label(root, text="Nombre:", bootstyle=PRIMARY)
        self.especie_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")
        self.especie_entry = ttk.Entry(root)  
        self.especie_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.color_label = ttk.Label(root, text="Color:", bootstyle=PRIMARY)
        self.color_label.grid(row=2, column=0, padx=10, pady=5, sticky="E")
        self.color_entry = ttk.Entry(root)  
        self.color_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.void_label = ttk.Label(root, text="")
        self.void_label.grid(row=3, column=0, padx=10, pady=5, sticky="E")


        # Botones
        self.agregar_button = ttk.Button(root, text="Añadir Planta", command=self.agregar, bootstyle="success-outline")
        self.agregar_button.grid(row=4, column=1, padx=10, pady=10, sticky="E")

        self.eliminar_button = ttk.Button(root, text="Eliminar Planta", command=self.eliminar, bootstyle="danger-outline")
        self.eliminar_button.grid(row=4, column=2, padx=10, pady=10, sticky="W")

        self.buscar_button = ttk.Button(root, text="Buscar Planta", command=self.buscar, bootstyle="info-outline")
        self.buscar_button.grid(row=5, column=1, padx=10, pady=10, sticky="E")

        self.mostrar_button = ttk.Button(root, text="Mostrar Plantas", command=self.mostrar, bootstyle="primary-outline")
        self.mostrar_button.grid(row=5, column=2, padx=10, pady=10, sticky="W")

        # Área de texto para mostrar resultados
        self.resultado_text = tk.Text(root, height=10, width=75) 
        self.resultado_text.grid(row=6, column=0, columnspan=3, padx=15, pady=10)

    def agregar(self):
        self.resultado_text.delete(1.0, tk.END)
        id = self.id_entry.get()
        especie = self.especie_entry.get()
        color = self.color_entry.get()

        if id and especie and color:
            if self.lista_plantas.buscarPlanta(id):
                self.resultado_text.insert(tk.END, f"Error: Ya existe una planta con ID {id}.\n")
            else:
                planta = Planta(id, especie, color)
                self.lista_plantas.agregarPlanta(planta)
                self.resultado_text.insert(tk.END, f"Planta con ID {id} añadida.\n")
        else:
            self.resultado_text.insert(tk.END, "Error: Todos los campos son obligatorios.\n")

    def eliminar(self):
        self.resultado_text.delete(1.0, tk.END)
        id = self.id_entry.get()
        if id:
            if self.lista_plantas.eliminarPlanta(id):
                self.resultado_text.insert(tk.END, f"Planta con ID {id} eliminada.\n")
            else:
                self.resultado_text.insert(tk.END, f"Error: No existe la planta con ID {id}.\n")
        else:
            self.resultado_text.insert(tk.END, "Error: Debe ingresar un ID.\n")

    def buscar(self):
        self.resultado_text.delete(1.0, tk.END)
        id = self.id_entry.get()
        if id:
            planta = self.lista_plantas.buscarPlanta(id)
            if planta:
                self.especie_entry.delete(0, tk.END)
                self.especie_entry.insert(0, planta.especie)
                self.color_entry.delete(0, tk.END)
                self.color_entry.insert(0, planta.color)
                self.resultado_text.insert(tk.END, f"Se encontró la planta con ID: {planta.id}, Especie: {planta.especie}, Color: {planta.color}\n")
            else:
                self.resultado_text.insert(tk.END, f"No se encontró la planta con ID {id}.\n")
        else:
            self.resultado_text.insert(tk.END, "Error: Debe ingresar un ID.\n")

    def mostrar(self):
        self.resultado_text.delete(1.0, tk.END)
        plantas = self.lista_plantas.mostrarPlanta()
        if plantas:
            for planta in plantas:
                self.resultado_text.insert(tk.END, f"ID: {planta.id}, Especie: {planta.especie}, Color: {planta.color}\n")
        else:
            self.resultado_text.insert(tk.END, "No hay plantas en la lista.\n")

if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")  # Ventana con tema moderno
    app = Principal(root)
    root.mainloop()
