import turtle

wn = turtle.Screen()
# Polecenie: uzupełnij komentarze z wyjaśnieniem instrukcji wykonywanych w kolejnych linijkach kodu
def rysuj_gwiazdke(x,y, kolor, bgcolor):
    # włącz ekran i zapisz go do zmiennej np. wn
    #
    elfik=turtle.Turtle()
    #
    elfik.color(kolor, bgcolor)
    #
    elfik.penup()
    #
    elfik.setposition(x, y)
    #
    elfik.pendown()
    #
    elfik.begin_fill()
    #
    elfik.forward(25)
    #
    elfik.left(72)
    #
    elfik.forward(25)
    #
    for i in range(4):
        #
        elfik.right(144)
        #
        elfik.forward(25)
        #
        elfik.left(72)
        #
        elfik.forward(25)

    #
    elfik.end_fill()
    #
    elfik.penup()
rysuj_gwiazdke(50,50,"green","pink")
rysuj_gwiazdke(100,100,"yellow","gold")
rysuj_gwiazdke(150,150,"pink","red")



wn.exitonclick()
