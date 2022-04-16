from clases.final import Final
from clases.incial import Inicial
from clases.juego import Juego
from funcionalidades import io
from funcionalidades import funcion


if __name__ == "__main__":
    juego = Juego()
    while juego.abierto:
        total=sum(len(i.cartas) for i in juego.finales)
        if total==len(juego.cartas1):
            print("-----------------------CORONO GONORREA---------------------------------")
            break
        io.printear(juego)
        io.movimientos(juego)

