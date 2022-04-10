class Final:
    def __init__(self,cartas = tuple(),pinta = None):

        pass

    #Funcion pa poner las cartas en la torre final
    def poner(self, carta):
        if len(self.cartas) == 0 and carta[0] == 1:       #Si la torre está vacía entonces se debe appendear un As y se asigna la pinta del As a la torre
            self.cartas.append(carta)
            self.pinta = carta[1]

        elif self.cartas[-1][0] < carta[0] and carta[1] == self.pinta:    #Si la ultima carta de la torre es menor a la que se va a poner y es de la misma pinta que se appendee
            self.cartas.append(carta)
        else:
            return False
    
    
    

        

        

