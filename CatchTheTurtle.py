import turtle
from random import randint
import time


timeLeft = 10
penTime = turtle.Turtle()
penTime.penup()
penTime.hideturtle()
penTime.goto(0,270)
penTime.write(f"Time : 10", align="center", font=("Courier", 24, "bold"))


scoreN = 0
penScore = turtle.Turtle()
penScore.penup()
penScore.hideturtle()
penScore.goto(0,300)
penScore.write(f"Score : 0", align="center", font=("Courier", 24, "bold"))

board = turtle.Screen()
board.bgcolor("lightblue")
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("black")
turtle_instance.penup()
turtle_instance.shapesize(2,2,2)


while timeLeft > 0:
    position_X = randint(-300,300)
    position_Y = randint(-300,300)

    turtle_instance.hideturtle()
    turtle_instance.goto(position_X, position_Y)
    turtle_instance.showturtle()

    def score(x,y):
        penScore.clear()
        global scoreN
        scoreN += 1
        penScore.write(f"Score : {scoreN}", align="center", font=("Courier", 24, "bold"))
        turtle_instance.hideturtle()

    turtle_instance.onclick(score,1)

    time.sleep(0.8)
    timeLeft -= 1
    penTime.clear()
    penTime.write(f"Time : {timeLeft}", align="center", font=("Courier", 24, "bold"))
    penScore.clear()
    penScore.write(f"Score : {scoreN}", align="center", font=("Courier", 24, "bold"))

penScore.clear()
penScore.goto(0,0)
penScore.write(f"Game Over! Your Score is {scoreN}", align="center", font=("Courier", 24, "bold"))

turtle.mainloop()

