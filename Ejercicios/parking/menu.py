from coche import Coche
from listaCoches import ListaCoches
from gestionCobros import GestionCobros

class Menu:
    def __init__(self):
        self.parking = ListaCoches(max_normal=10, max_disc=5, max_electricos=3)
        self.GestionCobros = GestionCobros()

    
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
                self.llamar_grua()
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
        hora_entrada = input("Inserta la hora de entrada: ")
        nuevo_coche = Coche(matricula, marca, color, tipo)
        self.parking.anadir_coche(nuevo_coche, hora_entrada)
        self.GestionCobros.crearCobro(matricula)
        print(f"Coche con matrícula {matricula} añadido correctamente al parking")
            
    def buscar_coche(self):
        matricula = input("Matrícula del coche a buscar: ")
        coche = self.parking.buscar_coche(matricula)
        if coche:
            print(f"Coche encontrado: matricula: {coche.matricula}, Marca: {coche.marca}, Color: {coche.color}, Tipo: {coche.tipo}")
            return coche
        else:
            print("Coche no encontrado.")

    def eliminar_coche(self):
        matricula = input("Matrícula del coche a eliminar: ")
        if matricula in self.GestionCobros.lista_cobros:
            hora_entrada = self.obtener_hora_entrada(matricula) 
            if hora_entrada is not None:
                hora_salida = input("Inserta la hora de salida: ")
                resultado_cobro = self.GestionCobros.calcularPrecio(hora_entrada, hora_salida)
                if resultado_cobro > 0:
                    self.parking.eliminar_coche(matricula)
                    self.GestionCobros.lista_cobros.remove(matricula)
                    print(f"Coche con matrícula {matricula} eliminado tras realizar el cobro de {resultado_cobro}.")
                else:
                    print("No se pudo realizar el cobro. El coche no será eliminado.")
            else:
                print("No se encontró la hora de entrada del coche.")
        else:
            print("Coche no encontrado.")
        
    def llamar_grua(self):
        matricula = input("Matrícula del coche que se ha de llevar la grua: ")
        self.parking.eliminar_coche(matricula)
        
    def obtener_hora_entrada(self, matricula):
        for registro in self.parking.lista_coches:
            if registro["coche"].matricula == matricula:
                return registro["hora_entrada"] 
        return None
    
if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()