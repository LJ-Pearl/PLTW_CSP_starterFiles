#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)
legs = 6
leg_len = 70
z = 380 / legs
painter.pensize(5) 
n = 0
while (n < legs):
  painter.goto(0,0)
  painter.setheading(z*n)
  painter.forward(leg_len)
  n = n + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
