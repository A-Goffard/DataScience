"""
1)

Enunciado:

Suma de Números: Escribe un programa que calcule la suma de todos los
números del 1 al 100 utilizando un bucle for o while.

Algoritmo: 

suma = 0
fin = 100
desde 1 hasta fin:ind
    suma = suma+ind
mostrar suma

"""
# Código En Python

suma = 0
fin = 100
for ind in range(1, fin+1):
    suma = suma+ind
print(suma)

"""
2)

Enunciado:

Números Pares e Impares: Crea un programa que imprima todos los números
pares del 1 al 50 y luego todos los números impares del 51 al 100.

Algoritmo: 
num = 0
lista[]
mientras num <= 100
    numMod = num % 2
    if num <= 50 & numMod=0
        print(num)
    elif numMod!=0
        print(num+1)

mejor:
for num (1,51):
    si num % 2==0 entonces mostrar num
for num (50,101):
    si num % 2!=0 entonces mostrar num
"""
# Código En Python
for num in range(1,51):
    if num % 2 == 0:
        print(num)
for num in range(51,101):
    if num % 2 != 0:
        print(num)

"""
3)

Enunciado:

Tabla de Multiplicar: Diseña un programa que solicite al usuario un número y
muestre su tabla de multiplicar del 1 al 10.

Algoritmo: 

input(num)
print(num*1)
print(num*2)
print(num*3)
print(num*4)
print(num*5)
print(num*6)
print(num*7)
print(num*8)
print(num*9)
print(num*10)

for rango del 1 al 10
    imprimir el num*ind

"""
# Código En Python

num = int(input("Elige un número"))
print(num*1)
print(num*2)
print(num*3)
print(num*4)
print(num*5)
print(num*6)
print(num*7)
print(num*8)
print(num*9)
print(num*10)

num = int(input("Elige un número para tener la tabla de multiplicar "))
for ind in range (1,11):
    print (num*ind)

"""
4)

Enunciado:

Factorial: Escribe una función que calcule el factorial de un número entero
positivo dado.

Algoritmo: 
input= int(num)(+)
for num > 0
    resul = resul*num
    num = num + 1
print resul

"""
# Código En Python

num = int(input("Elige un número fara calcular el factor "))
resul = 1
for num in range(1, num+1):
    resul = resul*num
    num = num + 1
print (resul)

"""
5)

Enunciado:

Contador de Vocales: Crea un programa que solicite al usuario una cadena de
texto y cuente el número de vocales que contiene.

Algoritmo: 

input(palabra)
for letra en palabra
    if bocal
        cont+1
    esle
        cont
print(cont)

"""
# Código En Python

palabra = input("Escribe una palabra para ver cuántas vocales tiene: ")
cont = 0

for letra in palabra:
    if letra in "aeiouAEIOU":
        cont = cont+1
print (cont)


"""
6)

Enunciado:

Triángulo de Asteriscos: Diseña un programa que imprima un triángulo de
asteriscos como el siguiente:
*
**
***
****
*****

Algoritmo: 
ind=0
for ind in range (1,5)
    print("*" * (ind+1))
    ind+1
    

"""
# Código En Python
for ind in range(1,6):
    print("*"*ind)
    ind = ind + 1


"""
7)

Enunciado:

Cuadrado de Números: Escribe un programa que imprima un cuadrado de
números del 1 al 5, como este:
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

Algoritmo: 

for ind in range (1,5)
    print(1 2 3 4 5)

"""
# Código En Python
for ind in range (1,6):
    print("1 2 3 4 5")

"""
8)

Enunciado:

Números Primos: Crea un programa que imprima todos los números primos del
1 al 100.

Algoritmo: 


"""
# Código En Python


"""
9)

Enunciado:

Búsqueda en Matriz: Diseña un programa que busque un número específico en
una matriz de números enteros.

Algoritmo: 

xxxxx

"""
# Código En Python




"""
10)

Enunciado:

Suma de Diagonales: Escribe un programa que calcule la suma de las
diagonales principal y secundaria de una matriz cuadrada.

Algoritmo: 

xxxxx

"""
# Código En Python



"""
11)

Enunciado:

Calculadora Básica: Crea un programa que simule una calculadora básica,
permitiendo al usuario realizar operaciones de suma, resta, multiplicación y
división. Implementa cada operación como una función separada.

Algoritmo: 

xxxxx

"""
# Código En Python



"""
12)

Enunciado:

Conversión de Temperatura: Escribe funciones que conviertan temperaturas
de Celsius a Fahrenheit y viceversa.

Algoritmo: 

xxxxx

"""
# Código En Python



"""
13)

Enunciado:

Palíndromo: Diseña una función que determine si una cadena de texto es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

Algoritmo: 

xxxxx

"""
# Código En Python




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

xxxxx

"""
# Código En Python





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


