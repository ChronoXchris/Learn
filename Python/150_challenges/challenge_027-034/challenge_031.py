'''
Challenge:
Ask the user to enter the radius of a circle
(measurement from the centre point to the edge). Work
out the area of the circle (π*radius2).
'''

import math
num = int(input("PLease enter a radius: "))
area = math.pi*(num**2)
print(area)