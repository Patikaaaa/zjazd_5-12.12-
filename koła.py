import turtle

t = turtle.Turtle()
screen = turtle.Screen()

def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# narysuj kilka okręgów
draw_circle("blue",90,0,0)
y=0
draw_circle("pink",30,0,y-60)

screen.exitonclick()
