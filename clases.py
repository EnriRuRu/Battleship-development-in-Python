
import random
import numpy as np


class Tablero:
    """
    en esta clase cro el tablero, realmente creo dos por cada jugador, uno en el que se colocarán los barcos 
    y el otro permanecerá vacío.
    Hay dos constructores, el segundo sobreesceribe al primero. El primero lo hice cuando coloqué los barcos de 
    manera arbitraria, en el segundo los barcos se colocan de manera aleatoria, tanto en el tablero del computador como en
    el del jugador
    """
    def __init__(self, idjug, barcos, dim =(10,10)):
        
        self.dim=dim
        self.marsinbarcos=np.full(self.dim, " ")
        self.mar=np.full(self.dim, " ")
        self.idjug = idjug
        self.poner_barcos(barcos)
        
    def __init__(self, idjug, dim =(10,10)):
    
        self.dim=dim
        self.marsinbarcos=np.full(self.dim, " ")
        self.mar=np.full(self.dim, " ")
        self.idjug = idjug
        self.esloras()
        
        
    
    def colocar_barco(self,tablero, barco):
        """
        Aquí se colocan las posiciones de cada barco en el caso de las posiciones arbitrarias 
        prebiamente asignadas. NO SE UTILIZA ESTE MËTODO PARA LOS BARCOS ALEATORIOS
        """
        for elem in barco:
            tablero[elem] = "O"
        
        
        
    def poner_barcos(self,barcos):
        
        """"
        Aquí se ponen todos los barcos de la lista barcos. 
        NO NO SE UTILIZA ESTE MËTODO PARA LOS BARCOS ALEATORIOS
        """
        for barco in barcos:
            self.colocar_barco(self.mar, barco)
        
        
        
    def imprimir_mapa(self):
        """"
        Se mostrará el tablero del jugador
        """
        print("tablero de: ", self.idjug)
        for i in self.mar:
            print(i)   
    
    
    def imprimir_mapa_sin_disparos(self):
        """"
        Se mostrará el tablero sin barcos del computador
        """
        print("tablero de: ", self.idjug)
        for i in self.marsinbarcos:
            print(i)    
            
        
        
    def disparo(self, coordenada):
        
        """"
        Función disparo
        """
        
        print("disparando a:", coordenada)
        acierto=True
        if self.mar[coordenada[0], coordenada[1]] == "O":
            print("Tocado")
            print("tira otra vez")
            self.mar[coordenada[0], coordenada[1]] = "X"
            self.marsinbarcos[coordenada[0], coordenada[1]] = "X"
        else:
            print("Agua")
            acierto = False
            self.mar[coordenada[0], coordenada[1]] = "-"
            self.marsinbarcos[coordenada[0], coordenada[1]] = "#"
        return acierto
    
    
    
    def quedan_barcos(self):
        
        """"
        con este metodo implementamos una condición, si se cumple es True. Que se utilizará 
        para saber cuando termina el juego
        """
        return "O" in self.mar
    
    
    def esloras(self):
        """
        con este método damos la eslora de cada uno de los barcos  para que la funcion barco_aleatorio 
        coloque los barcos.
        """
        esloras = [1,1,1,1,2,2,2,3,3,4]
        for e in esloras:
            self.barco_aleatorio(e)
        
    
    def barco_aleatorio(self,eslora):
        """"
        Aquí se colocan los barcos de manera aleatoria
        el segundo while se encarga de que se cumplan las condiciones para que no se salga del tablero
        ni se monte un barco sobre otros, hace la comprobación de que se pueden colocar
        el último for finalmente pone los barcos el el tablero.
        """
        cabe=False
        while cabe ==False:
            fila = np.random.randint(9)
            columna = np.random.randint(9)
            orien = np.random.choice(["Norte", "Sur", "Este", "Oeste"])
            fila_o = fila
            columna_o= columna
            
            i=0
            while fila>=0 and fila <10 and columna >=0 and columna < 10 and self.mar[fila,columna] == " " and i < eslora:
                if orien == "Norte":
                    fila = fila -1
                if orien == "Sur":
                    fila = fila + 1
                if orien == "Este":
                    columna = columna + 1
                if orien == "Oeste":
                    columna = columna - 1
                i = i + 1
            if i == eslora:
                cabe=True
                
        fila=fila_o
        columna= columna_o
            
        for i in range(eslora):
            
            self.mar[fila,columna] = "O"
            
            if orien == "Norte":
                fila = fila -1
            if orien == "Sur":
                fila = fila + 1
            if orien == "Este":
                columna = columna + 1
            if orien == "Oeste":
                columna = columna - 1