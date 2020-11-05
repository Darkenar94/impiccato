
import random
from giocoLib import *

class Impostazioni:
    def __init__(self):
        self.testo = ottieni_testo()
        self.lista = ottieni_lista(self.testo)
        self.parole = ottieni_parole(self.lista)
        self.parola = random.choice(self.parole)
        self.stringa = self.parola[0] + "_" *len(self.parola[1:-1]) + self.parola[-1]
        self.simboli = " \"'!|<>,;.:_-+*}]#ç¸@§˘?^~`=)(/&%$£1234567890"
        self.caratteri = list(self.simboli)
        self.posizioni = []
        self.caratteri_errati = []
        self.punteggio = 6
