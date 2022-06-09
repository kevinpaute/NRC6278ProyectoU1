import re #validar datos

def validar_entrada(entrada):
    '''
    Funcion que valida la entrada del usuario sea de 0 y 1
    '''
    if re.match("^[0-1]{1}$", entrada):
        return True
    else:
        return False

#validar datos de ingreso de la A a la G
def validar_entrada_A_G(entrada):
    '''
    Funcion que valida que la entrada sea una letra entre A y G
    '''
    if re.match("^[A-G]{1}$", entrada):
        return True
    else:
        return False
