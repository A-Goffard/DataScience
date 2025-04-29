import tkinter as tk
from tkinter import messagebox
from figura import Figura
from figuras import Listafiguras

# Lista para almacenar las figuras
ListaFiguras = []

# Variable para rastrear el índice seleccionado previamente
indice_seleccionado = None

def actualizar_lista():
    """Actualiza el Listbox con las figuras."""
    listbox_figuras.delete(0, tk.END)  # Limpia la lista
    for figura in ListaFiguras:
        listbox_figuras.insert(tk.END, f"ID: {figura.id}, Nombre: {figura.nombre}, Lados: {figura.lados}, Color: {figura.color}")

def añadir_figura():
    id = entry_id.get()
    nombre = entry_nombre.get()
    lados = entry_lados.get()
    color = entry_color.get()
    if id and nombre and lados and color:
        figura = Figura(id, nombre, lados, color)
        ListaFiguras.append(figura)
        messagebox.showinfo("Éxito", "Figura añadida correctamente.")
        entry_id.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_lados.delete(0, tk.END)
        entry_color.delete(0, tk.END)
        actualizar_lista()  # Actualiza la lista de coches
    else:
        messagebox.showwarning("Error", "Por favor, completa todos los campos.")

def eliminar_figura():
    id = entry_id.get()
    for figura in ListaFiguras:
        if figura.id == id:
            ListaFiguras.remove(figura)
            messagebox.showinfo("Éxito", "Figura eliminada correctamente.")
            entry_id.delete(0, tk.END)
            actualizar_lista()  # Actualiza la lista de figuras
            return
    messagebox.showwarning("Error", "Figura no encontrada.")

def buscar_figura():
    id = entry_id.get()
    for figura in ListaFiguras:
        if figura.id == id:
            messagebox.showinfo("Figura encontrada", f"ID: {figura.id}, Nombre: {figura.nombre}, Lados: {figura.lados}, Color: {figura.color}")
            return
    messagebox.showwarning("Error", "Figura no encontrada.")

def listar_figuras():
    if not ListaFiguras:
        messagebox.showinfo("Lista de figuras", "No hay figuras.")
    else:
        lista = "\n".join([f"ID: {figura.id}, Nombre: {figura.nombre}, Lados: {figura.lados}, Color: {figura.color}" for figura in ListaFiguras])
        messagebox.showinfo("Lista de figuras", lista)

def seleccionar_figura(event):
    """Actualiza los campos de entrada con los datos de la figura seleccionada o deselecciona."""
    global indice_seleccionado
    seleccion = listbox_figuras.curselection()  # Obtiene el índice de la selección

    if seleccion:
        indice = seleccion[0]
        if indice_seleccionado == indice:  # Si se selecciona el mismo índice, deseleccionar
            listbox_figuras.selection_clear(0, tk.END)  # Deselecciona todos los elementos
            indice_seleccionado = None  # Reinicia el índice seleccionado
            # Limpia los campos de entrada
            entry_id.delete(0, tk.END)
            entry_nombre.delete(0, tk.END)
            entry_lados.delete(0, tk.END)
            entry_color.delete(0, tk.END)
        else:
            indice_seleccionado = indice  # Actualiza el índice seleccionado
            figura = ListaFiguras[indice]  # Obtiene la figura correspondiente
            # Actualiza los campos de entrada
            entry_id.delete(0, tk.END)
            entry_id.insert(0, figura.id)
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, figura.nombre)
            entry_lados.delete(0, tk.END)
            entry_lados.insert(0, figura.lados)
            entry_color.delete(0, tk.END)
            entry_color.insert(0, figura.color)
    else:
        indice_seleccionado = None  # Reinicia el índice seleccionado si no hay selección

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Figuras")

# Crear los widgets
label_id = tk.Label(ventana, text="ID:")
label_id.grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(ventana)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=1, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=1, column=1, padx=10, pady=5)

label_lados = tk.Label(ventana, text="Lados:")
label_lados.grid(row=2, column=0, padx=10, pady=5)
entry_lados = tk.Entry(ventana)
entry_lados.grid(row=2, column=1, padx=10, pady=5)

label_color = tk.Label(ventana, text="Color:")
label_color.grid(row=3, column=0, padx=10, pady=5)
entry_color = tk.Entry(ventana)
entry_color.grid(row=3, column=1, padx=10, pady=5)

btn_añadir = tk.Button(ventana, text="Añadir Figura", command=añadir_figura)
btn_añadir.grid(row=4, column=0, padx=10, pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Figura", command=eliminar_figura)
btn_eliminar.grid(row=4, column=1, padx=10, pady=5)

btn_buscar = tk.Button(ventana, text="Buscar Figura", command=buscar_figura)
btn_buscar.grid(row=5, column=0, padx=10, pady=5)

btn_listar = tk.Button(ventana, text="Listar Figuras", command=listar_figuras)
btn_listar.grid(row=5, column=1, padx=10, pady=5)

# Listbox para mostrar los coches
label_lista = tk.Label(ventana, text="Lista de Figuras:")
label_lista.grid(row=6, column=0, columnspan=2, pady=5)

listbox_figuras = tk.Listbox(ventana, width=50, height=10)
listbox_figuras.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Vincular el evento de selección del Listbox
listbox_figuras.bind("<<ListboxSelect>>", seleccionar_figura)

# Iniciar el bucle principal de la ventana
ventana.mainloop()