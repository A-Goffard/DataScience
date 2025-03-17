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

def seleccionar_tipo_viaje():
    print("¿En qué modalidad te gustaría contratar el viaje?")
    print("1. Económico. Viaje estandar.")
    print("2. Business. Viaje con desayuno y periódico y asientos confort.")
    print("3. VIP. Viaje con desayuno, periódico, manta, almohada, conexión wifi, intimidad y asientos amplios.")
    opcion = input("Introduce el número de la opción deseada: ")
    tipos = {"1": "Económico", "2": "Business", "3": "VIP"}
    return tipos[opcion]

def seleccionar_plus_opcion(tipo):
    plus_opciones = {
        "Económico": ("desayuno y periódico", 50),
        "Business": ("manta y almohada", 60),
        "VIP": ("conexión wifi", 0)
    }
    print("¿Quieres el plus de " + plus_opciones[tipo][0] + "? El coste del plus es de " + str(plus_opciones[tipo][1]) + "€.")
    if input("si/no: ") == "si":
        return plus_opciones[tipo][1]
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