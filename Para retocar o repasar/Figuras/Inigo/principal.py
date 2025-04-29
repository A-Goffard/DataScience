import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY, SUCCESS, DANGER, INFO
from figuras import Figuras
from figura import Figura

from tkinter import messagebox

class Principal:
    def __init__(self, root):
        self.lista_figuras = Figuras()
        self.root = root
        self.root.title("Sistema de Gestión de Figuras")
        self.root.geometry("500x500")

        # Campos de entrada
        self.id_label = ttk.Label(root, text="Id:", bootstyle=PRIMARY)
        self.id_label.grid(row=0, column=0, padx=10, pady=5, sticky="E")
        self.id_entry = ttk.Entry(root)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.nombre_label = ttk.Label(root, text="Nombre:", bootstyle=PRIMARY)
        self.nombre_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")
        self.nombre_entry = ttk.Entry(root)  
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.lados_label = ttk.Label(root, text="Lados:", bootstyle=PRIMARY)
        self.lados_label.grid(row=2, column=0, padx=10, pady=5, sticky="E")
        self.lados_entry = ttk.Entry(root) 
        self.lados_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.color_label = ttk.Label(root, text="Color:", bootstyle=PRIMARY)
        self.color_label.grid(row=3, column=0, padx=10, pady=5, sticky="E")
        self.color_entry = ttk.Entry(root)  
        self.color_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.void_label = ttk.Label(root, text="")
        self.void_label.grid(row=4, column=0, padx=10, pady=5, sticky="E")


        # Botones
        self.agregar_button = ttk.Button(root, text="Añadir Figura", command=self.agregar, bootstyle="success-outline")
        self.agregar_button.grid(row=5, column=1, padx=10, pady=10, sticky="E")

        self.eliminar_button = ttk.Button(root, text="Eliminar Figura", command=self.eliminar, bootstyle="danger-outline")
        self.eliminar_button.grid(row=5, column=2, padx=10, pady=10, sticky="W")

        self.buscar_button = ttk.Button(root, text="Buscar Figura", command=self.buscar, bootstyle="info-outline")
        self.buscar_button.grid(row=6, column=1, padx=10, pady=10, sticky="E")

        self.mostrar_button = ttk.Button(root, text="Mostrar Figuras", command=self.mostrar, bootstyle="primary-outline")
        self.mostrar_button.grid(row=6, column=2, padx=10, pady=10, sticky="W")

        # Área de texto para mostrar resultados
        self.resultado_text = tk.Text(root, height=10, width=75) 
        self.resultado_text.grid(row=7, column=0, columnspan=3, padx=15, pady=10)

    def agregar(self):
        self.resultado_text.delete(1.0, tk.END)
        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        lados = self.lados_entry.get()
        color = self.color_entry.get()

        if id and nombre and lados and color:
            figura = Figura(id, nombre, lados, color)
            self.lista_figuras.agregar(figura)
            self.resultado_text.insert(tk.END, f"Figura con matrícula {id} añadido.\n")
        else:
            self.resultado_text.insert(tk.END, "Error: Todos los campos son obligatorios.\n")

    def eliminar(self):
        self.resultado_text.delete(1.0, tk.END)
        id = self.id_entry.get()
        if id:
            figura = self.lista_figuras.buscar(id)
            if figura:
                respuesta = messagebox.askyesno("Confirmar", f"¿Estás seguro de que deseas eliminar la figura con ID {id} ?")
                if respuesta == tk.YES:
                    self.lista_figuras.eliminar(id)
                    self.resultado_text.insert(tk.END, f"Figura con ID {id} eliminada.\n")
                    # print("¡Elemento eliminado!")
                else:
                    self.resultado_text.insert(tk.END, "Eliminación cancelada.\n")
                    # print("Eliminación cancelada.")
                    return True
            else:
                self.resultado_text.insert(tk.END, f"Error: No existe el figura con matrícula {id}.\n")
        else:
            self.resultado_text.insert(tk.END, "Error: Debe ingresar una matrícula.\n")
    
    def buscar(self):
        self.resultado_text.delete(1.0, tk.END)
        id = self.id_entry.get()
        if id:        
            figura = self.lista_figuras.buscar(id)
            if figura:
                self.nombre_entry.delete(0, tk.END)
                self.nombre_entry.insert(0, figura.nombre)
                self.lados_entry.delete(0, tk.END)
                self.lados_entry.insert(0, figura.lados)
                self.color_entry.delete(0, tk.END)
                self.color_entry.insert(0, figura.color)
                self.resultado_text.insert(tk.END, f"Se encontró la figura con ID: {figura.id}, Nombre: {figura.nombre}, Lados: {figura.lados}, Color: {figura.color}\n")
            else:
                self.resultado_text.insert(tk.END, f"No se encontró la figura con ID {id}.\n")
        else:
            self.resultado_text.insert(tk.END, "Error: Debe ingresar un ID.\n")

    def mostrar(self):
            figuras = self.lista_figuras.mostrar()
            self.resultado_text.delete(1.0, tk.END)
            if figuras:
                for figura in figuras:
                    self.resultado_text.insert(tk.END, f"ID: {figura.id}, Nombre: {figura.nombre}, Lados: {figura.lados}, Color: {figura.color}\n")
            else:
                self.resultado_text.insert(tk.END, "No hay figuras en la lista.\n")

if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")  # Ventana con tema moderno
    app = Principal(root)
    root.mainloop()
