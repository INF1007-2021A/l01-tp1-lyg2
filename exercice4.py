import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    vitesseInitiale0 = (vitesseInitiale * 1000) / (60*60)
    vitesseFinale0 = (vitesseFinale * 1000) / (60 * 60)
    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"
    positionFinale = ((vitesseInitiale0 + vitesseFinale0) * duree)/2 + positionInitiale

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print('La position finale sera : ' + str(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale)) + '.')
