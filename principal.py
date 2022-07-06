import random
import numpy as np

from clases import Tablero
from funciones import jugar
from variables import *

#tablero_1 = Tablero("jugador",jbarcos)

#tablero_2 = Tablero("máquina", mbarcos)

tablero_1 = Tablero("jugador")
tablero_2 = Tablero("máquina")

jugar(tablero_1, tablero_2)