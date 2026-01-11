import turtle
board = turtle.Screen()
board.bgcolor("black")
board.title("Turtle")
turtle_instance = turtle.Turtle()
turtle_instance.color("white")
turtle_instance.shape("turtle")
turtle_instance.speed(0)

'''
turtle_instance.circle(50)
turtle_instance.circle(-50)
turtle_instance.forward(200)
'''

for i in range(30):
    turtle_instance.circle(40)
    turtle_instance.left(12)

turtle_instance.hideturtle()
turtle.done()
