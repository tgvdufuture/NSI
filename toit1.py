import turtle
import turtle

def toit1(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''

    turtle.fillcolor("black")
    turtle.begin_fill()
    # Point gauche de la base
    turtle.penup()
    turtle.goto(x - 85, y_sol)
    turtle.pendown()
    # Point sommet du triangle
    turtle.goto(x, y_sol + 45)
    # Point droit de la base
    turtle.goto(x + 85, y_sol)
    # Retour au point de départ pour fermer le triangle
    turtle.goto(x - 85, y_sol)
    turtle.end_fill()
    turtle.penup()

if __name__ == '__main__':
    toit1(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()