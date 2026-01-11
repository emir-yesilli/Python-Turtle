import turtle

board = turtle.Screen()
board.bgcolor("black")
board.title("Turtle")
turtle_instance = turtle.Turtle()
turtle_instance.color("white")
turtle_instance.shape("turtle")

#     - E -
'''
turtle_instance.back(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.left(180)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(200)
turtle_instance.left(90)
turtle_instance.forward(100)
'''

#       - Star -
'''
for _ in range(5):
    turtle_instance.forward(100)
    turtle_instance.left(144)
'''

#      - Polygon -
'''
number_of_sides = int(input("Enter number of sides: "))
degrees = 360 / number_of_sides
for i in range(number_of_sides):
    turtle_instance.forward(100)
    turtle_instance.left(degrees)
'''


#       - Shrinking Square -
'''
x = 100
for i in range(4):
    for i in range(4):
        turtle_instance.forward(x)
        turtle_instance.left(90)

    turtle_instance.forward(x/2)
    x = x / 2 * (2**(1/2))
    turtle_instance.left(45)
'''

turtle_instance.hideturtle()
turtle.done()
