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

    def __init__(self):
        self.lista_coches = {}

    def anadir_coche(self, coche, hora_entrada):
        if self.existe_coche(coche.matricula):
            print(f"No se puede añadir el coche porque la matrícula {coche.matricula} ya está en la lista")
        else:
            self.lista_coches[coche] = datetime.datetime.now()
            print(f"Coche añadido: {coche.marca} con Matrícula {coche.matricula}")

    def existe_coche(self, matricula):
        for coche in self.lista_coches:
            if coche.matricula == matricula:
                return True
        return False

    def buscar_coche(self, matricula):
        for coche in self.lista_coches:
            if coche.matricula == matricula:
                return coche
        return None

    def eliminar_coche(self, matricula):
        if self.existe_coche(matricula):
            self.lista_coches.pop(self.buscar_coche(matricula))
            return True
        return False

    def mostrar_coches(self):
        if not self.lista_coches:
            print("No hay coches en la lista.")
        else:
            print("1) Ver todos los coches")
            print("2) Ver los coches en plazas normales")
            print("3) Ver los coches en plazas para discapacitados")
            print("4) Ver los coches en plazas para eléctricos ")
            opcion=input("Selecciona una opción: ")
            if opcion=="1":
                for coche, fecha in self.lista_coches.items():
                    print(f"Coche: {coche.marca} {coche.color} con matricula: {coche.matricula}, Fecha y Hora de entrada: {fecha}")
            elif opcion=="2":
                for coche, fecha in self.lista_coches.items():
                    if coche.tipo=="N":
                        print(f"Coche: {coche.marca} {coche.color} con matricula: {coche.matricula}, Fecha y Hora de entrada: {fecha}")
            elif opcion=="3":
                for coche, fecha in self.lista_coches.items():
                    if coche.tipo=="D":
                        print(f"Coche: {coche.marca} {coche.color} con matricula: {coche.matricula}, Fecha y Hora de entrada: {fecha}")
            elif opcion=="4":
                for coche, fecha in self.lista_coches.items():
                    if coche.tipo=="E":
                        print(f"Coche: {coche.marca} {coche.color} con matricula: {coche.matricula}, Fecha y Hora de entrada: {fecha}")
            else:
                print("opcion no válida")

    def contar_coches(self,tipo):
        contador = 0
        for coche in self.lista_coches:
            if coche.tipo==tipo:
                contador += 1
        return contador