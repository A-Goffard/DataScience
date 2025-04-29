import tkinter as tk
from tkinter import simpledialog, messagebox
from figuras import Figuras
from figura import Figura

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("🎨 Tablero de Figuras 🎨")
        self.root.geometry("400x500")
        self.root.config(bg="#B3E5FC")  # Fondo azul pastel

        self.figuras = Figuras()

        # Frame de botones
        self.frame_botones = tk.Frame(root, bg="#B3E5FC")
        self.frame_botones.pack(fill="both", expand=True, padx=20, pady=20)

        # Título
        titulo = tk.Label(self.frame_botones, text="¡Crea tus Figuras!", font=("Comic Sans MS", 20, "bold"), bg="#B3E5FC", fg="#4B0082")
        titulo.pack(pady=10)

        # Estilo botones
        estilo_boton = {"font": ("Comic Sans MS", 14), "bg": "#FFEB3B", "fg": "black", "width": 25, "height": 2}

        tk.Button(self.frame_botones, text="➕ Añadir Figura", command=self.anadir_figura, **estilo_boton).pack(pady=5)
        tk.Button(self.frame_botones, text="🗑️ Eliminar Figura", command=self.eliminar_figura, **estilo_boton).pack(pady=5)
        tk.Button(self.frame_botones, text="🔍 Buscar Figura (por ID)", command=self.buscar_figura, **estilo_boton).pack(pady=5)
        tk.Button(self.frame_botones, text="✅ Verificar si Existe", command=self.verificar_figura, **estilo_boton).pack(pady=5)
        tk.Button(self.frame_botones, text="📜 Mostrar Figuras", command=self.mostrar_figuras, **estilo_boton).pack(pady=5)

        # Pie de página
        pie = tk.Label(self.frame_botones, text="¡Diviértete creando!", font=("Comic Sans MS", 12, "italic"), bg="#B3E5FC", fg="#006400")
        pie.pack(side="bottom", pady=10)

    # -------------------------------------------------------
    def anadir_figura(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("➕ Nueva Figura")
        ventana.geometry("350x400")
        ventana.config(bg="#E1F5FE")

        tk.Label(ventana, text="ID:", font=("Comic Sans MS", 14), bg="#E1F5FE").pack(pady=5)
        id_entry = tk.Entry(ventana, font=("Comic Sans MS", 14))
        id_entry.pack(pady=5)

        tk.Label(ventana, text="Nombre:", font=("Comic Sans MS", 14), bg="#E1F5FE").pack(pady=5)
        nombre_entry = tk.Entry(ventana, font=("Comic Sans MS", 14))
        nombre_entry.pack(pady=5)

        tk.Label(ventana, text="Lados:", font=("Comic Sans MS", 14), bg="#E1F5FE").pack(pady=5)
        lados_spinbox = tk.Spinbox(ventana, values=(3, 4), font=("Comic Sans MS", 14))  # Solo triángulo o cuadrado
        lados_spinbox.pack(pady=5)

        tk.Label(ventana, text="Color:", font=("Comic Sans MS", 14), bg="#E1F5FE").pack(pady=5)
        color_options = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
        color_var = tk.StringVar(ventana)
        color_var.set(color_options[0])
        color_menu = tk.OptionMenu(ventana, color_var, *color_options)
        color_menu.config(font=("Comic Sans MS", 12))
        color_menu.pack(pady=5)

        def guardar():
            id = id_entry.get()
            nombre = nombre_entry.get()
            lados = int(lados_spinbox.get())
            color = color_var.get()

            if id and nombre and lados in (3, 4) and color:
                figura = Figura(id, nombre, lados, color)
                self.figuras.anadirFigura(figura)
                messagebox.showinfo("¡Perfecto!", f"Figura '{nombre}' añadida exitosamente.")
                ventana.destroy()
            else:
                messagebox.showwarning("Error", "Sólo se permiten figuras de 3 o 4 lados.")

        tk.Button(ventana, text="Guardar Figura", font=("Comic Sans MS", 14, "bold"),
                  bg="#FFCA28", command=guardar).pack(pady=20)

    # -------------------------------------------------------
    def eliminar_figura(self):
        id = simpledialog.askstring("Eliminar Figura", "¿Cuál es el ID de la figura a eliminar?")
        for figura in self.figuras.lista_figuras:
            if figura.get_id() == id:
                self.figuras.eliminarFigura(figura)
                messagebox.showinfo("Hecho", f"Figura '{figura.get_nombre()}' eliminada.")
                return
        messagebox.showerror("Error", "¡No encontré esa figura!")

    def buscar_figura(self):
        id = simpledialog.askstring("Buscar Figura", "Introduce el ID a buscar:")
        for index, figura in enumerate(self.figuras.lista_figuras):
            if figura.get_id() == id:
                messagebox.showinfo("¡Encontrado!", f"Figura '{figura.get_nombre()}' está en la posición {index}.")
                return
        messagebox.showerror("No encontrado", "Figura no encontrada.")

    def verificar_figura(self):
        id = simpledialog.askstring("Verificar Figura", "Introduce el ID a verificar:")
        for figura in self.figuras.lista_figuras:
            if figura.get_id() == id:
                messagebox.showinfo("Existe", f"✅ Sí, la figura '{figura.get_nombre()}' existe.")
                return
        messagebox.showwarning("No existe", "🚫 No existe una figura con ese ID.")

    def mostrar_figuras(self):
        if not self.figuras.lista_figuras:
            messagebox.showinfo("Lista Vacía", "Todavía no hay figuras.")
            return

        info = ""
        for figura in self.figuras.lista_figuras:
            info += f"🎨 ID: {figura.get_id()}, Nombre: {figura.get_nombre()}, Lados: {figura.get_lados()}, Color: {figura.get_color()}\n\n"
        messagebox.showinfo("Tus Figuras", info)

# -------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
