print("¿Cómo te llamas?")
nombre = str(input())

print("¿Qué operación quieres hacer?")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
operacion = str(input("Introduce el número de la operación que quieres hacer: "))

print("Introduce el primer número")
num1 = input()
num1 = int(num1)
print("Introduce el segundo número")
num2 = input()
num2 = int(num2)
# print("Introduce el primer número")
# num1 = input()
# num1 = int(round(float(num1)))
# print("Introduce el segundo número")
# num2 = input()
# num2 = int(round(float(num2)))

# Funciones

def suma(num1, num2):
    return num1 + num2
def resta(num1, num2):
    return num1 - num2
def multiplicacion(num1, num2):
    return num1 * num2
def division(num1, num2): 
    if num2 == 0:
        num2 = float(input("Introduce un número distinto de 0, no se puede dividir por 0, es tu última oportunidad: ")) 
    return int(round(num1 / num2))

# Operaciones

if operacion == "1":
    operacion = "suma"
    resultado = int(suma(num1, num2))
    print("Genial " + nombre + ", el resultado de la " + operacion + " es: " + str(resultado))

elif operacion == "2":
    operacion = "resta"
    resultado = int(resta(num1, num2))
    print("Genial " + nombre + ", el resultado de la " + operacion + " es: " + str(resultado))

elif operacion == "3":
    operacion = "multiplicación" 
    resultado = int(multiplicacion(num1, num2))
    print("Genial " + nombre + ", el resultado de la " + operacion + " es: " + str(resultado))

elif operacion == "4":
    operacion = "división"
    resultado = int(division(num1, num2))
    print("Genial " + nombre + ", el resultado de la " + operacion + " es: " + str(resultado))

else:
    print("Operación no válida")
