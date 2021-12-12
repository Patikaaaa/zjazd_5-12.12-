import turtle

# Polecenie: uzupełnij komentarze z wyjaśnieniem instrukcji wykonywanych w kolejnych linijkach kodu

# włącz ekran i zapisz go do zmiennej np. wn
wn = turtle.Screen()
#
elfik=turtle.Turtle()
#
elfik.color('black', 'yellow')
#
elfik.penup()
#
elfik.setposition(117, 198)
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
#
wn.exitonclick()

