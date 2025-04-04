# Detección de Anagramas: Crea una función que determine si dos
# cadenas de texto son anagramas (contienen las mismas letras en diferente
# orden).
# - Solicitar cadenaTexto1
# - Solicitar cadenaTexto2
# Función anagrama:
# - Eliminar espacios y convertir a minúsculas
# - Ordenar carácteres de menor a mayor en cadenaTexto1 y cadenaTexto2
# - Si cadenaTexto1ordenada y cadenaTexto2ordenada son iguales:
# - Mostrar: “Es un anagrama”
# - Si no:
# - Mostrar: “No es un anagrama”
# --------------------------------------------------------------------------------
# def ingresar_datos():

#     cadena1 = str(input("Introduce texto 1 : "))        #Ingresa cadena1
#     cadena2 = str(input("Introduce texto 2 : "))        #Ingresa cadena2

#     cadena1Low = cadena1.lower()                          #Minuscula cadena1
#     cadena2Low = cadena2.lower()                          #Minuscula cadena2

#     cadena1Done = cadena1Low.replace(" ","")              #SinEspacio cadena1
#     cadena2Done = cadena2Low.replace(" ","")              #SinEspacio cadena2

#     if sorted(cadena1Done) == sorted(cadena2Done):
#         print("Es un anagrama")
#         return True
        
#     else:
#         print("No es un anagrama")
    
    
# def anagrama():
#     while True:
#         if ingresar_datos():
#             break
#         print("Ingrese otras cadenas")
        
# anagrama()

def anagrama():

    cadenaTexto1 = input("Introduce texto 1 : ") 
    cadenaTexto2 = input("Introduce texto 2 : ")  

    cadenaTexto1_ordenada = cadenaTexto1.lower().replace(" ","")                   
    cadenaTexto2_ordenada = cadenaTexto2.lower().replace(" ","")                


    if sorted(cadenaTexto1_ordenada) == sorted(cadenaTexto2_ordenada):
        print("Es un anagrama")
        return True

    else:
        print("No es un anagrama")


anagrama()
