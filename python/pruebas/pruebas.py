def sumar (num1, num2):
    return num1 + num2

def restar (num1, num2):
    return num1 - num2

def pedir_numero ():
    num = int(input("Inserta un número, por favor "))
    return num

def menu():
    print("Opciones: ")
    print("1) Sumar: ")
    print("2) Restar: ")
    print("3) Salir: ")
    opc = int(input("Elige una opción: "))
    return opc

def operativa(num1, num2, opc):
    if opc == 1:
        resul = sumar(num1, num2)
    elif opc == 2:
        resul = restar(num1, num2)
    else:
        print("Agur!")
        print("True: ", True, "True int: ", int(True))
        resul = True
    return int(resul)

def main():
    opc = menu()
    num1 = pedir_numero()
    num2 = pedir_numero()
    
    operativa(num1, num2, opc)
    
    
if __name__ == "__main__": 
    main()