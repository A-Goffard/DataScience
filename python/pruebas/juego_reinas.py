import tkinter as tk
from tkinter import messagebox

class JuegoReinas:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de las 8 Reinas")
        self.vidas = 3
        self.reinas = 0
        self.n = 8
        self.tablero_estado = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.crear_tablero()
        self.vidas_label = tk.Label(self.root, text=f"Vidas: {self.vidas}")
        self.vidas_label.pack()

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
                if self.reinas == 8:
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
        self.vidas = 3
        self.reinas = 0
        self.vidas_label.config(text=f"Vidas: {self.vidas}")
        self.tablero_estado = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.tablero.destroy()
        self.crear_tablero()

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoReinas(root)
    root.mainloop()