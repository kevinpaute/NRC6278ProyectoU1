from validacion_entrada import *
import emoji

estado_meta = {'A':'0', 'B':'0', 'C':'0', 'D':'0', 'E':'0', 'F':'0', 'G':'0'}
arcos = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def robot_tapa_gol(): 
    """
    Método que determina si el robot tape o no tape el gol segun el estado de la ubicacion
    
    Parámetros:
    -----------
    No recibe parámetros

    Retorna:
    --------
    No retorna nada, solo imprime el resultado
    
    """
    # Inicializacion de costo
    costo = 0
    # Ciclo para recorrer los arcos
    while True:
        # Se solicita la ubicacion del arco
        ubicacion = str(input("Ingrese la ubicacion del arco 🥅: "))
        # Se valida las entrada que sean solo letras desde la A hasta la G
        if validar_entrada_A_G(ubicacion):
            # Se valida que el arco no este en el estado meta
            while True:
                # Se solicita el estado actual del robot
                print("Ingrese el estado del arco ", ubicacion, " 🥅: ")
                # Se valida que el estado sea solo el 0 y 1
                estado_arco=input()
                if validar_entrada(estado_arco)==True:
                    #Si el estado es 1 se suma 1 al costo 
                    if estado_arco == '1':
                        #Accion donde futbolista lanza la pelota
                        print("Futbolista🧍🏻 patea el balón ⚽ al arco ", ubicacion," 🥅")
                        #El estado del arco se pone en 0
                        estado_meta[ubicacion] = '0'
                        #Se suma 1 al costo
                        costo += 1
                        #Imprime mensaje de el robot tape el gol
                        print("El robot🤖 tapa el balón ⚽")
                        #Se imprime el costo del robot
                        print("El futbolista no anota un gol 🤔")
                        print("Costo del movimiento: ", costo)
                        #Se sale del ciclo
                    #Si el estado es 0 se suma 1 al costo
                    elif estado_arco == '0':
                        #Accion donde futbolista lanza la pelota
                        print("Futbolista🧍🏻 patea el balón ⚽ al arco ", ubicacion, " 🥅")
                        #El estado del arco se pone en 1
                        estado_meta[ubicacion] = '1'
                        #Se suma 1 al costo
                        costo += 1
                        #Imprime mensaje de el robot tape el gol
                        print("El robot🤖 no tapa el balón ⚽")
                        print("El futbolista anota gol 🥇")
                        print("Costo del movimiento: ", costo)
                    

                    # Ciclo para recorrer los arcos 
                    for i in range(0,7,1): 
                        # Si la ubicacion del arco es igual a la lista de arcos
                        if ubicacion == arcos[i]:
                            #Omite el arco que se esta evaluando
                            pass
                        else: 
                            while True:
                                # Se solicita el estado actual del arco
                                print("\nIngrese el estado del arco ", arcos[i],"🥅: ")
                                estado_arco = input()
                                # Se valida que el estado sea solo el 0 y 1
                                if validar_entrada(estado_arco)==True:
                                    #Si el estado es 1 se suma 1 al costo
                                    if estado_arco == '1':
                                        print("\nFutbolista🧍🏻 patea el balón⚽ al arco ", arcos[i], " 🥅")
                                        print("El robot🤖 se mueve al arco ", arcos[i], " 🥅")
                                        costo += 1
                                        print("Costo del movimiento: ", costo)
                                        #El estado del arco se pone en 0
                                        estado_meta[arcos[i]] = '0'
                                        costo += 1
                                        #Imprime mensaje de el robot tapa el gol
                                        print("El robot🤖 tapa el balón⚽ ")
                                        print("El futbolista no anota un gol 🤔")
                                        print("Costo del movimiento: ", costo)
                                    elif estado_arco == '0':
                                        print("\nFutbolista🧍🏻 patea el balón⚽ al arco ", arcos[i], " 🥅")
                                        print("El robot🤖 se mueve al arco ", arcos[i])
                                        costo += 1
                                        print("Costo del movimiento: ", costo)
                                        estado_meta[arcos[i]] = '1'
                                        costo += 1
                                        print("El robot🤖 no tapa el balón⚽")
                                        print("El futbolista anota gol 🥇")
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