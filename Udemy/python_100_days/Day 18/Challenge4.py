
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.speed("fastest")
tim.pensize(15)
direction = [0, 90, 180, 270]


for number_n in range(200):
    tim.color(random_color())
    tim.forward(40)
    tim.right(random.choice(direction))
