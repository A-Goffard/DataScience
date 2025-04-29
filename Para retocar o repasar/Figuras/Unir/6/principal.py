import tkinter as tk
from tkinter import simpledialog, messagebox
from figura import Figura
from figuras import Figuras

class Principal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestor de Figuras")
        self.root.geometry("500x500")
        self.root.configure(bg="#e6f2ff")  
        self.figuras = Figuras()
        self.crear_menu()

    def crear_menu(self):
        # Título principal
        titulo = tk.Label(
            self.root,
            text="Gestor de Figuras",
            font=("Verdana", 24, "bold"),
            bg="#e6f2ff",
            fg="#003366"
        )
        titulo.pack(pady=20)

        # Subtítulo
        subtitulo = tk.Label(
            self.root,
            text="Seleccione una opción",
            font=("Verdana", 14),
            bg="#e6f2ff",
            fg="#004080"
        )
        subtitulo.pack(pady=10)

        # Frame de botones
        frame_botones = tk.Frame(self.root, bg="#e6f2ff")
        frame_botones.pack(pady=20)

        # Estilo de botones
        estilo_boton = {
            "font": ("Verdana", 12),
            "bg": "#007acc",
            "fg": "white",
            "activebackground": "#005f99",
            "activeforeground": "white",
            "width": 25,
            "height": 2,
            "bd": 0,
            "relief": "ridge",
            "cursor": "hand2"
        }

        # Botones
        tk.Button(frame_botones, text="Agregar Figura", command=self.agregar, **estilo_boton).pack(pady=10)
        tk.Button(frame_botones, text="Eliminar Figura", command=self.eliminar, **estilo_boton).pack(pady=10)
        tk.Button(frame_botones, text="Buscar Figura", command=self.buscar, **estilo_boton).pack(pady=10)
        tk.Button(frame_botones, text="Mostrar Figuras", command=self.mostrar, **estilo_boton).pack(pady=10)

    def agregar(self):
        id = simpledialog.askstring("Agregar Figura", "ID:")
        nombre = simpledialog.askstring("Agregar Figura", "Nombre:")
        lados = simpledialog.askinteger("Agregar Figura", "Número de lados:")
        color = simpledialog.askstring("Agregar Figura", "Color:")
        if id and nombre and lados is not None and color:
            figura = Figura(id, nombre, lados, color)
            self.figuras.agregar(figura)
            messagebox.showinfo("Éxito", "Figura agregada correctamente.")

    def eliminar(self):
        id = simpledialog.askstring("Eliminar Figura", "ID de la figura a eliminar:")
        figura_a_eliminar = next((figura for figura in self.figuras.figuras if figura.id == id), None)
        if figura_a_eliminar:
            self.figuras.eliminar(figura_a_eliminar)
            messagebox.showinfo("Éxito", "Figura eliminada.")
        else:
            messagebox.showerror("Error", "Figura no encontrada.")

    def buscar(self):
        id = simpledialog.askstring("Buscar Figura", "ID de la figura a buscar:")
        figura_encontrada = next((figura for figura in self.figuras.figuras if figura.id == id), None)
        if figura_encontrada:
            messagebox.showinfo("Figura encontrada", str(figura_encontrada))
        else:
            messagebox.showerror("Error", "Figura no encontrada.")

    def mostrar(self):
        lista = self.figuras.mostrar()
        if lista:
            messagebox.showinfo("Lista de Figuras", lista)
        else:
            messagebox.showinfo("Lista de Figuras", "No hay figuras registradas.")

    def run(self):
        self.root.mainloop()
        
if __name__ == "__main__":
    app = Principal()
    app.run()
