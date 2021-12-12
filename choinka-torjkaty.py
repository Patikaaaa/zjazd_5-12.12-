import turtle

wn = turtle.Screen()
tofik = turtle.Turtle()


def rysujtrojkaty(x, y, size, bgcolor):
    tofik.penup()
    tofik.setposition(x, y)
    tofik.fillcolor(bgcolor)
    tofik.begin_fill()
    tofik.pendown()
    tofik.goto(x + size, y)
    tofik.goto(x, y + size)
    tofik.goto(x - size, y)
    tofik.goto(x, y)
    tofik.end_fill()


def rysujchoinke(x, y, size, step, count):
    for part in range(count):
        rysujtrojkaty(x, y, size, "green")
        y = y - 2*step
        size = size + step


rysujchoinke(0, 0, 40, 20, 8)

wn.exitonclick()
