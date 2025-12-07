import turtle
from trait import trait

def toit2(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    '''
<<<<<<< HEAD
    turtle.pensize(8)
    trait(x-85, y_sol, x+81, y_sol)
    
=======
    turtle.pensize(10)
    if niveau == 0:
        trait(x-70, 60, x+70, 60)
        trait(x-70, 60, x+70, 60)
    else:
        trait(x-70, y_sol*niveau, x+70, y_sol*niveau)
    pass

>>>>>>> 04debde73e3d8bd82d5af1b628994c3902543837
if __name__ == '__main__':
    toit2(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()