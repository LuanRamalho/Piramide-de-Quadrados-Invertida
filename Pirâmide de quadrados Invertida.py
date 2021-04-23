import turtle

a = turtle.Screen()
turtle.speed(0)

def quadrado(posx, posy, lado):
    turtle.showturtle()
    # posiciona
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    # desenha

    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
        turtle.hideturtle()

# Invertida
def pir_invertida(n,posx, posy,lado):
    for i in range(1,n+1):
        # desenha linha
        # --- posiciona
        turtle.penup()
        turtle.goto(posx+ (n-i)*lado/2,posy-(n-i)*lado)
        turtle.pendown()

        # --- desenha
        for j in range(1,i+1):
            quadrado(turtle.xcor(),turtle.ycor(), lado)
            turtle.setx(turtle.xcor()+lado)
            turtle.hideturtle()

quadrado(-150, 250, 50)
pir_invertida(12,-150,250,50)

a.exitonclick()