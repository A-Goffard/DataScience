import tkinter as tk
from tkinter import messagebox
from figura import Figura  # Importa la clase figura
from figuras import Listafiguras  # Importa la clase Listafiguras

class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de figuras")
        self.lista_figuras = Listafiguras()

        # Crear botones
        tk.Button(root, text="Agregar figura", command=self.agregar_figura).pack(pady=5)
        tk.Button(root, text="Buscar figura", command=self.buscar_figura).pack(pady=5)
        tk.Button(root, text="Eliminar figura", command=self.eliminar_figura).pack(pady=5)
        tk.Button(root, text="Mostrar Todos", command=self.mostrar_todos).pack(pady=5) 
        tk.Button(root, text="Existe", command=self.existe).pack(pady=5)

    def agregar_figura(self):
        # Ventana para agregar figura
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar figura")

        tk.Label(ventana, text="id:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(ventana, text="nombre:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(ventana, text="lados:").grid(row=2, column=0, padx=5, pady=5) 
        tk.Label(ventana, text="color:").grid(row=3, column=0, padx=5, pady=5)

        id_entry = tk.Entry(ventana)
        color_entry = tk.Entry(ventana)
        nombre_entry = tk.Entry(ventana) 
        lados_entry = tk.Entry(ventana)

        id_entry.grid(row=0, column=1, padx=5, pady=5)
        color_entry.grid(row=1, column=1, padx=5, pady=5)
        nombre_entry.grid(row=2, column=1, padx=5, pady=5)
        lados_entry.grid(row=3, column=1, padx=5, pady=5)

        def guardar_figura():
            id = id_entry.get()
            color = color_entry.get()
            nombre = nombre_entry.get()
            lados = lados_entry.get()
            if id and color and nombre:
                figura = Figura (id, color, nombre, lados)
                self.lista_figuras.agregar_figura(figura)
                messagebox.showinfo("Éxito", "figura agregado correctamente")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios")

        tk.Button(ventana, text="Guardar", command=guardar_figura).grid(row=4, column=0, columnspan=2, pady=10)

    def buscar_figura(self):
        # Ventana para buscar figura
        ventana = tk.Toplevel(self.root)
        ventana.title("Buscar figura")

        tk.Label(ventana, text="id:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = tk.Entry(ventana)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        def buscar():
            id = id_entry.get()
            figura = self.lista_figuras.buscar_figura(id)
            if figura:
                messagebox.showinfo("figura Encontrado", f"id: {figura.id}\nColor: {figura.color}\nnombre: {figura.nombre}\nlados: {figura.lados}")
            else:
                messagebox.showerror("Error", "figura no encontrado")

        tk.Button(ventana, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=10)

    def eliminar_figura(self):
        # Ventana para eliminar figura
        ventana = tk.Toplevel(self.root)
        ventana.title("Eliminar figura")

        tk.Label(ventana, text="id:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = tk.Entry(ventana)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        def eliminar():
            id = id_entry.get()
            if self.lista_figuras.eliminar_figura(id):
                messagebox.showinfo("Éxito", "figura eliminado correctamente")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "figura no encontrado")

        tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=1, column=0, columnspan=2, pady=10)

    def mostrar_todos(self):
        # Ventana para mostrar todos los figuras
        ventana = tk.Toplevel(self.root)
        ventana.title("Lista de figuras")

        figuras = self.lista_figuras.mostrar_todos()
        if figuras:
            for figura in figuras:
                tk.Label(ventana, text=f"id: {figura.id}, Color: {figura.color}, nombre: {figura.nombre}").pack(pady=2)
        else:
            tk.Label(ventana, text="No hay figuras en la lista").pack(pady=10)
            
    def existe(self):
        # Ventana para verificar si figura existe
        ventana = tk.Toplevel(self.root)
        ventana.title("Verificar existencia de figura")

        tk.Label(ventana, text="id:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = tk.Entry(ventana)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        def verificar():
            id = id_entry.get()
            if self.lista_figuras.existe(id):
                messagebox.showinfo("Éxito", "La figura existe")
            else:
                messagebox.showerror("Error", "La figura no existe")

        tk.Button(ventana, text="Verificar", command=verificar).grid(row=1, column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()
