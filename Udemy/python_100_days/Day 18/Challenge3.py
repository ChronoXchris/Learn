import turtle as t
import random


tim = t.Turtle()
colors = [
    "red", "blue", "green", "yellow", "purple", "orange", "pink", "brown",
    "black", "white", "gray", "cyan", "magenta", "lime"
]



def number(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for number_n in range(3, 11):
    tim.color(random.choice(colors))
    number(number_n)
