# Juego de guerra en las cartas de la bajara Española

# 2 jugadores
# Crear la baraja
#   4 palos del 1 al 7, sota, caballo y rey

# Repartimos todas las cartas aleatoriamente entre los jugadores
# Los jugadores sacan las cartas al mismo tiempo en el orden que le han quedado
# La carta más alta gana y ese jugador se lleva las cartas y las pone al final de sus cartas
# El que se quede sin cartas pierde




# Crear lista de jugadores (N) ---> listaJugadores = [Jugador1, Jugador2]

# Cartas ---> 40 cartas = cantBaraja
# Crear lista de barajas ---> numeroCarta = ["1", "2", "3", "4", "5", "6" "7", "S", "C", "R"]
# Crar palos por separado?? ---> palos = ["Oros", "Copas", "Espadas", "Bastos"]

# Crear un diccionario por persona??

# Partida:

# Crear baraja: Diccionario ---> baraja: {1:Copas, 2:copas, .... R:bastos} random de 40 cartas
# Repartir cartas
#    cantPorJugador = 0
#    repartidas = 0
#    jugadores[N]
#    Mientras repartidas <= cantBaraja
#       Por cada jugador(hasta N): jugadorActual
#             jugadores[jugadorActual]=añadirCartaAlMonton
#       repartidas = repartidas + 1
#


# Disparar el evento de sacar carta al pulsar el space

#    Mostrar cartas:
#       Por cada jugador(hasta N): jugadorActual
#             jugadores[jugadorActual]=añadirCartaAlMonton

# Comparar las cartas posición [0] de cada jugador
# El jugador que tenga la carta más alta añade al diccionario al final las cartas de la jugada y el resto de jugadores se les quita del diccionario
#   append()
#   pop[0]()
# Comprobar en cada final de turno si hay un jugador con la lista/dic bacío, es eliminado
# Comprobar en cada ciclo los diccionarios/listas, si solo hay uno con valores, es el ganador

import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def sacar_carta(self):
        return self.cartas.pop(0) if self.cartas else None

    def tiene_cartas(self):
        return len(self.cartas) > 0

def crear_baraja():
    palos = ["Oros", "Copas", "Espadas", "Bastos"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "S", "C", "R"]
    baraja = [(numero, palo) for numero in numeros for palo in palos]
    random.shuffle(baraja)
    return baraja

def repartir_cartas(baraja, jugadores):
    while baraja:
        for jugador in jugadores:
            if baraja:
                jugador.agregar_carta(baraja.pop(0))

def jugar_turno(jugadores):
    cartas_jugadas = [(jugador, jugador.sacar_carta()) for jugador in jugadores if jugador.tiene_cartas()]
    cartas_jugadas.sort(key=lambda x: x[1][0], reverse=True)
    ganador = cartas_jugadas[0][0]
    for jugador, carta in cartas_jugadas:
        ganador.agregar_carta(carta)
    return ganador

def juego_guerra():
    jugadores = [Jugador("Jugador1"), Jugador("Jugador2")]
    baraja = crear_baraja()
    repartir_cartas(baraja, jugadores)

    while all(jugador.tiene_cartas() for jugador in jugadores):
        ganador = jugar_turno(jugadores)
        print(f"Ganador del turno: {ganador.nombre}")

    ganador_final = max(jugadores, key=lambda jugador: len(jugador.cartas))
    print(f"El ganador del juego es: {ganador_final.nombre}")

if __name__ == "__main__":
    juego_guerra()

