print("Hola")
print("¿Qué viaje quieres realizar según tu confort?")
print("1. Económico")
print("2. Business")
print("3. VIP")
opcion = input("Introduce el número de la opción deseada: ")
if opcion == "1":
    tipo = "Económico"
    print("El precio común.")
    print("¿Eres mayor de 65?")
    if input("si/no: ") == "si":
        precio = int(150-(150*0.2))
    else:
        precio = int(150)
    print("¿Quieres el plus de desayuno y periódico?")
    if input("si/no: ") == "si":
        plus = "con plus"
        precio += int(50)
if opcion == "2":
    tipo = "Business"
    print("El precio incluye desayuno, periódico. Puesto más confort.")
    print("¿Eres mayor de 65?")
    if input("si/no: ") == "si":
        precio = int(250-(250*0.2))
    else:
        precio = int(250)
    print("¿Quieres el plus de manta y almohada?")
    if input("si/no: ") == "si":
        plus = "con plus"
        precio += int(60)
if opcion == "3":
    tipo = "VIP"
    print("El precio incluye desayuno, periódico, manta, almohada y conexión wifi. Asientos amplios.")
    print("¿Eres mayor de 65?")
    if input("si/no: ") == "si":
        plus = ""
        precio = int(500-(500*0.2))
    else:
        precio = int(500)
print("Has seleccionado ", str(tipo), plus, "-", str(precio), "€."," Confirmar pago!!" )
if input("si/no: ") == "si":
    print("Pago con tarjeta")
else:
    print("Operación no válida")

