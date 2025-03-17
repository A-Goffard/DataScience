def sumar (num1, num2):
    return num1 + num2

def restar (num1, num2):
    return num1 - num2

def pedir_numero ():
    num = int(input("Inserta un número, por favor "))
    return num

def main():
    num1 = pedir_numero()
    num2 = pedir_numero()
    
    print(sumar(num1, num2))
    print(restar(num1, num2))
    
    
if __name__ == "__main__": 
    main()