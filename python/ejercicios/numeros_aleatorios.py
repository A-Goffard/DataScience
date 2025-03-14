import random # Los numeros que pongas en el rango, no cogen nunca el ultimo numero

# print(random.randrange(1, 10))

x = random.randrange(1, 10)

if x > 5:
    print("El número es mayor que 5")
    print("El número es = ", x)
elif x == 5:
    print("El número es 5")
    print("El número es = ", x)
else:
    print("El número es menor que 5")
    print("El número es = ", x)