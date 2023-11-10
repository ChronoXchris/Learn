'''
Challenge:
Ask for the radius and the depth of a cylinder
and work out the total volume (circle
area*depth) rounded to three decimal
places.
'''

import math
radius = int(input("Please enter the radius of the cylinder: "))
depth = int(input("PLease enter the depth of the cylinder: "))
area = math.pi*(radius**2)
volum = area*depth
print("The volum is", round(volum,3))