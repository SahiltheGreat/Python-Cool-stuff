import turtle
def chessgrid(x,y,width,c):
    turtle.penup()
    turtle.pencolor('black')
    turtle.fillcolor(c)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(40)
        turtle.left(90)
    turtle.end_fill()
for x in range(8):
    for y in range(8):
        a='black'
        b='white'
        if(((x+y)%2) == 0):
            chessgrid(40*x,40*y,40,a)
        else:
            chessgrid(40*x,40*y,40,b)
turtle.exitonclick()
