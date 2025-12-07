from facade import facade
from random import shuffle, randint
from fenetre import fenetre
from fenetre_balcon import fenetre_balcon
import turtle

def etage(x, y_sol, couleur, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    '''
    # dessin des murs
    facade(x, y_sol, couleur, niveau)

    elements = []
    for i in range(3):
        if randint(0, 1) == 0:
            elements.append("fenetre")
        else:
            elements.append("balcon")

    intervalle = 50
    decalage = 8  

    x_actuel = x - (2 * intervalle) + decalage

    for element in elements:
        x_actuel = x_actuel + intervalle
        
        if element == "balcon":
            fenetre_balcon(x_actuel, y_sol)
            turtle.pensize(1)
        else:
            fenetre(x_actuel, y_sol)
            

if __name__ == '__main__':
    turtle.colormode(255)
    etage(0, 0, "red", 1)
    turtle.exitonclick()