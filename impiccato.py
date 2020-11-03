
import random
from giocoLib import *

testo = ottieni_testo()
lista = ottieni_lista(testo)
parole = ottieni_parole(lista)

vittoria = "\nhai vinto!"
avvertimento = "attenzione: lettera utilizzata / carattere non consentito"
parola = random.choice(parole)
stringa = parola[0] + "_" *len(parola[1:-1]) + parola[-1]

simboli = " \"'!|<>,;.:_-+*}]#ç¸@§˘?^~`=)(/&%$£1234567890"
caratteri = list(simboli)
posizioni = []
caratteri_errati = []

punteggio = 6

controlla_punteggio(punteggio, caratteri_errati, stringa, parola)

while True:
    print("")
    carattere = input("lettera: ")
    carattere = carattere.lower()
    if ha_vinto(carattere, parola):
        print(vittoria)
        if continua():
            (parola, stringa, caratteri, posizioni, caratteri_errati, punteggio) = resetta(parole, simboli)
        else:
            break
    elif len(carattere) > 1 or len(carattere) < 1:
        gestisci_lunghezza(carattere, avvertimento)
    elif presente(carattere, parola):
        if not presente(carattere, caratteri):
            caratteri.append(carattere)
            posizioni = ottieni_posizioni(parola, carattere, posizioni)
            stringa = ottieni_stringa(posizioni, parola, punteggio, caratteri_errati)
            if ha_vinto(stringa, parola):
                print(vittoria)
                if continua():
                    (parola, stringa, caratteri, posizioni, caratteri_errati, punteggio) = resetta(parole, simboli)
                else:
                    break
        else:
            print(avvertimento)
    else:
        if not presente(carattere, caratteri_errati) and carattere not in simboli:
            caratteri_errati.append(carattere)
            punteggio -= 1
            if controlla_punteggio(punteggio, caratteri_errati, stringa, parola):
                break
        else:
            print(avvertimento)
