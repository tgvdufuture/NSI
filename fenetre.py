<<<<<<< HEAD
import turtle
=======
>>>>>>> 04debde73e3d8bd82d5af1b628994c3902543837
from rectangle import rectangle
import turtle

def fenetre(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''
<<<<<<< HEAD
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.pensize(1)
    rectangle(x,y+17,30,30)
    turtle.end_fill()
=======
    pass
>>>>>>> 04debde73e3d8bd82d5af1b628994c3902543837

if __name__ == '__main__':
    fenetre(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()