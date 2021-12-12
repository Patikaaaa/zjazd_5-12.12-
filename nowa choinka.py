import turtle

# Polecenie: napisz instrukcje potrzebne do narysowania choinki.

# włącz ekran i zapisz go do zmiennej np. wn
wn = turtle.Screen()
# ustaw tło jako "dark blue"
tofik=turtle.Turtle()
tofik.color('black', 'dark blue')

# stwórz zółwia i ustaw go do zmiennej tofik

# ustaw kształt jako "żółw" (anf. turtle)

#podnieś pisak
tofik.penup()
# idź do punktu (0,0_
tofik.setposition(0,0)

tofik.color('green')
# ustaw kolor pisaka na zielony (ang. green)

# rozpocznik wypełnianie (komenda begin_fill)
tofik.begin_fill()
# ustaw kolor wypełnienie jako zielony
tofik.color("green")

# ustaw rozmiar pisaka jako 8
tofik.pensize(8)
# przyciśnij (przyłóż) pisak
tofik.pendown()
# idź do punktu (100,0)
tofik.goto(100,0)
# podnieś pisak
tofik.penup()
# zakończ wypełnienie
tofik.end_fill()
# idź do punktu (100.0)
tofik.goto(100,0)
# przyciśnij (przyłóż) pisak
tofik.pendown()
# rozpocznij wypełnianie
tofik.begin_fill()
# ustaw kolor wypełnienie jako zielony
tofik.fillcolor("green")
# idź do punktu (0,75)
tofik.goto(0,75)

# idź do punktu (-100,0)
tofik.goto(-100,0)
# idź prosto 100 jednostek
tofik.forward(100)
# idź do punktu (125,65)

# idź do punktu (-125,65)

# idź do punktu (0,0)
tofik.goto(0,0)
# podnieś pisak
tofik.penup()
# zakończ wypełnienie
tofik.end_fill()
# idź do punktu (0,75)
tofik.goto(0,75)
# przyciśnij (przyłóż) pisak
tofik.pendown()
# rozpocznij wypełnianie
tofik.begin_fill()
# ustaw kolor wypełnienie jako zielony
tofik.color("green")
# idź do punktu (50,75)
tofik.goto(50,75)
# idź do punktu (0,120)
tofik.goto(0,120)
# idź do punktu (-50,75)
tofik.goto(-50,75)
# idź do punktu (0,75)
tofik.goto(0,75)









# podnieś pisak
tofik.penup()
# zakończ wypełnienie
tofik.end_fill()
# idź do punktu (0,-90)
tofik.goto(0,-90)
# przyciśnij (przyłóż) pisak
tofik.pendown()
# ustal kolor jak brązowy (ang brown)
tofik.color("brown")
# rozpocznij wypełnianie
tofik.begin_fill()
# ustal kolor wypełnienia jako brązowy
tofik.fillcolor("brown")
# idź do punktu (20,-90)
tofik.goto(20,-90)

# skręć w lewo o 90 stopni
tofik.left(90)

# idź prosto 20 jednostek
tofik.forward(20)
# skręć w lewo o 90 stopni
tofik.left(90)
# idź prosto 40 jednostek
tofik.forward(40)
# skręć w lewo o 90 stopni
tofik.left(90)
# idź prosto 20 jednostek
tofik.forward(20)
# skręć w lewo o 90 stopni
tofik.left(90)
# idź prosto 20 jednostek
tofik.forward(20)
# podnieś pisak
tofik.penup()
# zakończ wypełnienie
tofik.end_fill()
# czekaj na koniec pokliknięciu
wn.exitonclick()
