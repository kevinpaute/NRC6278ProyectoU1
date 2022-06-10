from validacion_entrada import *

estado_meta = {'A':'0', 'B':'0', 'C':'0', 'D':'0', 'E':'0', 'F':'0', 'G':'0'}
lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def acciones_por_estado():
    costo = 0
    while True:
        ubicacion = input("Ingrese la ubicacion del arco: ")
        if validar_entrada(ubicacion):
            print("Ingrese el estado del arco", ubicacion)
            estado_arco=input()
            while True:
                if validar_entrada(estado_arco)==True:
                    print("Futbolista patea el balón al arco ", ubicacion)
                    estado_meta[ubicacion] = '0'
                    costo += 1
                    print("El robot tapa el balón")
                    print("Costo del movimiento: ", costo)
                    # Un for que no me incluya la lista [A]
                    for i in range(1,8,1):
                        if i == ubicacion:
                            pass
                        else:
                            estado_arco = input()
                            print("\nIngrese el estado del arco ", lista[i])
                            while True:
                                if validar_entrada(estado_arco)==True:
                                    if estado_arco == '1':
                                        print("\nFutbolista patea el balón al arco ", lista[i])
                                        print("El robot se mueve al arco ", lista[i])
                                        costo += 1
                                        print("Costo del movimiento: ", costo)
                                        estado_meta[lista[i]] = '0'
                                        costo += 1
                                        print("El robot tapa el balón")
                                        print("Costo del movimiento: ", costo)
                                    elif estado_arco == '0':
                                        print("\nFutbolista patea el balón al arco ", lista[i])
                                        print("El robot se mueve al arco ", lista[i])
                                        costo += 1
                                        print("Costo del movimiento: ", costo)
                                        estado_meta[lista[i]] = '1'
                                        costo += 1
                                        print("El robot no tapa el balón")
                                        print("Costo del movimiento: ", costo)
                                    break
                                else:
                                    print("\nIngrese un estado valida")

                    break
                else:
                    print("\nIngrese un estado valida")
            break
        else:
            print("\nIngrese una ubicacion valida")
        
acciones_por_estado()