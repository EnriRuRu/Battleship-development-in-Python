import random
import numpy as np

def jugar(tablero_1, tablero_2):

    while tablero_1.quedan_barcos() and  tablero_2.quedan_barcos():

        bandera=True

        while bandera:
            print("turno jugador")
            coord_fila=-1
            coord_columna=-1
            while coord_fila<0 or coord_fila>9:
                coord_fila = int(input( "dame la fila de disparo: " ))
            while coord_columna<0 or coord_columna>9:
                coord_columna = int( input("dame la columna de disparo: "))
            coordenada = [coord_fila, coord_columna]
            if tablero_2.disparo(coordenada) == False:
                bandera = False
            tablero_2.imprimir_mapa_sin_disparos()
                
        print("FALLASTEEE")

        bandera=True

        if tablero_1.quedan_barcos():
        
            while bandera:
                print("turno máquina")
                coord_fila = random.randint(0,9)
                coord_columna = random.randint(0,9)
                coordenada = [coord_fila, coord_columna]
                if tablero_1.disparo(coordenada) == False:
                    bandera = False
                tablero_1.imprimir_mapa()
                print("la máquina falló")

    if tablero_1.quedan_barcos() ==False:
        print("HAS PERDIDO. La máquina ganó")
            
    else:
        print("HAS GANADO. La máquina pierde")    
            
            

