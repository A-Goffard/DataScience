# Búsqueda Binaria: Escribe una función que realice una búsqueda  binaria en 
# una lista ordenada de números enteros. 
# Algoritmo: 

# FUNCION crearLista(): 
#  cuantosNumeros = LEER_ENTRADA("Introduce cuantos numeros vas a  meter en la lista a ordenar: ")) 
#  lista=[] 
""" Quieres que el usuario meta los números a añadir en la lista uno a uno ¿o qué pides con esto?"""
#  DE 0 A cuantosNumeros-1+1:ind 
""" es un bucle? """
#  lista.append = LEER_ENTRADA(f"Introduce elemento número  {ind+1}, en lista a ordenar: "))) 
#  retornar lista 

""" Porqué repetimos esto? cual es la finalidad de hacer dos listas así? """
# FUNCIÓN crear_lista_ordenada(): 
#  cuantosNumeros = LEER_ENTRADA("Introduce cuantos numeros vas a  meter en la lista ordenada: ") 
#  lista=[] 

#  DE 0 A cuantosNumeros-1:ind 
#  lista[ind]= LEER_ENTRADA(f"Introduce elemento a número  ",ind+1," en la lista ordenada: ") 
#  retornar lista

""" de donde saco el parametro de numero? ¿inicio y fin te refieres a la longitud de la lista?"""
""" que lista quieres que use? la primera o la segunda? y para que es la otra? """
# FUNCION busqueda_binaria(lista, numero, inicio, fin):  if inicio > fin: 
#  return -1 

#  centro = (inicio + fin) // 2 

#  if lista[centro] == numero: 
#  retornar centro 
""" si pasas un codigo hecho al programador mal hecho sustituyendo solo las palabras que quieres que cambie para seguir ese código no se puede implementar """
#  sino si lista[centro] < numero: 
#  retornar busqueda_binaria(lista, numero, centro + 1, fin)  sino: 
#  retornar busqueda_binaria(lista, numero, inicio, centro - 1)
""" para que crear funciones que luego no se usan?"""
# FUNCION main(): 
#  lista = crearLista() 
#  numero = Entero(LEER_ENTRADA("Introduce el numero a buscar en  la lista ya introducida: ")) 
#  inicio = 0 
#  fin = tamaño(lista) - 1 
#  resultado = busqueda_binaria(lista, numero, inicio, fin) 
"""No se puede hacer <> he puesto != """
#  si resultado <> -1: 
#  mostrar("El numero a buscar se encuentra en la posicion  ",resultado) 
#  sino 
#  mostrar("El numero a buscar no se encuentra en la lista") """ 

def crearLista():
    cuantosNumeros = int(input("Introduce cuantos numeros vas a  meter en la lista a ordenar: ") )
    lista=[]
    ind=0
    while ind < cuantosNumeros:
        lista.append(input(f"Introduce elemento número  {ind+1}, en lista a ordenar: "))
        ind += 1
    print(lista)
    return lista
    
def crear_lista_ordenada():
    cuantosNumeros = int(input("Introduce cuantos numeros vas a  meter en la lista ordenada: ") )
    lista=[]
    ind=0
    while ind < cuantosNumeros:
        lista.append(input(f"Introduce elemento número  {ind+1}, en lista ordenada: "))
        ind += 1
    print(lista)
    
def busqueda_binaria(lista, numero, inicio, fin):
    if inicio > fin:
        return -1
    centro = (inicio + fin) // 2
    if lista[centro] == numero: 
        return centro 
    elif int(lista[centro]) < int(numero): 
        return busqueda_binaria(lista, numero, centro + 1, fin)  
    else: 
        return busqueda_binaria(lista, numero, inicio, centro - 1)
    
def main():

    lista = crearLista() 
    numero = int(input("Introduce el numero a buscar en  la lista ya introducida: ")) 
    inicio = 0 
    fin = len(lista) - 1
    resultado = busqueda_binaria(lista, numero, inicio, fin) 
    if resultado != -1: 
        print("El numero a buscar se encuentra en la posicion  ",resultado) 
    else: 
        print("El numero a buscar no se encuentra en la lista")
    
if __name__ == "__main__":
    main() 