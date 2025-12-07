import turtle
from rectangle import rectangle

def facade(x, y_sol, couleur, niveau):
    '''
    Paramètres :
        x : abcisse du centre de la façade
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    remarque :
        Facade dessine une facade sans les élements interieurs
    '''
<<<<<<< HEAD
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    rectangle(-50, y_sol, 150, niveau+50)
    turtle.end_fill()
=======
    rectangle(x, y_sol, couleur, niveau)
>>>>>>> 04debde73e3d8bd82d5af1b628994c3902543837

if __name__ == '__main__':
    facade(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
<<<<<<< HEAD
    turtle.exitonclick()

=======
    turtle.exitonclick()
>>>>>>> 04debde73e3d8bd82d5af1b628994c3902543837
