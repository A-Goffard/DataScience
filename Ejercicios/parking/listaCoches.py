from coche import Coche


class ListaCoches:
    """
    Clase que representa una lista de coches en un parking.
    """
    def __init__(self, max_normal, max_disc, max_electricos):
        self.lista_coches = []
        self.max_normal = max_normal
        self.max_disc = max_disc
        self.max_electricos = max_electricos
        self.cant_ocupados_n = 0
        self.cant_ocupados_d = 0
        self.cant_ocupados_e = 0

    def anadir_coche(self, coche, hora_entrada):
        """
        Añade un coche a la lista de coches del parking.
        """
        self.lista_coches.append({"coche": coche, "hora_entrada": hora_entrada})
        print("Coche añadido correctamente")

    def eliminar_coche(self, matricula):
        for registro in self.lista_coches:
            if registro["coche"].matricula == matricula:
                self.lista_coches.remove(registro)
                return True
        return False

    def buscar_coche(self, matricula):
        """
        Busca un coche en la lista de coches del parking por su matrícula.
        """
        for coche, hora_entrada in self.lista_coches:
            if coche.matricula == matricula:
                return coche
        print("No se encontró el coche en el parking.")
        return None

    def mostrar_todos(self):
        """
        Muestra todos los coches en la lista de coches del parking.
        """
        if not self.lista_coches:
            print("No hay coches en el parking.")
            return
        print("--- Todos los coches en el parking ---")
        for coche, hora_entrada in self.lista_coches:
            print(f"Matrícula: {coche.matricula}, Marca: {coche.marca}, Color: {coche.color}, Tipo: {coche.tipo}, Hora de entrada: {hora_entrada}")

    def mostrar_normal(self):
        """
        Muestra los coches normales en la lista de coches del parking.
        """
        if not self.lista_coches:
            print("No hay coches normales en el parking.")
            return
        print("--- Coches en plazas normales ---")
        for coche, hora_entrada in self.lista_coches:
            if coche.tipo == "normal":
                print(f"Matrícula: {coche.matricula}, Marca: {coche.marca}, Color: {coche.color}, Tipo: {coche.tipo}, Hora de entrada: {hora_entrada}")

    def mostrar_disc(self):
        """
        Muestra los coches para discapacitados en la lista de coches del parking.
        """
        if not self.lista_coches:
            print("No hay coches discapacitados en el parking.")
            return
        print("--- Coches en plazas para discapacitados ---")
        for coche, hora_entrada in self.lista_coches:
            if coche.tipo == "disc":
                print(f"Matrícula: {coche.matricula}, Marca: {coche.marca}, Color: {coche.color}, Tipo: {coche.tipo}, Hora de entrada: {hora_entrada}")

    def mostrar_elec(self):
        """
        Muestra los coches eléctricos en la lista de coches del parking.
        """
        if not self.lista_coches:
            print("No hay coches electricos en el parking.")
            return
        print("--- Coches en plazas eléctricas ---")
        for coche, hora_entrada in self.lista_coches:
            if coche.tipo == "electrico":
                print(f"Matrícula: {coche.matricula}, Marca: {coche.marca}, Color: {coche.color}, Tipo: {coche.tipo}, Hora de entrada: {hora_entrada}")
