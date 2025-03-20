from random import randint

def obtener_precio_base(tipo):
    precios_base = {
        "Económico": 150,
        "Business": 250,
        "VIP": 500
    }
    return precios_base[tipo]

def obtener_descuento(edad):
    if edad >= 65:
        return 0.2
    else:
        return 0

def calcular_precio_total(precio_base, descuento, plus_opcion):
    return precio_base - precio_base * descuento + plus_opcion

def datos_cliente():
    print("Escribe tu nombre:")
    nombre = input()
    print("Hola, " + nombre)
    print("¿Qué edad tienes?")
    edad = int(input())
    return nombre, edad

def selecionar_opcion_caso(nombre, edad):
    print("¿Que queres hacer?")
    print("1. Generar el sorteo de un viaje.")
    print("2. Comprar un viaje.")
    print("3. Salir.")
    eleccion = input("Introduce el número de la opción deseada: ")
    if eleccion == "1":
        sorteo()
    elif eleccion == "2":
        comprar(nombre, edad)
    else:
        print("¡Hasta luego!")
    return eleccion

def sorteo():
    lista_nombres = ["Sonia", "Ignacio", "Alain", "Ysaias", "Nico", "Iñigo", "Angelina", "Ander", "Ángel", "Javier", "Luis Miguel", "Alex", "Ainara", "Aintzane"]

    lista_boletos = []
    diccionario_sorteo = {}
    contador = 0
    
    while contador < 14:
        numero_random = randint(1, 14)
        if numero_random in lista_boletos:
            pass
        else:
            lista_boletos.append(numero_random)
            diccionario_sorteo[lista_nombres[contador]] = numero_random
            contador += 1
        
    numero_ganador = randint(1, 14)
    ganador = [nombre for nombre, numero in diccionario_sorteo.items() if numero == numero_ganador]
    
    if ganador:
        print(f"El ganador del viaje es: {ganador[0]} con el número {numero_ganador}")
    else:
        print("No se ha encontrado un ganador.")
    
def seleccionar_tipo_viaje():
    print("¿En qué modalidad te gustaría contratar el viaje?")
    print("1. Económico. Viaje estandar.")
    print("2. Business. Viaje con desayuno y periódico y asientos confort.")
    print("3. VIP. Viaje con desayuno, periódico, manta, almohada, conexión wifi, intimidad y asientos amplios.")
    opcion = input("Introduce el número de la opción deseada: ")
    tipos = {"1": "Económico", "2": "Business", "3": "VIP"}
    return tipos[opcion]

def seleccionar_plus_opcion(tipo):
    tipos = ["Económico", "Business", "VIP"]
    plus_opciones = [("desayuno y periódico", 50), ("manta y almohada", 60), ("conexión wifi", 0)]
    index = tipos.index(tipo)
    if tipo != "VIP":
        print("¿Quieres el plus de " + plus_opciones[index][0] + "? El coste del plus es de " + str(plus_opciones[index][1]) + "€.")
        if input("si/no: ") == "si":
            return plus_opciones[index][1]
        else:
            return 
    else:
        return 0
    
def print_seleccion_viaje(nombre, tipo_viaje, plus_opcion, precio_total):
    print("")
    print("")
    print("-------------------")
    print(nombre)
    print("Has seleccionado el viaje de tipo: ", str(tipo_viaje))
    print("Plus: ", plus_opcion if plus_opcion > 0 else "ninguno")
    print("Precio total: ", str(int(precio_total)), "€.")
    print("-------------------")
    print("")
    print("")
    
def confirmar_reserva():
    print("¿Está todo correcto?")
    if input("si/no: ") == "si":
        print("La reserva se ha realizado correctamente")
    else:
        print("Tal vez quieras probar otra vez")
    
def comprar(nombre, edad):
    tipo_viaje = seleccionar_tipo_viaje()
    precio_base = obtener_precio_base(tipo_viaje)
    descuento = obtener_descuento(edad)
    plus_opcion = seleccionar_plus_opcion(tipo_viaje)
    precio_total = calcular_precio_total(precio_base, descuento, plus_opcion)
    print_seleccion_viaje(nombre, tipo_viaje, plus_opcion, precio_total)
    confirmar_reserva()

def main():
    nombre, edad = datos_cliente()
    selecionar_opcion_caso(nombre, edad)

if __name__ == "__main__": 
    main()