'''
Challenge:
Draw a pattern that will change each time the
program is run. Use the random function to pick
the number of lines, the length of each line and
the angle of each turn.
'''

import random
import turtle
line = random.randint(30,1000)
for i in (0,line):
    lenght = random.randint(30,200)
    angle = random.randint(45,360)
    turtle.forward(lenght)
    turtle.right(angle)
turtle.hideturtle()
turtle.exitonclick()

