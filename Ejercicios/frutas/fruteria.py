from frutas import Frutas
from fruta import Fruta


def menu():
    frutas = Frutas()

    while True:
        print("\n--- Menú Frutería ---")
        print("1. Agregar Fruta")
        print("2. Eliminar Fruta")
        print("3. Mostrar Frutas")
        print("4. Buscar Fruta por nombre")
        print("5. Buscar Fruta por ID")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese ID de la fruta: ")
            nombre = input("Ingrese nombre de la fruta: ")
            color = input("Ingrese color de la fruta: ")
            sabor = input("Ingrese sabor de la fruta: ")
            nueva_fruta = Fruta(id, nombre, color, sabor)
            frutas.agregar_fruta(nueva_fruta)
            print("Fruta agregada exitosamente.")

        elif opcion == "2":
            id = input("Ingrese el ID de la fruta a eliminar: ")
            fruta_encontrada = None
            for fruta in frutas.mostrar_frutas():
                # Usa get_id() para comparar correctamente
                if hasattr(fruta, "get_id") and fruta.get_id() == id:
                    fruta_encontrada = fruta
                    break
            if fruta_encontrada:
                frutas.eliminar_fruta(id)
                print("Fruta eliminada exitosamente.")
            else:
                print("No existe ninguna fruta con ese ID.")

        elif opcion == "3":
            print("\nLista de Frutas:")
            for fruta in frutas.mostrar_frutas():
                # Muestra los atributos usando getters si existen
                if hasattr(fruta, "get_id"):
                    print(f"ID: {fruta.get_id()}, Nombre: {fruta.get_nombre()}, Color: {fruta.get_color()}, Sabor: {fruta.get_sabor()}")
                else:
                    print(fruta)

        elif opcion == "4":
            nombre = input("Ingrese el nombre de la fruta a buscar: ")
            resultado = frutas.buscar_frutas(nombre)
            if resultado:
                print("Frutas encontradas:")
                for fruta in resultado:
                    if hasattr(fruta, "get_id"):
                        print(f"ID: {fruta.get_id()}, Nombre: {fruta.get_nombre()}, Color: {fruta.get_color()}, Sabor: {fruta.get_sabor()}")
                    else:
                        print(fruta)
            else:
                print("No se encontraron frutas con ese nombre.")

        elif opcion == "5":
            id = input("Ingrese el ID de la fruta a buscar: ")
            resultado = frutas.buscar_fruta_por_id(id)
            if resultado:
                print("Fruta encontrada:")
                if hasattr(resultado, "get_id"):
                    print(f"ID: {resultado.get_id()}, Nombre: {resultado.get_nombre()}, Color: {resultado.get_color()}, Sabor: {resultado.get_sabor()}")
                else:
                    print(resultado)
            else:
                print("No se encontró ninguna fruta con ese ID.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
