import tkinter as tk
from tkinter import messagebox, simpledialog

class JuegoReinas:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de las N Reinas")
        self.configurar_juego()
        self.tablero_estado = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.crear_tablero()
        self.vidas_label = tk.Label(self.root, text=f"Vidas: {self.vidas}")
        self.vidas_label.pack()
        self.solucion_btn = tk.Button(self.root, text="Mostrar Solución", command=self.mostrar_solucion)
        self.solucion_btn.pack()

    def configurar_juego(self):
        self.n = simpledialog.askinteger("Configuración", "Ingrese el tamaño del tablero (N, entre 2 y 30):", minvalue=2, maxvalue=30)
        self.m = simpledialog.askinteger("Configuración", "Ingrese el número de reinas (M, entre 1 y 30):", minvalue=1, maxvalue=30)
        if self.m > self.n:
            messagebox.showinfo("Advertencia", f"El número máximo de reinas para un tablero de {self.n}x{self.n} es {self.n}.")
            self.m = self.n
        self.vidas = 3
        self.reinas = 0

    def crear_tablero(self):
        self.tablero = tk.Frame(self.root)
        self.tablero.pack()
        for i in range(self.n):
            for j in range(self.n):
                celda = tk.Frame(self.tablero, width=50, height=50)
                celda.grid(row=i, column=j)
                celda.config(bg="#f0d9b5" if (i + j) % 2 == 0 else "#b58863")
                celda.bind("<Button-1>", lambda event, fila=i, col=j: self.manejar_click(event, fila, col))

    def manejar_click(self, event, fila, col):
        celda = event.widget
        if self.tablero_estado[fila][col] == 1:
            celda.config(bg="#f0d9b5" if (fila + col) % 2 == 0 else "#b58863")
            self.tablero_estado[fila][col] = 0
            self.reinas -= 1
        else:
            if self.es_seguro(fila, col):
                celda.config(bg="red")
                self.tablero_estado[fila][col] = 1
                self.reinas += 1
                if self.reinas == self.m:
                    self.mostrar_mensaje_ganador()
            else:
                celda.config(text="X", fg="red")
                self.root.after(1000, lambda: celda.config(text=""))
                self.vidas -= 1
                self.vidas_label.config(text=f"Vidas: {self.vidas}")
                if self.vidas == 0:
                    self.mostrar_mensaje_perdedor()

    def es_seguro(self, fila, col):
        for i in range(self.n):
            if self.tablero_estado[fila][i] == 1 or self.tablero_estado[i][col] == 1:
                return False

        for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
            if self.tablero_estado[i][j] == 1:
                return False

        for i, j in zip(range(fila, -1, -1), range(col, self.n)):
            if self.tablero_estado[i][j] == 1:
                return False

        for i, j in zip(range(fila, self.n), range(col, -1, -1)):
            if self.tablero_estado[i][j] == 1:
                return False

        for i, j in zip(range(fila, self.n), range(col, self.n)):
            if self.tablero_estado[i][j] == 1:
                return False

        return True

    def mostrar_mensaje_ganador(self):
        messagebox.showinfo("¡Ganaste!", "¡Ganaste! Puedes reiniciar el juego para jugar de nuevo.")
        self.reiniciar_juego()

    def mostrar_mensaje_perdedor(self):
        messagebox.showinfo("¡Perdiste!", "¡Perdiste! Puedes reiniciar el juego para intentarlo de nuevo.")
        self.reiniciar_juego()

    def reiniciar_juego(self):
        self.configurar_juego()
        self.vidas_label.config(text=f"Vidas: {self.vidas}")
        self.tablero_estado = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.tablero.destroy()
        self.crear_tablero()

    def mostrar_solucion(self):
        solucion = self.resolver_reinas()
        if solucion:
            for i in range(self.n):
                for j in range(self.n):
                    if solucion[i][j] == 1:
                        celda = self.tablero.grid_slaves(row=i, column=j)[0]
                        celda.config(bg="green")
        else:
            messagebox.showinfo("Sin solución", "No hay solución posible para este tablero.")

    def resolver_reinas(self):
        def es_valido(tablero, fila, col):
            for i in range(fila):
                if tablero[i][col] == 1:
                    return False
            for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
                if tablero[i][j] == 1:
                    return False
            for i, j in zip(range(fila, -1, -1), range(col, self.n)):
                if tablero[i][j] == 1:
                    return False
            return True

        def resolver(tablero, fila):
            if fila >= self.m:
                return True
            for col in range(self.n):
                if es_valido(tablero, fila, col):
                    tablero[fila][col] = 1
                    if resolver(tablero, fila + 1):
                        return True
                    tablero[fila][col] = 0
            return False

        tablero = [[0 for _ in range(self.n)] for _ in range(self.n)]
        if resolver(tablero, 0):
            return tablero
        return None

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoReinas(root)
    root.mainloop()