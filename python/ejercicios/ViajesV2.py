def precioBase(tipo):
    if tipo == "Económico":
        return 150
    elif tipo == "Business":
        return 250
    elif tipo == "VIP":
        return 500
    
def descuento(edad):
    if edad >= 65:
        return 0.2
    else:
        return 0
    
def plus(tipo, plus_option):
    if tipo == "Económico" and plus_option == "si":
        return 50
    elif tipo == "Business" and plus_option == "si":
        return 60
    elif tipo == "VIP":
        return 0
    
def precioTotal(precioBase, descuento, plus):
    return precioBase - precioBase * descuento + plus


# Intro

print("Escribe tu nombre:")
nombre = input()
print("Hola, " + nombre)
print("¿Qué edad tienes?")
edad = int(input())

print("¿En qué modalidad te gustaría contratar el viaje?")
print("1. Económico. Viaje estandar.")
print("2. Business. Viaje con desayuno y periódico y asientos confort.")
print("3. VIP. Viaje con desayuno, periódico, manta, almohada, conexión wifi, intimidad y asientos amplios.")

tipo = ""
plus_option = ""
precio = 0
opcion = input("Introduce el número de la opción deseada: ")


# Operaciones

if opcion == "1":
    tipo = "Económico"

    print("¿Quieres el plus de desayuno y periódico?")
    if input("si/no: ") == "si":
        plus_option = "si"
    else:
        plus_option = "no"
    precio = precioTotal(precioBase(tipo), descuento(edad), plus(tipo, plus_option))

elif opcion == "2":
    tipo = "Business"
    
    print("¿Quieres el plus de manta y almohada?")
    if input("si/no: ") == "si":
        plus_option = "si"
    else:
        plus_option = "no"
    precio = precioTotal(precioBase(tipo), descuento(edad), plus(tipo, plus_option))        
    
elif opcion == "3":
    tipo = "VIP"
    
    precio = precioTotal(precioBase(tipo), descuento(edad), plus(tipo, plus_option))

print("")
print("")
print("-------------------")
print("Has seleccionado el viaje de tipo: ", str(tipo))
print("Plus: ", plus_option)
print("Precio total: ", str(int(precio)), "€.")
print("-------------------")
print("")
print("")
print("¿Está todo correcto?")

if input("si/no: ") == "si":
    print("La reserva se ha realizado correctamente")
else:
    print("Tal vez quieras probar otra vez")