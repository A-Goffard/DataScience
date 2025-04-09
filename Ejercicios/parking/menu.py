from coche import Coche
from listaCoches import ListaCoches
from gestionCobros import GestionCobros

class Menu:
    def __init__(self):
        self.parking = ListaCoches()
    
    def mostrar_menu(self):
        while True:
            print("\n---- Menú ----")
            print("1. Agregar coche")
            print("2. Eliminar coche")
            print("3. Llamar grua")
            print("4. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.agregar_coche()
            elif opcion == "2":
                self.eliminar_coche()
            elif opcion == "3":
                self.coches.llamar_grua()
            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

    def agregar_coche(self):
        matricula = input("Matrícula del coche: ")
        marca = input("Marca del coche: ")
        color = input("Color del coche: ")
        tipo = input("Tipo de coche: ")
        nuevo_coche = Coche(matricula, marca, color, tipo)
        self.coches.anadir_coche(nuevo_coche)

    def buscar_coche(self):
        matricula = input("Matrícula del coche a buscar: ")
        coche = self.coches.buscar_coche(matricula)
        if coche:
            print(f"Coche encontrado: matricula: {coche.matricula}, Marca: {coche.marca}, Color: {coche.color}, Tipo: {coche.tipo}")
            return coche
        else:
            print("Coche no encontrado.")

    def eliminar_coche(self):
        matricula = input("Matrícula del coche a eliminar: ")
        self.coches.eliminar_coche(matricula)

    def llamar_grua(self):
        matricula = input("Matrícula del coche que se ha de llevar la grua: ")
        self.coches.eliminar_coche(matricula)

if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()