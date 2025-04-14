from coches import Coche
from listaCoches import ListaCoches

def mostrar_menu():
    print("\n--- Gestión de Parking ---")
    print("1. Añadir coche")
    print("2. Eliminar coche")
    print("3. Listar coches")
    print("4. Salir")
    print("--------------------------")

def main():
    lista_coches = ListaCoches()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            matricula = input("Introduzca la matrícula: ")
            marca = input("Introduzca la marca: ")
            modelo = input("Introduzca el modelo: ")
            color = input("Introduzca el color: ")
            tamanio = input("Introduzca el tamaño: ")
            coche = Coche(matricula, marca, modelo, color, tamanio)
            lista_coches.anadir_coche(coche)
        elif opcion == "2":
            matricula = input("Introduzca la matrícula del coche a eliminar: ")
            lista_coches.eliminar_coche(matricula)
        elif opcion == "3":
            print("\n--- Lista de Coches ---")
            lista_coches.mostrar_coches()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
