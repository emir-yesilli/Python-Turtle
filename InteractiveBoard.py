import turtle
board = turtle.Screen()
board.bgcolor("black")
board.title("Interactive Board")
turtle_instance = turtle.Turtle()
turtle_instance.color("white")
turtle_instance.speed(0)

turtle_instance.left(90)

def up():
    turtle_instance.setheading(90)
    turtle_instance.forward(5)

def down():
    turtle_instance.setheading(270)
    turtle_instance.forward(5)

def left():
    turtle_instance.setheading(180)
    turtle_instance.forward(5)

def right():
    turtle_instance.setheading(0)
    turtle_instance.forward(5)

def clear():
    turtle_instance.clear()

def position():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()

def penup():
    turtle_instance.penup()
def pendown():
    turtle_instance.pendown()

board.listen()
board.onkey(up, "Up")
board.onkey(down, "Down")
board.onkey(left, "Left")
board.onkey(right, "Right")
board.onkey(clear, "c")
board.onkey(position, "p")
board.onkeypress(penup, "space")
board.onkeyrelease(pendown, "space")

turtle.mainloop()