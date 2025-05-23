from frutas import Frutas
from fruta import Fruta


def menu():
    frutas = Frutas()

    while True:
        print("\n--- Menú Frutería ---")
        print("1. Agregar Fruta")
        print("2. Eliminar Fruta")
        print("3. Mostrar Frutas")
        print("4. Buscar Fruta")
        print("5. Salir")
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
            print("Ingrese los datos completos de la fruta a eliminar:")
            id = input("ID: ")
            nombre = input("Nombre: ")
            color = input("Color: ")
            sabor = input("Sabor: ")
            fruta_eliminar = Fruta(id, nombre, color, sabor)
            fruta_encontrada = frutas.buscar_fruta(fruta_eliminar)
            if fruta_encontrada:
                frutas.eliminar_fruta(fruta_eliminar)
                print("Fruta eliminada exitosamente.")
            else:
                print("No existe ninguna fruta con esos datos.")

        elif opcion == "3":
            print("\nLista de Frutas:")
            for fruta in frutas.mostrar_frutas():
                # Muestra los atributos usando getters si existen
                if hasattr(fruta, "get_id"):
                    print(f"ID: {fruta.get_id()}, Nombre: {fruta.get_nombre()}, Color: {fruta.get_color()}, Sabor: {fruta.get_sabor()}")
                else:
                    print(fruta)

        elif opcion == "4":
            print("Ingrese los datos completos de la fruta a buscar:")
            id = input("ID: ")
            nombre = input("Nombre: ")
            color = input("Color: ")
            sabor = input("Sabor: ")
            fruta = Fruta(id, nombre, color, sabor)
            resultado = frutas.buscar_fruta(fruta)
            if resultado:
                print("Fruta encontrada:")
                if hasattr(resultado, "get_id"):
                    print(f"ID: {resultado.get_id()}, Nombre: {resultado.get_nombre()}, Color: {resultado.get_color()}, Sabor: {resultado.get_sabor()}")
                else:
                    print(resultado)
            else:
                print("No se encontró ninguna fruta con esos datos.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
