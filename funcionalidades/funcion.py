def pasar_cartas(from_, to, cantidad):
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
        if carta_up[0] == 'D' or carta_up[0] == 'C' and \
                carta_down[0] == 'T' or carta_down[0] == 'P':
            colores = True
        elif carta_up[0] == 'T' or carta_up[0] == 'P' and \
                carta_down[0] == 'D' or carta_down[0] == 'C':
            colores = True

        if carta_down[0] < carta_up[0] and colores:
            to.anadir(from_.agarrar(cantidad))
            return True

        return False

    # corresponde al caso en el que no hay cartas en to
    elif len(to.visibles) == 0 and cantidad <= len(from_.visibles):
        to.anadir(from_.agarrar(cantidad))
        return True

    return False
