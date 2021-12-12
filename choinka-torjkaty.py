import turtle

wn = turtle.Screen()
tofik = turtle.Turtle()


def rysujtrojkaty(x, y, rozmair, bgcolor):
    tofik.penup()
    tofik.setposition(x, y)
    tofik.fillcolor(bgcolor)
    tofik.begin_fill()
    tofik.pendown()
    tofik.goto(x + rozmair, y)
    tofik.goto(x, y + rozmair)
    tofik.goto(x - rozmair, y)
    tofik.goto(x, y)
    tofik.end_fill()


def rysujchoinke(x, y, rozmiar, krok, ilosc):
    for part in range(ilosc):
        rysujtrojkaty(x, y, rozmiar, "green")
        y = y - 2*krok
        rozmiar = rozmiar + krok


rysujchoinke(0, 0, 40, 20, 8)

wn.exitonclick()
