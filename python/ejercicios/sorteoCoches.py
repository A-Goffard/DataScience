# Sorteo de 10 coches aleatoriamente
import random

coches = [
    "Toyota Corolla",
    "Honda Civic",
    "Ford Focus",
    "Chevrolet Malibu",
    "Nissan Sentra",
    "Volkswagen Jetta",
    "Hyundai Elantra",
    "Kia Optima",
    "Mazda 3",
    "Subaru Impreza"
]

print("El coche que has ganado es: ")
cocheR = random.randint(0, 9)
print(coches[cocheR])

