from clases.final import Final
from clases.incial import Inicial
from clases.juego import Juego
from funcionalidades import io


if __name__ == "__main__":
    juego = Juego()
    while juego.abierto:
        io.printear(juego)
        io.movimientos(juego)

