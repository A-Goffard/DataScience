def sumar(num1, num2):
    return int(num1 + num2)

def restar(num1, num2):
    return int(num1 - num2)

def multiplicar(num1, num2):
    return int(num1 * num2)

def dividir(num1, num2):
    if es_cero(num2):
        num2 = pedir_numero()
        if es_cero(num2):
            return -1
    else:
        print("")
    return int(num1 / num2)

def potencia(num1, num2):
    if es_cero(num2):
        return 1
    else:
        return int(num1 ** num2)

def es_cero(num):
    return num == 0 # si es cero devuelve True, si es distinto, devuelve False
    
def pedir_numero():
    num = int(input("Inserta un número, por favor"))
    return num

def menu():
    print("Opciones: ")
    print("1) Sumar ")
    print("2) Restar ")
    print("3) Multiplicar ")
    print("4) Dividir ")
    print("5) Potencia ")
    print("0) Salir ")
    opc = int(input())
    return opc

def operativa(num1, num2, opc):
    if opc == 1:
        resul = sumar(num1, num2)
    elif opc == 2:
        resul = restar(num1, num2)
    elif opc == 3:
        resul = multiplicar(num1, num2)
    elif opc == 4:
        resul = dividir(num1, num2)
    elif opc == 5:
        resul = potencia(num1, num2)
    else: #cero u otros
        print("¡Hasta luego Mari Carmen!")
        resul = -1
    
    return int(resul) 

def main():
    opc = menu()   
    num1 = pedir_numero()
    num2 = pedir_numero()
    resul = operativa(num1, num2, opc)
    print("El resultado es: ", int(resul))
    
if __name__ == "__main__":
    main()