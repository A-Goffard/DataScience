from tkinter import *
from tkinter import messagebox
from figuras import Figuras
from figura import Figura

class MenuGrafico:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Figuras")
        self.ventana.geometry("500x500")

        self.figuras = Figuras()

        # Etiquetas y campos de entrada
        Label(ventana, text="ID:").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.id_entry = Entry(ventana)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(ventana, text="Nombre:").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.nombre_entry = Entry(ventana)
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(ventana, text="Lados:").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.lados_entry = Entry(ventana)
        self.lados_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(ventana, text="Color:").grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.color_entry = Entry(ventana)
        self.color_entry.grid(row=3, column=1, padx=10, pady=5)

        # Botones
        Button(ventana, text="Agregar Figura", command=self.agregar, bg="lightgreen").grid(row=4, column=0, padx=10, pady=10)
        Button(ventana, text="Eliminar Figura", command=self.eliminar, bg="lightcoral").grid(row=4, column=1, padx=10, pady=10)
        Button(ventana, text="Buscar Figura", command=self.buscar, bg="lightblue").grid(row=5, column=0, padx=10, pady=10)
        Button(ventana, text="Mostrar Figuras", command=self.mostrar, bg="lightyellow").grid(row=5, column=1, padx=10, pady=10)

    def agregar(self):
        """
        Agrega una figura a la lista.
        """
        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        lados = self.lados_entry.get()
        color = self.color_entry.get()

        if id and nombre and lados and color:
            # Validar que el campo 'lados' sea un número entero
            if lados.isdigit():
                lados = int(lados)
                figura = Figura(id, nombre, lados, color)
                self.figuras.agregar(figura)
                print(f"Figura con ID {id} agregada correctamente.")
            else:
                print("Error: El campo 'Lados' debe ser un número entero.")
        else:
            print("Error: Todos los campos son obligatorios.")

    def eliminar(self):
        """
        Elimina una figura de la lista por su ID con confirmación.
        """
        id = self.id_entry.get()
        if id:
            if self.figuras.existe(id):
                # Mostrar cuadro de confirmación
                respuesta = messagebox.askyesno("Confirmar eliminación", f"¿Está seguro de que desea eliminar la figura con ID {id}?")
                if respuesta:  # Si el usuario confirma
                    self.figuras.eliminar(id)
                    print(f"Figura con ID {id} eliminada correctamente.")
                else:
                    print("Eliminación cancelada por el usuario.")
            else:
                print(f"Error: No se encontró una figura con ID {id}.")
        else:
            print("Error: Debe ingresar un ID para eliminar.")

    def buscar(self):
        """
        Busca una figura por su ID y muestra sus detalles.
        """
        id = self.id_entry.get()
        if id:
            figura = self.figuras.buscar(id)
            if figura:
                print(f"Figura encontrada: ID: {figura.id}, Nombre: {figura.nombre}, Lados: {figura.lados}, Color: {figura.color}")
            else:
                print(f"Error: No se encontró una figura con ID {id}.")
        else:
            print("Error: Debe ingresar un ID para buscar.")

    def mostrar(self):
        """
        Muestra todas las figuras en la lista.
        """
        figuras = self.figuras.mostrar()
        if not figuras:
            print("No hay figuras registradas.")
        else:
            print("Lista de Figuras:")
            for figura in figuras:
                print(f"ID: {figura.id}, Nombre: {figura.nombre}, Lados: {figura.lados}, Color: {figura.color}")

if __name__ == "__main__":
    ventana = Tk()
    app = MenuGrafico(ventana)
    ventana.mainloop()