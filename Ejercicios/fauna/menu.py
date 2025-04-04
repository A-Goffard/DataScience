from Gato import Gato
from Perro import Perro
from lista_menu import ListaAnimales

class Fauna:
    def __init__(self):
        # Crear una instancia de ListaAnimales
        self.lista_animales = ListaAnimales()

    def menu(self):
        while True:
            print("\n---- Menú ----")
            print("1. Mostrar lista de animales")
            print("2. Agregar nuevo perro")
            print("3. Agregar nuevo gato")
            print("4. Salir")
            opcion = input("Inserta una opción: ")

            if opcion == "1":
                # Llamar al método mostrar_animales de ListaAnimales
                self.lista_animales.mostrar_animales()
            elif opcion == "2":
                # Agregar un nuevo perro
                nombre = input("Inserta el nombre del perro: ")
                edad = int(input("Inserta la edad del perro: "))
                nuevo_perro = Perro(nombre, edad)
                self.lista_animales.agregar_animal(nuevo_perro)
                print("Perro agregado correctamente.")
            elif opcion == "3":
                # Agregar un nuevo gato
                nombre = input("Inserta el nombre del gato: ")
                edad = int(input("Inserta la edad del gato: "))
                nuevo_gato = Gato(nombre, edad)
                self.lista_animales.agregar_animal(nuevo_gato)
                print("Gato agregado correctamente.")
            elif opcion == "4":
                # Salir del programa
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, elije una opción válida.")