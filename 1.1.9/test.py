from turtle import *
import turtle as trtl

painter = trtl.Turtle()

painter.goto(90, 0)
painter.right(180)
painter.speed(1)
painter.forward(900)

def superCoolName():
    if painter.xcor() <= -90 and painter.xcor() >= -180:
         painter.pencolor("green")
    else:
        painter.pencolor("red")

one = 1

while one == 1:
    superCoolName

if painter.xcor() <= -90:
    listen()
    onkey(superCoolName, 'Up')



wn = trtl.Screen()
wn.mainloop()