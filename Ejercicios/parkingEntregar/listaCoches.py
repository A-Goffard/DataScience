from coche import Coche
import datetime

class ListaCoches:
    max_normal = 200
    max_disc = 20
    max_electricos = 40

    def __init__(self):
        self.lista_coches = {}
        self.cantidad_ocupados_n = self.contar_coches("N")
        self.cantidad_ocupados_d = self.contar_coches("D")
        self.cantidad_ocupados_e = self.contar_coches("E")

    def anadir_coche(self, coche, hora_entrada):
        self.lista_coches[coche.matricula] = {"coche": coche, "hora_entrada": int(hora_entrada)}
        print(f"Coche añadido: {coche.matricula} con Matrícula {coche.matricula}")

    def existe_coche(self, matricula):
        return matricula in self.lista_coches

    def buscar_coche(self, matricula):
        return self.lista_coches.get(matricula, {}).get("coche")

    def obtener_hora_entrada(self, matricula):
        return self.lista_coches.get(matricula, {}).get("hora_entrada")

    def eliminar_coche(self, matricula):
        if matricula in self.lista_coches:
            del self.lista_coches[matricula]
            print(f"Coche con matrícula {matricula} eliminado.")
        else:
            print(f"No se encontró el coche con matrícula {matricula}.")

    def mostrar_coches(self):
        if not self.lista_coches:
            print("No hay coches en la lista.")
        else:
            print("1) Ver todos los coches")
            print("2) Ver los coches en plazas normales")
            print("3) Ver los coches en plazas para discapacitados")
            print("4) Ver los coches en plazas para eléctricos ")
            opcion = input("Selecciona una opción: ")
            if opcion == "1":
                for matricula, datos in self.lista_coches.items():
                    coche = datos["coche"]
                    hora_entrada = datos["hora_entrada"]
                    print(f"Coche: {coche.marca} {coche.color} con matricula: {coche.matricula}, Hora de entrada: {hora_entrada}")
            elif opcion == "2":
                for matricula, datos in self.lista_coches.items():
                    coche = datos["coche"]
                    hora_entrada = datos["hora_entrada"]
                    if coche.tipo == "N":
                        print(f"Coche: {coche.marca} {coche.color} con matricula: {coche.matricula}, Hora de entrada: {hora_entrada}")
            elif opcion == "3":
                for matricula, datos in self.lista_coches.items():
                    coche = datos["coche"]
                    hora_entrada = datos["hora_entrada"]
                    if coche.tipo == "D":
                        print(f"Coche: {coche.marca} {coche.color} con matricula: {coche.matricula}, Hora de entrada: {hora_entrada}")
            elif opcion == "4":
                for matricula, datos in self.lista_coches.items():
                    coche = datos["coche"]
                    hora_entrada = datos["hora_entrada"]
                    if coche.tipo == "E":
                        print(f"Coche: {coche.marca} {coche.color} con matricula: {coche.matricula}, Hora de entrada: {hora_entrada}")
            else:
                print("opcion no válida")

    def contar_coches(self, tipo):
        contador = 0
        for matricula, datos in self.lista_coches.items():
            coche = datos["coche"]
            if coche.tipo == tipo:
                contador += 1
        return contador