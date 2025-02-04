from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.title("Ping Pong")
screen.setup(width=1500, height=1000)


peddle_one = Turtle("square")
peddle_one.color("white")
peddle_one.penup()
peddle_one.goto(-700, 0)
peddle_one.shapesize(10, 0.5)

peddle_two = Turtle("square")
peddle_two.color("white")
peddle_two.penup()
peddle_two.goto(700, 0)
peddle_two.shapesize(10, 0.5)


def player1_up():
    y = peddle_one.ycor()
    peddle_one.sety(y + 20)

def player1_down():
    y = peddle_one.ycor()
    peddle_one.sety(y - 20)

def player2_up():
    y = peddle_two.ycor()
    peddle_two.sety(y + 20)

def player2_down():
    y = peddle_two.ycor()
    peddle_two.sety(y - 20)


screen.listen()
screen.onkey(player1_up, "w")
screen.onkey(player1_down, "s")
screen.onkey(player2_up, "Up")
screen.onkey(player2_down, "Down")

screen.exitonclick()

