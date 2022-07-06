
import random
import numpy as np


class Tablero:
    
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
        
        
    #def crear_tablero(self, fill_value=" "):
     #   return  np.full(self.dim, fill_value)
    
    def colocar_barco(self,tablero, barco):
        for elem in barco:
           # print("Colocando barco en posicion", elem)
            tablero[elem] = "O"
            #print (elem)
        
    def poner_barcos(self,barcos):
        for barco in barcos:
            self.colocar_barco(self.mar, barco)
        
    def imprimir_mapa(self):
        print("tablero de: ", self.idjug)
        for i in self.mar:
            print(i)   
    
    def imprimir_mapa_sin_disparos(self):
        print("tablero de: ", self.idjug)
        for i in self.marsinbarcos:
            print(i)    
            
        
        
    def disparo(self, coordenada):
        
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
    
    def quedan_barcos(self,):
        return "O" in self.mar
    
    def esloras(self):
        """
        con este método damos la eslora para que la funcion barco_aleatorio coloque los barcos
        """
        esloras = [1,1,1,1,2,2,2,3,3,4]
        for e in esloras:
            self.barco_aleatorio(e)
        
    
    def barco_aleatorio(self,eslora):
        """"
        en el primer while los barcos se construyen según la eslora,
        el segundo while se encarga de que se cumplan las condiciones para que no se salga del tablero
        ni se monte un barco sobre otros
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