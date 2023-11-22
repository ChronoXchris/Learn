'''
Challenge:
Draw an octagon that uses a different colour (randomly
selected from a list of six possible colours) for each line.
'''

import turtle
import random
turtle.shape("turtle")


for i in range(0,6):
    colour = random.choice(["red", "blue", "black", "yellow", "green", "pink"])
    turtle.color(colour)
    turtle.forward(100)
    turtle.left(60)
turtle.exitonclick()
