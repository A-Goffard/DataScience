def obtener_precio_base(tipo):
    tipos = ["Económico", "Business", "VIP"]
    precios_base = [150, 250, 500]
    return precios_base[tipos.index(tipo)]

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

def seleccionar_tipo_viaje():
    print("¿En qué modalidad te gustaría contratar el viaje?")
    print("1. Económico. Viaje estandar.")
    print("2. Business. Viaje con desayuno y periódico y asientos confort.")
    print("3. VIP. Viaje con desayuno, periódico, manta, almohada, conexión wifi, intimidad y asientos amplios.")
    opcion = input("Introduce el número de la opción deseada: ")
    tipos = ["Económico", "Business", "VIP"]
    return tipos[int(opcion) - 1]

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
    
def confirmar_reserva():
    print("¿Está todo correcto?")
    if input("si/no: ") == "si":
        print("La reserva se ha realizado correctamente")
    else:
        print("Tal vez quieras probar otra vez")
    
def main():
    nombre, edad = datos_cliente()
    tipo_viaje = seleccionar_tipo_viaje()
    precio_base = obtener_precio_base(tipo_viaje)
    descuento = obtener_descuento(edad)
    plus_opcion = seleccionar_plus_opcion(tipo_viaje)
    precio_total = calcular_precio_total(precio_base, descuento, plus_opcion)
    
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

    confirmar_reserva()

if __name__ == "__main__": 
    main()