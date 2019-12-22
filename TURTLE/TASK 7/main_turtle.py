import turtle

leonardo = turtle.Turtle()

def leonardoSetPosition(x,y):
    leonardo.up()
    leonardo.goto(x, y)
    leonardo.down()

leonardo.width(2)

# Стеклянная колба лампы - Начало
leonardo.fillcolor("#fcdb03")
leonardo.begin_fill()
leonardo.forward(130)
leonardo.circle(5, 90)
leonardo.forward(60)
leonardo.circle(-10, 60)
leonardo.circle(150, 300)
leonardo.circle(-10, 60)
leonardo.forward(60)
leonardo.circle(5, 90)
leonardo.end_fill()
# Стеклянная колба лампы - Конец

# Нить накаливания - Начало
leonardoSetPosition(20, 0)
leonardo.left(90)
leonardo.forward(70)
leonardo.circle(50, 30)
# Цикл создания витков нити
i = 0
while i < 3:
    leonardo.circle(-20, 255)
    leonardo.circle(-5, 100)
    i += 1
# Конец цискла
leonardo.circle(-20, 255)
leonardo.circle(50, 30)
leonardo.forward(70)
leonardoSetPosition(0, 0)
# Нить накаливания - Конец

# Цоколь лампы - Начало
leonardo.fillcolor("#6d6a6e")
leonardo.begin_fill()
leonardo.right(90)
leonardo.circle(7, 180)
leonardo.forward(130)
leonardo.circle(-7, 180)
leonardo.forward(130)
leonardo.circle(7, 180)
leonardo.forward(120)
leonardo.circle(-7, 180)

leonardo.forward(25)
leonardo.left(90)
leonardo.circle(-30, 180)
leonardo.right(90)
leonardo.forward(60)
leonardo.left(180)
leonardo.forward(85)

leonardo.circle(-7, 180)
leonardo.forward(120)
leonardo.circle(7, 180)
leonardo.forward(130)
leonardo.circle(-7, 180)
leonardo.forward(130)
leonardo.circle(7, 180)
leonardo.forward(130)
leonardo.end_fill()
# Цоколь лампы - Конец


turtle.done()