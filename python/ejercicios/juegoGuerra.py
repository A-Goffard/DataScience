# Juego de guerra en las cartas de la bajara Española

# 2 jugadores
# Crear la baraja
#   4 palos del 1 al 7, sota, caballo y rey

# Repartimos todas las cartas aleatoriamente entre los jugadores
# Los jugadores sacan las cartas al mismo tiempo en el orden que le han quedado
# La carta más alta gana y ese jugador se lleva las cartas y las pone al final de sus cartas
# El que se quede sin cartas pierde




# Crear lista de jugadores ---> Lista_jugadores = [Jugador1, Jugador2]

# Cartas ---> 40 cartas
# Crear lista de barajas ---> Lista_baraja = ["1", "2", "3", "4", "5", "6" "7", "S", "C", "R"]
# Crar palos por separado?? ---> Cuatro_palos = ["Oros", "Copas", "Espadas", "Bastos"]

# Crear un diccionario por persona??

# Partida:

# Disparar el evento de sacar carta al pulsar el space
# Comparar las cartas posición [0] de cada jugador
# El jugador que tenga la carta más alta añade al diccionario al final las cartas de la jugada y el resto de jugadores se les quita del diccionario
#   append()
#   pop[0]()
# Comprobar en cada final de turno si hay un jugador con la lista/dic bacío, es eliminado
# Comprobar en cada ciclo los diccionarios/listas, si solo hay uno con valores, es el ganador

