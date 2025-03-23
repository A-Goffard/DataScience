# """
# 1)

# Enunciado:

# Suma de Números: Escribe un programa que calcule la suma de todos los
# números del 1 al 100 utilizando un bucle for o while.

# Algoritmo: 

# suma = 0
# fin = 100
# desde 1 hasta fin:ind
#     suma = suma+ind
# mostrar suma

# """
# # Código En Python

# suma = 0
# fin = 100
# for ind in range(1, fin+1):
#     suma = suma+ind
# print(suma)

# """
# 2)

# Enunciado:

# Números Pares e Impares: Crea un programa que imprima todos los números
# pares del 1 al 50 y luego todos los números impares del 51 al 100.

# Algoritmo: 
# num = 0
# lista[]
# mientras num <= 100
#     numMod = num % 2
#     if num <= 50 & numMod=0
#         print(num)
#     elif numMod!=0
#         print(num+1)

# mejor:
# for num (1,51):
#     si num % 2==0 entonces mostrar num
# for num (50,101):
#     si num % 2!=0 entonces mostrar num
# """
# # Código En Python
# for num in range(1,51):
#     if num % 2 == 0:
#         print(num)
# for num in range(51,101):
#     if num % 2 != 0:
#         print(num)

# """
# 3)

# Enunciado:

# Tabla de Multiplicar: Diseña un programa que solicite al usuario un número y
# muestre su tabla de multiplicar del 1 al 10.

# Algoritmo: 

# input(num)
# print(num*1)
# print(num*2)
# print(num*3)
# print(num*4)
# print(num*5)
# print(num*6)
# print(num*7)
# print(num*8)
# print(num*9)
# print(num*10)

# for rango del 1 al 10
#     imprimir el num*ind

# """
# # Código En Python

# num = int(input("Elige un número"))
# print(num*1)
# print(num*2)
# print(num*3)
# print(num*4)
# print(num*5)
# print(num*6)
# print(num*7)
# print(num*8)
# print(num*9)
# print(num*10)

# num = int(input("Elige un número para tener la tabla de multiplicar "))
# for ind in range (1,11):
#     print (num*ind)

# """
# 4)

# Enunciado:

# Factorial: Escribe una función que calcule el factorial de un número entero
# positivo dado.

# Algoritmo: 
# input= int(num)(+)
# for num > 0
#     resul = resul*num
#     num = num + 1
# print resul

# """
# # Código En Python

# num = int(input("Elige un número fara calcular el factor "))
# resul = 1
# for num in range(1, num+1):
#     resul = resul*num
#     num = num + 1
# print (resul)

# """
# 5)

# Enunciado:

# Contador de Vocales: Crea un programa que solicite al usuario una cadena de
# texto y cuente el número de vocales que contiene.

# Algoritmo: 

# input(palabra)
# for letra en palabra
#     if bocal
#         cont+1
#     esle
#         cont
# print(cont)

# """
# # Código En Python

# palabra = input("Escribe una palabra para ver cuántas vocales tiene: ")
# cont = 0

# for letra in palabra:
#     if letra in "aeiouAEIOU":
#         cont = cont+1
# print (cont)


# """
# 6)

# Enunciado:

# Triángulo de Asteriscos: Diseña un programa que imprima un triángulo de
# asteriscos como el siguiente:
# *
# **
# ***
# ****
# *****

# Algoritmo: 
# ind=0
# for ind in range (1,5)
#     print("*" * (ind+1))
#     ind+1
    

# """
# # Código En Python
# for ind in range(1,6):
#     print("*"*ind)
#     ind = ind + 1


# """
# 7)

# Enunciado:

# Cuadrado de Números: Escribe un programa que imprima un cuadrado de
# números del 1 al 5, como este:
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# Algoritmo: 

# for ind in range (1,5)
#     print(1 2 3 4 5)

# """
# # Código En Python
# for ind in range (1,6):
#     print("1 2 3 4 5")

# """
# 8)

# Enunciado:

# Números Primos: Crea un programa que imprima todos los números primos del
# 1 al 100.

# Algoritmo: 


# """
# # Código En Python


# """
# 9)

# Enunciado:

# Búsqueda en Matriz: Diseña un programa que busque un número específico en
# una matriz de números enteros.

# Algoritmo: 

# xxxxx

# """
# # Código En Python




# """
# 10)

# Enunciado:

# Suma de Diagonales: Escribe un programa que calcule la suma de las
# diagonales principal y secundaria de una matriz cuadrada.

# Algoritmo: 

# xxxxx

# """
# # Código En Python



# """
# 11)

# Enunciado:

# Calculadora Básica: Crea un programa que simule una calculadora básica,
# permitiendo al usuario realizar operaciones de suma, resta, multiplicación y
# división. Implementa cada operación como una función separada.

# Algoritmo: 

# input opcion
# input numero 1
# imput numero 2
# def suma
# def resta
# def multiplicacion
# def division
# def es_cero?


# """
# # Código En Python

# def sumar(num1, num2):
#     return int(num1 + num2)

# def restar(num1, num2):
#     return int(num1 - num2)

# def multiplicar(num1, num2):
#     return int(num1 * num2)

# def dividir(num1, num2):
#     if es_cero(num2):
#         num2 = pedir_numero()
#         if es_cero(num2):
#             return -1
#     else:
#         print("")
#     return int(num1 / num2)

# def es_cero(num):
#     return num == 0 # si es cero devuelve True, si es distinto, devuelve False
    
# def pedir_numero():
#     num = int(input("Inserta un número, por favor"))
#     return num

# def menu():
#     print("Opciones: ")
#     print("1) Sumar ")
#     print("2) Restar ")
#     print("3) Multiplicar ")
#     print("4) Dividir ")
#     print("0) Salir ")
#     opc = int(input())
#     return opc

# def operativa(num1, num2, opc):
#     if opc == 1:
#         resul = sumar(num1, num2)
#     elif opc == 2:
#         resul = restar(num1, num2)
#     elif opc == 3:
#         resul = multiplicar(num1, num2)
#     elif opc == 4:
#         resul = dividir(num1, num2)
#     else: #cero u otros
#         print("Agur!")
#         resul = -1
    
#     return int(resul) 

# def main():
#     opc = menu()   
#     num1 = pedir_numero()
#     num2 = pedir_numero()
#     resul = operativa(num1, num2, opc)
#     print("El resultado es: ", int(resul))
    
# if __name__ == "__main__":
#     main()

# """
# 12)

# Enunciado:

# Conversión de Temperatura: Escribe funciones que conviertan temperaturas
# de Celsius a Fahrenheit y viceversa.

# Algoritmo: 

# input temp
# input tipo
# def celsius_a_fahrenheit
# def fahrenheit_a_celsius

# """
# # Código En Python

# def celsius_a_fahrenheit(temp):
#     return (temp * 9/5) + 32

# def fahrenheit_a_celsius(temp):
#     return (temp - 32) * 5/9

# def pedir_temp():
#     temp = int(input("Introduce la temperatura "))
#     return temp

# def pedir_tipo():
#     tipo = input("¿Celsius (introcude: C) o Fahrenheit (introduce: F)? ")
#     if tipo != "C" and tipo != "F":
#         print("¡¿Tipo C o F?!")
#         tipo = input("¿C o F? Última oportunidad ")
#         return tipo
#     else:
#         return tipo

# def main():
#     temp = pedir_temp()
#     tipo = pedir_tipo()
#     if tipo == "C":
#         print(celsius_a_fahrenheit(temp))
#     elif tipo == "F":
#         print(fahrenheit_a_celsius(temp))
#     else:
#         print("Agur!")
        
        
# if __name__ == "__main__":
#     main()
    



# """
# 13)

# Enunciado:

# Palíndromo: Diseña una función que determine si una cadena de texto es un
# palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

# Algoritmo: 

# input(palabra)
# if palabra == palabra alreves
#     print("Es palíndromo")
# else
#     print("No es palíndromo")

# """
# # Código En Python

# def es_palindromo(palabra):
#     if palabra == palabra[::-1]:
#         print("Es palíndromo")
#     else:
#         print("No es palíndromo")

# palabra = input("Escribe una palabra para ver si es palíndromo: ")

# def main():
#     es_palindromo(palabra)  

# if __name__ == "__main__":
#     main()


"""
14)

Enunciado:

Ordenamiento de Burbuja: Implementa el algoritmo de ordenamiento de
burbuja para ordenar una lista de números enteros de forma ascendente.

Algoritmo: 

xxxxx

"""
# Código En Python




"""
15)

Enunciado:

Búsqueda Binaria: Escribe una función que realice una búsqueda binaria en
una lista ordenada de números enteros.

Algoritmo: 

xxxxx

"""
# Código En Python





"""
16)

Enunciado:

Detección de Anagramas: Crea una función que determine si dos cadenas de
texto son anagramas (contienen las mismas letras en diferente orden).

Algoritmo: 

input(palabra1)
input(palabra2)
if palabra1 contenido == palabra2 contenido
    print("Son anagramas")
else
    print("No son anagramas")

"""
# Código En Python

def son_anagramas(palabra1, palabra2):
    if len(palabra1) != len(palabra2):
        print("No son anagramas")
        return
    
    dicConteo1 = {}
    dicConteo2 = {}
    
    for letra in palabra1:
        if letra in dicConteo1:
            dicConteo1[letra] += 1
        else:
            dicConteo1[letra] = 1
    
    for letra in palabra2:
        if letra in dicConteo2:
            dicConteo2[letra] += 1
        else:
            dicConteo2[letra] = 1
    
    if dicConteo1 == dicConteo2:
        print("Son anagramas")
    else:
        print("No son anagramas")

def main():
    palabra1 = input("Escribe una palabra ")
    palabra2 = input("Escribe otra palabra ")
    son_anagramas(palabra1, palabra2)
    
if __name__ == "__main__":
    main()



"""
17)

Enunciado:

Sucesión de Fibonacci: Diseña una función que genere los primeros n números
de la sucesión de Fibonacci.

Algoritmo: 

xxxxx

"""
# Código En Python





"""
18)

Enunciado:

Validación de Email: Escribe una función que valide si una dirección de correo
electrónico tiene un formato válido.

Algoritmo: 

xxxxx

"""
# Código En Python



"""
19)

Enunciado:

Análisis de Texto: Crea un programa que analice un texto dado y cuente la
frecuencia de cada palabra.

Algoritmo: 

xxxxx

"""
# Código En Python


"""
20)

Enunciado:

Juego de Adivinanza: Diseña un juego en el que el ordenador elige un número
aleatorio y el usuario tiene que adivinarlo. Proporciona pistas como "más alto" o
"más bajo" según la suposición del usuario.

Algoritmo: 

xxxxx

"""
# Código En Python


