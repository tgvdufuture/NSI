import turtle
from rectangle import rectangle
from trait import trait

def fenetre_balcon(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    # porte-fenetre
    rectangle(x,y,30,50)


    # balcon
    trait(x,y,x+50,y)
    trait(x+50,y,x+50,y-30)
    trait(x+50,y-30,x-30,y-30)
    trait(x-30,y-30,x-30,y)
    trait(x-30,y,x,y)



if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()