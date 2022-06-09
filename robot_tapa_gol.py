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

    print("El robot esta en el arco A")
    if estado_arcoA == '1':
        print("Futbolista patea el balón hacia el arco A")
        estado_meta['A'] = '0'
        costo += 1
        print("El robot tapa el balón en el arco A")
        print("Costo del movimiento: ", costo)
        
        if estado_arcoB == '1':
            print("\nFutbolista patea el balón al arco B")
            print("El robot se mueve al arco B")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['B'] = '0'
            costo += 1
            print("El robot tapa el balón")
            print("Costo del movimiento: ", costo)

        elif estado_arcoB == '0':
            print("\nFutbolista patea el balón al arco B")
            print("El robot se mueve al arco B")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['B'] = '1'
            costo += 1
            print("El robot no tapa el balón")
            print("Costo del movimiento: ", costo)

        if estado_arcoC == '1':
            print("\nFutbolista patea el balón al arco C")
            print("El robot se mueve al arco C")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['C'] = '0'
            costo += 1
            print("El robot tapa el balón")
            print("Costo del movimiento: ", costo)

        elif estado_arcoC == '0':
            print("\nFutbolista patea el balón al arco C")
            print("El robot se mueve al arco C")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['C'] = '1'
            costo += 1
            print("El robot no tapa el balón")
            print("Costo del movimiento: ", costo)

        if estado_arcoD == '1':
            print("\nFutbolista patea el balón al arco D")
            print("El robot se mueve al arco D")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['D'] = '0'
            costo += 1
            print("El robot tapa el balón")
            print("Costo del movimiento: ", costo)

        elif estado_arcoD == '0':
            print("\nFutbolista patea el balón al arco D")
            print("El robot se mueve al arco D")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['D'] = '1'
            costo += 1
            print("El robot no tapa el balón")
            print("Costo del movimiento: ", costo)

        if estado_arcoE == '1':
            print("\nFutbolista patea el balón al arco E")
            print("El robot se mueve al arco E")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['E'] = '0'
            costo += 1
            print("El robot tapa el balón")
            print("Costo del movimiento: ", costo)

        elif estado_arcoE == '0':
            print("\nFutbolista patea el balón al arco E")
            print("El robot se mueve al arco E")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['E'] = '1'
            costo += 1
            print("El robot no tapa el balón")
            print("Costo del movimiento: ", costo)

        if estado_arcoF == '1':
            print("\nFutbolista patea el balón al arco F")
            print("El robot se mueve al arco F")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['F'] = '0'
            costo += 1
            print("El robot tapa el balón")
            print("Costo del movimiento: ", costo)

        elif estado_arcoF == '0':
            print("\nFutbolista patea el balón al arco F")
            print("El robot se mueve al arco F")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['F'] = '1'
            costo += 1
            print("El robot no tapa el balón")
            print("Costo del movimiento: ", costo)

        if estado_arcoG == '1':
            print("\nFutbolista patea el balón al arco G")
            print("El robot se mueve al arco G")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['G'] = '0'
            costo += 1
            print("El robot tapa el balón")
            print("Costo del movimiento: ", costo)

        elif estado_arcoG == '0':
            print("\nFutbolista patea el balón al arco G")
            print("El robot se mueve al arco G")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['G'] = '1'
            costo += 1
            print("El robot no tapa el balón")
            print("Costo del movimiento: ", costo)


    elif estado_arcoA == '0':
        print("Futbolista patea el balón hacia el arco A")
        estado_meta['A'] = '1'
        costo += 1
        print("El robot no tapa el balón en el arco A")
        print("Costo del movimiento: ", costo)
        
        if estado_arcoB == '1':
            print("\nFutbolista patea el balón al arco B")
            print("El robot se mueve al arco B")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['B'] = '0'
            costo += 1
            print("El robot tapa el balón")
            print("Costo del movimiento: ", costo)

        elif estado_arcoB == '0':
            print("\nFutbolista patea el balón al arco B")
            print("El robot se mueve al arco B")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['B'] = '1'
            costo += 1
            print("El robot no tapa el balón")
            print("Costo del movimiento: ", costo)

        if estado_arcoC == '1':
            print("\nFutbolista patea el balón al arco C")
            print("El robot se mueve al arco C")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['C'] = '0'
            costo += 1
            print("El robot tapa el balón")
            print("Costo del movimiento: ", costo)

        elif estado_arcoC == '0':
            print("\nFutbolista patea el balón al arco C")
            print("El robot se mueve al arco C")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['C'] = '1'
            costo += 1
            print("El robot no tapa el balón")
            print("Costo del movimiento: ", costo)

        if estado_arcoD == '1':
            print("\nFutbolista patea el balón al arco D")
            print("El robot se mueve al arco D")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['D'] = '0'
            costo += 1
            print("El robot tapa el balón")
            print("Costo del movimiento: ", costo)

        elif estado_arcoD == '0':
            print("\nFutbolista patea el balón al arco D")
            print("El robot se mueve al arco D")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['D'] = '1'
            costo += 1
            print("El robot no tapa el balón")
            print("Costo del movimiento: ", costo)

        if estado_arcoE == '1':
            print("\nFutbolista patea el balón al arco E")
            print("El robot se mueve al arco E")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['E'] = '0'
            costo += 1
            print("El robot tapa el balón")
            print("Costo del movimiento: ", costo)

        elif estado_arcoE == '0':
            print("\nFutbolista patea el balón al arco E")
            print("El robot se mueve al arco E")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['E'] = '1'
            costo += 1
            print("El robot no tapa el balón")
            print("Costo del movimiento: ", costo)

        if estado_arcoF == '1':
            print("\nFutbolista patea el balón al arco F")
            print("El robot se mueve al arco F")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['F'] = '0'
            costo += 1
            print("El robot tapa el balón")
            print("Costo del movimiento: ", costo)

        elif estado_arcoF == '0':
            print("\nFutbolista patea el balón al arco F")
            print("El robot se mueve al arco F")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['F'] = '1'
            costo += 1
            print("El robot no tapa el balón")
            print("Costo del movimiento: ", costo)

        if estado_arcoG == '1':
            print("\nFutbolista patea el balón al arco G")
            print("El robot se mueve al arco G")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['G'] = '0'
            costo += 1
            print("El robot tapa el balón")
            print("Costo del movimiento: ", costo)

        elif estado_arcoG == '0':
            print("\nFutbolista patea el balón al arco G")
            print("El robot se mueve al arco G")
            costo += 1
            print("Costo del movimiento: ", costo)
            estado_meta['G'] = '1'
            costo += 1
            print("El robot no tapa el balón")
            print("Costo del movimiento: ", costo)

    print("\nEstado de la meta: ")
    print(estado_meta)
    # Imprimir el costo de las acciones realizadas
    print("Medida de desempeño: " + str(costo))

def arcoB():
    costo=0
    while True:
        estado_arcoB = input("Ingrese el estado del arco B: ")
        if validar_entrada(estado_arcoB)==True:
            break
        else:
            print("Ingrese un estado valido para el arco B")
    while True:
        estado_arcoA = input("Ingrese el estado del arco A: ")
        if validar_entrada(estado_arcoA)==True:
            break
        else:
            print("Ingrese un estado valido para el arco A")
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

    estado_meta = {'A': estado_arcoA, 'B': estado_arcoB, 'C': estado_arcoC, 'D': estado_arcoD, 'E': estado_arcoE, 'F': estado_arcoF, 'G': estado_arcoG}
       

    print("\nEl robot se mueve al arco B")
    costo += 1
    print("Costo del movimiento: ", costo)
    estado_meta['B'] = '0'
    costo += 1
    print("El robot tapa el balón")
    print("Costo del movimiento: ", costo)