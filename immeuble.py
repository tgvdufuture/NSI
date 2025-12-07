# module immeuble

import turtle
from couleur_aleatoire import couleur_aleatoire
from random import randint
from rdc import rdc
from etage import etage
from toit import toit
import turtle

def immeuble(x, y_sol):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard
    '''
    # Nombre d'étage (aléatoire)

    nombre_etage = randint(0,4)

    #Couleurs des éléments (aléatoire)

    couleur_facade = couleur_aleatoire()
    couleur_porte = couleur_aleatoire()

    # Dessin du RDC

    rdc(x, y_sol, couleur_facade, couleur_porte)

    # Dessin des étages
    
    y_courant = y_sol + 50
    for i in range(nombre_etage):
        etage(x, y_courant, couleur_facade, i+1)
        y_courant += 50

    # Dessin du toit
    toit(x+25, y_courant, nombre_etage)


if __name__ == '__main__':
    turtle.colormode(255)
    immeuble(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()