
import time
import random

def stampa(stringa):
    print("    ", end="")
    for lettera in stringa:
        print(lettera + " ", end="")
    print("\n")

def disegna_impiccato(testa, b_sx, b_dx, torso, g_sx, g_dx, c_1, c_2, c_3, c_4, c_5, c_6, stringa):
    print("\n"*20)#100
    print("""
  +------+
  |      |
  |      {}
  |     {}{}{}
  |     {} {}
  |           {} {} {} {} {} {}
  |           - - - - - -
-----
  """.format(testa, b_sx, torso, b_dx, g_sx, g_dx, c_1, c_2, c_3, c_4, c_5, c_6))
    stampa(stringa)

def controlla_stato(punteggio, caratteri_errati, stringa, parola):
    if punteggio == 0:
        disegna_impiccato("O", "/", "\\", "|", "/", "\\",   caratteri_errati[0].upper(), caratteri_errati[1].upper(), caratteri_errati[2].upper(), caratteri_errati[3].upper(), caratteri_errati[4].upper(), caratteri_errati[5].upper(), stringa)
        print("la parola era {} hai perso!\n".format(parola.upper()))
        time.sleep(3)
        return True
    elif punteggio == 6:
        disegna_impiccato("", "", "", "", "", "", "", "", "", "", "", "", stringa)
    elif punteggio == 5:
        disegna_impiccato("O", "", "", "", "", "", caratteri_errati[0].upper(), "", "", "", "", "", stringa)
    elif punteggio == 4:
        disegna_impiccato("O", "/", "", "", "", "", caratteri_errati[0].upper(), caratteri_errati[1].upper(), "", "", "", "", stringa)
    elif punteggio == 3:
        disegna_impiccato("O", "/", "\\", " ", "", "", caratteri_errati[0].upper(), caratteri_errati[1].upper(), caratteri_errati[2].upper(), "", "", "", stringa)
    elif punteggio == 2:
        disegna_impiccato("O", "/", "\\", "|", "", "",  caratteri_errati[0].upper(), caratteri_errati[1].upper(), caratteri_errati[2].upper(), caratteri_errati[3].upper(), "", "", stringa)
    elif punteggio == 1:
        disegna_impiccato("O", "/", "\\", "|", "/", "", caratteri_errati[0].upper(), caratteri_errati[1].upper(), caratteri_errati[2].upper(), caratteri_errati[3].upper(), caratteri_errati[4].upper(), "", stringa)

def ottieni_testo():
    file = open("/home/darkenar94/Scrivania/impiccato/999_parole.txt", "r")
    testo = file.read()
    file.close()
    return testo

def ottieni_lista(testo):
    sep = "\n"
    return testo.split(sep)

def ottieni_parole(lista):
    return [parola for parola in lista if len(parola) > 2]

def presente(x, contenitore):
    if x in contenitore:
        return True
    return False

def ottieni_parola(lettere):
    stringa = ""
    for lettera in lettere:
        stringa += lettera
    return stringa

def ottieni_lettere(parola, posizioni):
    posizioni = sorted(posizioni)
    lettere = list(parola[0] + "_"* (len(parola)-2) + parola[-1])
    for n in posizioni:
        lettere[n] = parola[n]
    return lettere

def ottieni_stringa(posizioni, parola, punteggio, caratteri_errati):
    lettere = ottieni_lettere(parola, posizioni)
    stringa = ottieni_parola(lettere)
    controlla_stato(punteggio, caratteri_errati, stringa, parola)
    return stringa

def ottieni_posizioni(parola, carattere, posizioni):
    contatore = 0
    for lettera in parola[1:-1]:
        contatore += 1
        if lettera == carattere:
            posizioni.append(contatore)
    return posizioni

def gestisci_lunghezza(carattere, avvertimento):
    if len(carattere) > 1:
        print("decisione errata")
    else:
        print(avvertimento)

def ha_vinto(stringa, parola):
    if stringa == parola:
        return True
    return False

def continua():
    scelta = input("\ncontinuare? S/n: ")
    if scelta.lower() == "s":
        return True
    elif scelta.lower() == "n":
        print("Bye, bye! =)")
        return False
    return continua()
