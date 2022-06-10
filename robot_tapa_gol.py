#algoritmo agente robot arquero con siete ubicación

#Importar libreria va
from validacion_entrada import *
costo = 0
estado_meta = {'A':'0', 'B':'0', 'C':'0', 'D':'0', 'E':'0', 'F':'0', 'G':'0'}
ubicacion = ''

def arco_accion1(costo, ubicacion, estado_meta):
        estado_arco=input(print("\nIngrese el estado del arco ", ubicacion))
        
        if validar_entrada(estado_arco)==True:
            print("\nFutbolista patea el balón al arco ", ubicacion)
            print("Costo del movimiento: ", costo)
            estado_meta[ubicacion] = '0'
            costo += 1
            print("El robot tapa el balón")
            print("Costo del movimiento: ", costo)

def arco_accion2(costo, ubicacion, estado_meta):
        estado_arco=input(print("\nIngrese el estado del arco ", ubicacion))
        while True:
            if validar_entrada(estado_arco)==True:
                if estado_arco == '1':
                    print("\nFutbolista patea el balón al arco ", ubicacion)
                    print("El robot se mueve al arco ", ubicacion)
                    costo += 1
                    print("Costo del movimiento: ", costo)
                    estado_meta[ubicacion] = '0'
                    costo += 1
                    print("El robot tapa el balón")
                    print("Costo del movimiento: ", costo)
                elif estado_arco == '0':
                    print("\nFutbolista patea el balón al arco ", ubicacion)
                    print("El robot se mueve al arco ", ubicacion)
                    costo += 1
                    print("Costo del movimiento: ", costo)
                    estado_meta[ubicacion] = '1'
                    costo += 1
                    print("El robot no tapa el balón")
                    print("Costo del movimiento: ", costo)
                break
            else:
                print("\nIngrese una entrada valida")
        


def ubicacion_accion1():
    if ubicacion == 'A':
        arco_accion1(costo, ubicacion, estado_meta)

def validacion_ubicacion(ubicacion):
    while True:
        ubicacion = str(input("Ingrese la ubicacion del arco: "))
        if validar_entrada_A_G(ubicacion) == True:
            break
        else:
            print("\nIngrese una ubicacion valida")

def arcoA():

    
    while True:
        ubicacion = str(input("Ingrese la ubicacion del arco: "))
        if validar_entrada_A_G(ubicacion) == True:
            break
        else:
            print("\nIngrese una ubicacion valida")

    if ubicacion == 'A':
        arco_accion1(costo, ubicacion, estado_meta)
        if ubicacion == 'B':
            arco_accion2(costo, ubicacion, estado_meta)
    elif ubicacion == 'B':
        arco_accion1(costo, ubicacion, estado_meta)
    elif ubicacion == 'C':
        arco_accion1(costo, ubicacion, estado_meta)
    elif ubicacion == 'D':
        arco_accion1(costo, ubicacion, estado_meta)
    elif ubicacion == 'E':
        arco_accion1(costo, ubicacion, estado_meta)
    elif ubicacion == 'F':
        arco_accion1(costo, ubicacion, estado_meta)
    elif ubicacion == 'G':
        arco_accion1(costo, ubicacion, estado_meta)