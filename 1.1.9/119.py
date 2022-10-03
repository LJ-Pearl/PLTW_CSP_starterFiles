import turtle as trtl

painter = trtl.Turtle()





def again():
    global ag
    ag = input("would you like to draw another shape?")

colors = ["red", "blue", "green", "yellow", "purple", "black"]

def draw():
    locationX = input("Where would you like to draw? (x coordinate)")
    locationY = input("Where would you like to draw? (y coordinate)")
    painter.penup()
    painter.goto(int(locationX), int(locationY))
    painter.pendown()
    col = input("What color would you like to use?")
    if col in colors:
        painter.fillcolor(col)
        painter.begin_fill()
    sel = input("What would you like to draw?")
    if sel == "square":
        for i in range(4):
            painter.forward(160)
            painter.left(90)
    elif sel == "circle":
        painter.circle(80)
    painter.end_fill()

ag = "yes"

while ag == "yes":
    draw()
    again()

wn = trtl.Screen()
wn.mainloop()