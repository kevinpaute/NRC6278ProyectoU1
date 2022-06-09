#algoritmo agente robot arquero con siete ubicación

#Importar libreria va
from validacion_entrada import *

estado_meta = {'A':'0', 'B':'0', 'C':'0', 'D':'0', 'E':'0', 'F':'0', 'G':'0'}


def arcoA():
    costo = 0
    
    #Validar todos datos de ingreso string 0 y 1 con ciclo while
    while True:
        estado_arcoA = input("Ingrese el estado del arco A: ")
        if validar_entrada(estado_arcoA)==True:
            break
        else:
            print("Ingrese un estado valido para el arco A")
    while True:
        estado_arcoB = input("Ingrese el estado del arco B: ")
        if validar_entrada(estado_arcoB)==True:
            break
        else:
            print("Ingrese un estado valido para el arco B")
    while True:
        estado_arcoC = input("Ingrese el estado del arco C: ")
        if validar_entrada(estado_arcoC)==True:
            break
        else:
            print("Ingrese un estado valido para el arco C")
    while True:
        estado_arcoD = input("Ingrese el estado del arco D: ")
        if validar_entrada(estado_arcoD)==True:
            break
        else:
            print("Ingrese un estado valido para el arco D")
    while True:
        estado_arcoE = input("Ingrese el estado del arco E: ")
        if validar_entrada(estado_arcoE)==True:
            break
        else:
            print("Ingrese un estado valido para el arco E")
    while True:
        estado_arcoF = input("Ingrese el estado del arco F: ")
        if validar_entrada(estado_arcoF)==True:
            break
        else:
            print("Ingrese un estado valido para el arco F")
    while True:
        estado_arcoG = input("Ingrese el estado del arco G: ")
        if validar_entrada(estado_arcoG)==True:
            break
        else:
            print("Ingrese un estado valido para el arco G")