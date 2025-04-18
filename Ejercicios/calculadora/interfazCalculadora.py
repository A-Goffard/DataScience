import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from calculadora import Calculadora

class InterfazCalculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x400")
        self.root.configure(bg="#FFC0CB")  # Fondo rosa

        # Variables internas
        self.operacion = None
        self.primer_numero = None

        # Pantalla de la calculadora
        self.pantalla = ttk.Entry(root, font=("Arial", 24), justify="right", bootstyle="info", width=15)
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Botones de números
        botones_numeros = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
            ("0", 4, 1)
        ]
        for (texto, fila, columna) in botones_numeros:
            ttk.Button(root, text=texto, bootstyle="primary", command=lambda t=texto: self.agregar_numero(t)).grid(
                row=fila, column=columna, padx=5, pady=5, ipadx=10, ipady=10
            )

        # Botones de operaciones
        botones_operaciones = [
            ("+", 1, 3, self.sumar),
            ("-", 2, 3, self.restar),
            ("*", 3, 3, self.multiplicar),
            ("/", 4, 3, self.dividir),
            ("=", 4, 2, self.calcular),
            ("C", 4, 0, self.limpiar)
        ]
        for (texto, fila, columna, comando) in botones_operaciones:
            ttk.Button(root, text=texto, bootstyle="info", command=comando).grid(
                row=fila, column=columna, padx=5, pady=5, ipadx=10, ipady=10
            )

    def agregar_numero(self, numero):
        """Agrega un número a la pantalla."""
        self.pantalla.insert(END, numero)

    def limpiar(self):
        """Limpia la pantalla y reinicia las variables."""
        self.pantalla.delete(0, END)
        self.operacion = None
        self.primer_numero = None

    def obtener_numero(self):
        """Obtiene el número actual de la pantalla."""
        try:
            return float(self.pantalla.get())
        except ValueError:
            self.limpiar()
            return None

    def sumar(self):
        self.primer_numero = self.obtener_numero()
        self.operacion = Calculadora.sumar
        self.pantalla.delete(0, END)

    def restar(self):
        self.primer_numero = self.obtener_numero()
        self.operacion = Calculadora.restar
        self.pantalla.delete(0, END)

    def multiplicar(self):
        self.primer_numero = self.obtener_numero()
        self.operacion = Calculadora.multiplicar
        self.pantalla.delete(0, END)

    def dividir(self):
        self.primer_numero = self.obtener_numero()
        self.operacion = Calculadora.dividir
        self.pantalla.delete(0, END)

    def calcular(self):
        """Realiza el cálculo y muestra el resultado."""
        segundo_numero = self.obtener_numero()
        if self.primer_numero is not None and self.operacion is not None and segundo_numero is not None:
            try:
                resultado = self.operacion(self.primer_numero, segundo_numero)
                self.pantalla.delete(0, END)
                self.pantalla.insert(0, str(resultado))
            except ValueError as e:
                self.pantalla.delete(0, END)
                self.pantalla.insert(0, "Error")

if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")  # Usar ttkbootstrap con tema moderno
    app = InterfazCalculadora(root)
    root.mainloop()
