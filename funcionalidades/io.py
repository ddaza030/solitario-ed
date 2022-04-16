# Funcion pa printear
from clases.incial import Inicial
from clases.final import Final
from funcionalidades import funcion
from clases.juego import Juego


def printear(Juego):
    """se debe printear así

    (torres)                   (ultima carta del a baraja)
AP	AC -- --               2C

7T	 --   --   --   --   --    --       (columnas iniciales)
     JP   --   --   --   --    --
          6D   --   --   --    --
		       QC   --   --    --
			        9T   --    --
				         8D    --
					           10D

    """
    #Printeo de las Torres finales
    for i in range(4):
        if len(Juego.finales[i].cartas)==0:
            print("{:6}".format('--'),end="")
        else:
            print("{:6}".format(str(funcion.simbolos(Juego.finales[i].cartas[-1][0]))+Juego.finales[i].cartas[-1][1]),end="")
    
    #Printeo de la Baraja, se printea la cartica que está suelta, o destapda
    if len(Juego.baraja)!=0:
        print("{:12}".format(' '),end="")
        print("{:6}".format(str(funcion.simbolos(Juego.suelta[0]))+Juego.suelta[-1]))

    else:
        print("{:12}".format(' '),end="")
        print("{:6}".format('--'))
    
    print()

    #Lista de cada columna con sus elementos en modo string
    ini=[]
    for element in Juego.iniciales:
        column=["--"]*len(element.invisibles)
        column+=[str(funcion.simbolos(carta[0]))+carta[1] for carta in element.visibles]
        ini.append(column)
    

    longestcol=len(max(ini,key=len))      #sacando la columna mas larga

    #Printeo de esta lista
    for i in range(len(ini)):
        for j in range(longestcol):
            try:
                print("{:6}".format(ini[j][i]),end="")
            except:
                print("{:6}".format(' '),end="")
        print()


# Funcion para movimientos
def movimientos(juego):
    movim = int(input("¿Qué movimiento deseas realizar?Ingresa solo el número:\n" +
                        "0. Cerrar el Juego\n" +
                      "1. Mover de columna A a B n (cantidad de cartas a mover)\n" +
                      "2. Destapar cola de arraste\n" +
                      "3. Reiniciar cola de arraste\n" +
                      "4. Mover de cola de arraste a torre final X\n" +
                      "5. Mover de cola de arraste a columna Y\n" +
                      "6. Mover de columna Y a torre final X\n" +
                      "7. Mover de torre final X a columna Y\n"))
    if movim == 0:
        juego.abierto=False

    elif movim == 1:
        a, b, n = tuple(map(int, input("Por favor ingresa los datos así: A B n\n" +
                                       "A:Corresponde a la columna origen\n" +
                                       "B:Corresponde a la columna destino\n" +
                                       "n:Corresponde a cantidad de cartas que se desplazarán\n").split()))

        verdad_absoluta = funcion.pasar_columnas(juego.iniciales[a - 1], juego.iniciales[b - 1], n)
        if verdad_absoluta:
            #printear(juego)
            pass
        else:
            print("Movimiento inválido, intente de nuevo")
            print()
            #printear()
            #movimientos(juego)

    elif movim == 2:
        juego.destapar()
        #printear()

    elif movim == 3:
        juego.reiniciar_cola()
        #printear()

    elif movim == 4:
        col=int(input("Ingrese el numero de la torre al que quiere llevar la carta:\n"))
        carta = juego.suelta
        if juego.finales[col-1].poner(carta):
            pass
        else:
            print("Movimiento inválido, intente de nuevo")

    elif movim == 5:
        a = int(input("Por favor ingresa los datos así: A\n" +
                                       "A:Corresponde a la columna destino\n"))

        verdad_absoluta = funcion.pasar_arrastre_columna(juego.suelta,juego.iniciales[a - 1])
        if verdad_absoluta:
            #printear(juego)
            juego.suelta=juego.baraja.popleft()
            pass
        else:
            print("Movimiento inválido, intente de nuevo")
            print()
            #printear()
            #movimientos(juego)

    elif movim == 6:
        pass

    elif movim == 7:
        pass


'''
Ensayo
n = [(9,1),(3,2),(2,4)]
while True:
    if referencia_baraja[0] == n[0][0] and referencia_baraja[1] == n[0][1]:
        break
    else:
        e=n.popleft()
        n.append(e)
     

#print(n[0][1] == referencia_baraja[1])

pila = deque()
def destapar():
    if len(n)>0:
        pila.append(n.popleft())
    else:
        return "Reinicia por favor la cola de arrastre"    
    return pila[-1]


'''
