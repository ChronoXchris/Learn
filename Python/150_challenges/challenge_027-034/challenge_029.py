'''
Challenge:
Ask the user to enter an integer that is over 500. Work
out the square root of that number and display it to two decimal places.
'''
import math
num = int(input("PLease enter a number that is over 500: "))
num1 = math.sqrt(num)

print(round(num1,2))