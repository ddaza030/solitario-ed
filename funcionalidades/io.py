#Funcion pa printear
def printear():
    pass


#Funcion para movimientos
def movimientos():
    movim = int(input("¿Qué movimiento deseas realizar?Ingresa solo el número:\n"+
                    "1. Mover de columna A a B n (cantidad de cartas a mover)\n"+
                    "2. Destapar cola de arraste\n"+
                    "3. Reiniciar cola de arraste\n"+
                    "4. Mover de cola de arraste a torre final X\n"+
                    "5. Mover de cola de arraste a columna Y\n"+
                    "6. Mover de columna Y a torre final X\n"+
                    "7. Mover de torre final X a columna Y\n"))
    if movim == 1:
        cartas = tuple(input("Por favor ingresa los datos así: A B n\n"+
                            "A:Corresponde a la columna origen\n"+
                            "B:Corresponde a la columna destino\n"+
                            "n:Corresponde a cantidad de cartas que se desplazarán\n").split())
        
    elif movim == 2:
        destapar()
        printear()

    elif movim == 3:
        reiniciar_cola()
        printear()

    elif movim == 4:
        carta = sacar_cola()
        final.poner(carta)
        printear()
        pass
    elif movim == 5:
        carta = sacar_cola()
        inicial.anadir(carta)
        pass

    elif movim == 6:
        pass

    elif movim == 7:            
        pass


'''
Ensayo
while True:
    i=0
    if referencia_baraja[0] == n[0][0] and referencia_baraja[1] == n[0][1]:
        break
    else:
        e=n.popleft()
        n.append(e)
        print(n)     

#print(n[0][1] == referencia_baraja[1])

pila = deque()
def destapar():
    if len(n)>0:
        pila.append(n.popleft())
    else:
        return "Reinicia por favor la cola de arrastre"    
    return pila[-1]


'''