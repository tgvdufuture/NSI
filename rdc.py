from facade import facade
from random import shuffle
from porte import porte
from fenetre import fenetre
import turtle

def rdc(x, y_sol, c_facade, c_porte):
    '''
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
<<<<<<< HEAD
    '''
    # Dessine la facade
    facade(x, y_sol, c_facade, 1)

    elements = ["porte", "fenetre", "fenetre"]
    shuffle(elements)

    intervalle = 50  
    decalage = -10    

    x_actuel = x - (2 * intervalle) - decalage

    for element in elements:
        x_actuel = x_actuel + intervalle

        if element == "porte":
            porte(x_actuel, y_sol, c_porte)
        else:
            fenetre(x_actuel, y_sol)

if __name__ == '__main__':
    turtle.colormode(255)
    rdc(0, 0, (0, 0, 255), "green")
=======
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''
    # Dessine la facade
    pass

    # Construit les 3 éléments (1 porte et 2 fenetres)

    pass

if __name__ == '__main__':
    rdc(0,0,"red","green")
    # On ferme la fenêtre s'il y a un clique gauche
>>>>>>> 04debde73e3d8bd82d5af1b628994c3902543837
    turtle.exitonclick()