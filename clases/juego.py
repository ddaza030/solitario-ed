from collections import deque
from clases.final import Final
from clases.incial import Inicial

import random

class Juego:

    cartas1 = [(i,j) for i in range(1,14) for j in ["P","C","T","D"]]
    #cartas2 = [(j,i) for i in ["A","J","Q","K"] for j in ["P","C","T","D"]]

    def __init__(self):
        self.abierto = True
        self.baraja=deque(Juego.cartas1.copy())
        self.sueltas = deque()
        random.shuffle(self.baraja) # Baraja de cartas del juego desordenadas
        self.iniciales=list()

        for i in range(1,8): #Creacion de cada una de las columnas iniciales
            listaInicial=list() #creacion de la columan inicial
            for j in range(i):
                listaInicial.append(self.baraja.pop()) #agregar cartas desde la baraja inicial a la columna
            self.iniciales.append(Inicial(listaInicial)) #agregar desde la inicial

        self.finales=list()

        for i in range(4): #Creacion de la columna de finales
            f=Final()
            self.finales.append(f)

        self.referencia_baraja = self.baraja[0]

    def destapar(self):
        if len(self.baraja) != 0:
            self.sueltas.append(self.baraja.popleft())
            return True
        else:
            return False

    def reiniciar_cola(self):
        if len(self.baraja) != 0:
            return False
        elif len(self.sueltas) == 0:
            return False
        else:
            while len(self.sueltas) != 0:
                self.baraja.append(self.sueltas.popleft())
            return True


"""
juego=Juego()
for i in range(len(juego.iniciales)):
    print(juego.iniciales[i])"""








