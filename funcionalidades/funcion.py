from collections import deque


def simbolos(numero):
    """Funcion para cambiar de numeros a las letras correspondientes"""
    if numero==1:
        return "A"
    elif numero==11:
        return "J"
    elif numero==12:
        return "Q"
    elif numero==13:
        return "K"
    return numero


def pasar_columnas(from_, to, cantidad):
    """Metodo para pasar cartas de un objeto Inicial al otro, devuelve True
        o False depende de si se termino o no el movimiento

        args:
            to (Inicial): es la baraja hacia la que se dirije el movimiento
            from_ (Inicial): corresponde a la baraja desde donde se hace el movimiento"""

    # corresponde al caso en el que existen cartas visibles en la bajara a la que se direge
    if len(to.visibles) != 0 and cantidad <= len(from_.visibles):

        carta_up = to.visibles[-1]
        carta_down = from_.visibles[-cantidad]
        colores = False

        # se revisa que el cambio por parte de colores se pueda hacer
        if (carta_up[1] == 'D' or carta_up[1] == 'C') and \
                (carta_down[1] == 'T' or carta_down[1] == 'P'):
            colores = True
        elif (carta_up[1] == 'T' or carta_up[1] == 'P') and \
                (carta_down[1] == 'D' or carta_down[1] == 'C'):
            colores = True

        if carta_up[0]-1 == carta_down[0] and colores:
            to.anadir(from_.agarrar(cantidad))
            return True

        return False

    # corresponde al caso en el que no hay cartas en to
    elif len(to.visibles) == 0 and cantidad <= len(from_.visibles):
        carta_down = from_.visibles[-cantidad]

        if carta_down[0] == 13:
            to.anadir(from_.agarrar(cantidad))
            return True

    return False


def pasar_arrastre_columna(carta, to):
    """Metodo para pasar cartas de un objeto Inicial al otro, devuelve True
        o False depende de si se termino o no el movimiento

        args:
            to (Inicial): es la baraja hacia la que se dirije el movimiento
            carta (tuple): corresponde a la carta suelta en Juego"""

    # corresponde al caso en el que existen cartas visibles en la bajara a la que se direge
    if carta is not None:

        carta_up = to.visibles[-1]
        colores = False

        # se revisa que el cambio por parte de colores se pueda hacer
        if (carta_up[1] == 'D' or carta_up[1] == 'C') and \
                (carta[1] == 'T' or carta[1] == 'P'):
            colores = True
        elif (carta_up[1] == 'T' or carta_up[1] == 'P') and \
                (carta[1] == 'D' or carta[1] == 'C'):
            colores = True

        if carta_up[0]-1 == carta[0] and colores:
            to.anadir([deque(carta)])

            return True

        return False

    # corresponde al caso en el que no hay cartas en to
    elif len(to.visibles) == 0 and\
            carta is not None:

        if carta[0] == 13:
            to.anadir(deque(carta))
            return True

    return False
