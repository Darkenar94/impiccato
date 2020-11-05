
import random
from giocoLib import *
from impostazioni import *

vittoria = "\nhai vinto!"
avvertimento = "attenzione: lettera utilizzata / carattere non consentito"

impostazioni = Impostazioni()
controlla_punteggio(impostazioni.punteggio, impostazioni.caratteri_errati, impostazioni.stringa, impostazioni.parola)

while True:
    carattere = input("\nlettera: ")
    carattere = carattere.lower()
    if ha_vinto(carattere, impostazioni.parola):
        print(vittoria)
        if continua():
            impostazioni.parola = random.choice(impostazioni.parole)
            impostazioni.stringa = impostazioni.parola[0] + "_" *len(impostazioni.parola[1:-1]) + impostazioni.parola[-1]
            impostazioni.caratteri = list(impostazioni.simboli)
            impostazioni.posizioni = []
            impostazioni.caratteri_errati = []
            impostazioni.punteggio = 6
            controlla_punteggio(impostazioni.punteggio, impostazioni.caratteri_errati, impostazioni.stringa, impostazioni.parola)
        else:
            break
    elif len(carattere) > 1 or len(carattere) < 1:
        gestisci_lunghezza(carattere, avvertimento)
    elif presente(carattere, impostazioni.parola):
        if not presente(carattere, impostazioni.caratteri):
            impostazioni.caratteri.append(carattere)
            impostazioni.posizioni = ottieni_posizioni(impostazioni.parola, carattere, impostazioni.posizioni)
            impostazioni.stringa = ottieni_stringa(impostazioni.posizioni, impostazioni.parola, impostazioni.punteggio, impostazioni.caratteri_errati)
            if ha_vinto(impostazioni.stringa, impostazioni.parola):
                print(vittoria)
                if continua():
                    impostazioni.parola = random.choice(impostazioni.parole)
                    impostazioni.stringa = impostazioni.parola[0] + "_" *len(impostazioni.parola[1:-1]) + impostazioni.parola[-1]
                    impostazioni.caratteri = list(impostazioni.simboli)
                    impostazioni.posizioni = []
                    impostazioni.caratteri_errati = []
                    impostazioni.punteggio = 6
                    controlla_punteggio(impostazioni.punteggio, impostazioni.caratteri_errati, impostazioni.stringa, impostazioni.parola)
                else:
                    break
        else:
            print(avvertimento)
    else:
        if not presente(carattere, impostazioni.caratteri_errati) and carattere not in impostazioni.simboli:
            impostazioni.caratteri_errati.append(carattere)
            impostazioni.punteggio -= 1
            if controlla_punteggio(impostazioni.punteggio, impostazioni.caratteri_errati, impostazioni.stringa, impostazioni.parola):
                break
        else:
            print(avvertimento)
