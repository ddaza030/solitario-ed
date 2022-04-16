from collections import deque


class Inicial:

    def __init__(self, cartas):
        self.visibles = deque([cartas[-1]])
        self.invisibles = deque(cartas[:-1])

    def agarrar(self, cantidad):
        conjunto_en_mano = deque()
        tamano = len(self.visibles)

        if cantidad < tamano:
            for i in range(cantidad):
                conjunto_en_mano.append(self.visibles.pop())
        if cantidad == tamano:
            try:
                for i in range(cantidad):
                    conjunto_en_mano.append(self.visibles.pop())
                    
                self.visibles.append(self.invisibles.pop())
                #self.invisibles.append(self.visibles.pop())
            except IndexError:
                pass

        return conjunto_en_mano

    def anadir(self, conjunto_en_mano):
        for i in range(len(conjunto_en_mano)):
            self.visibles.append(conjunto_en_mano.pop())





