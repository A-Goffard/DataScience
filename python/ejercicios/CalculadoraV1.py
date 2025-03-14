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
num1 = int(round(num1))
print("Introduce el segundo número")
num2 = input()
num2 = int(round(num2))

if operacion == "1":
    operacion = "suma"
    resultado = num1 + num2
    print("Genial " + nombre + ", el resultado de la " + operacion + " es: " + str(resultado))

if operacion == "2":
    operacion = "resta"
    resultado = num1 - num2
    print("Genial " + nombre + ", el resultado de la " + operacion + " es: " + str(resultado))

if operacion == "3":
    operacion = "multiplicación" 
    resultado = num1 * num2 
    print("Genial " + nombre + ", el resultado de la " + operacion + " es: " + str(resultado))

if operacion == "4":
    operacion = "división"
    resultado = int(round(num1 / num2))
    print("Genial " + nombre + ", el resultado de la " + operacion + " es: " + str(resultado))
