from validacion_entrada import *

estado_meta = {'A':'0', 'B':'0', 'C':'0', 'D':'0', 'E':'0', 'F':'0', 'G':'0'}
arcos = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def robot_tapa_gol(): 
    '''
    Método que determina si el robot tape o no tape el gol segun el estado de la ubicacion

    '''
    costo = 0
    while True:
        ubicacion = str(input("Ingrese la ubicacion del arco: "))
        if validar_entrada_A_G(ubicacion):
            while True:
                print("Ingrese el estado del arco", ubicacion)
                estado_arco=input()
                if validar_entrada(estado_arco)==True:
                    if estado_arco == '1':
                        print("Futbolista patea el balón al arco ", ubicacion)
                        estado_meta[ubicacion] = '0'
                        costo += 1
                        print("El robot tapa el balón")
                        print("Costo del movimiento: ", costo)
                    elif estado_arco == '0':
                        print("Futbolista patea el balón al arco ", ubicacion)
                        estado_meta[ubicacion] = '1'
                        costo += 1
                        print("El robot no tapa el balón")
                        print("Costo del movimiento: ", costo)
                    
                    for i in range(0,7,1):
                        if ubicacion == arcos[i]:
                            pass
                        else: 

                            while True:
                                print("\nIngrese el estado del arco ", arcos[i])
                                estado_arco = input()
                                if validar_entrada(estado_arco)==True:
                                    if estado_arco == '1':
                                        print("\nFutbolista patea el balón al arco ", arcos[i])
                                        print("El robot se mueve al arco ", arcos[i])
                                        costo += 1
                                        print("Costo del movimiento: ", costo)
                                        estado_meta[arcos[i]] = '0'
                                        costo += 1
                                        print("El robot tapa el balón")
                                        print("Costo del movimiento: ", costo)
                                    elif estado_arco == '0':
                                        print("\nFutbolista patea el balón al arco ", arcos[i])
                                        print("El robot se mueve al arco ", arcos[i])
                                        costo += 1
                                        print("Costo del movimiento: ", costo)
                                        estado_meta[arcos[i]] = '1'
                                        costo += 1
                                        print("El robot no tapa el balón")
                                        print("Costo del movimiento: ", costo)
                                    break
                                else:
                                    print("Ingrese un estado valido")

                    break
                else:
                    print("Ingrese un estado valido")
            break
        else:
            print("Ingrese una ubicacion valido")


robot_tapa_gol()