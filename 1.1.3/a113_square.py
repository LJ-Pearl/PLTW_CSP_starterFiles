 #   a113_square.py
#   Write code to draw a square.
import turtle as trtl

from turtle import *

painter = trtl.Turtle()

# Your code here
#for i in range(4):
 #   painter.right(90)
  #  painter.forward(100)

painter.speed(50)

def up():
    painter.setheading(90)
    painter.forward(10)

def down():
    painter.setheading(270)
    painter.forward(10)

def left():
    painter.setheading(180)
    painter.forward(10)

def right():
    painter.setheading(0)
    painter.forward(10)

listen()
onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')

wn = trtl.Screen()
wn.mainloop()
