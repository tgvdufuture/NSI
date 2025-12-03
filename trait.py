import turtle

def trait(x1,y1,x2,y2):
    '''
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    Cette function dessine un trait entre les 2 points transmis en paramètres
    '''
    X1 = x1
    X2 = x2
    Y1 = y1 
    Y2 = y2
    
    turtle.penup()
    turtle.goto(X1,Y1)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.goto(X2,Y2)
    turtle.penup()
    pass

if __name__ == '__main__':
    trait(0,0,100,100)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
