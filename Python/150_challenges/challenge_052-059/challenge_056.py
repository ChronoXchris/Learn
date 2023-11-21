'''
Challenge:
Randomly pick a whole number between 1
and 10. Ask the user to enter a number and
keep entering numbers until they enter the
number that was randomly picked.
'''

import random

number = random.randint(1,10)
user = int(input("Guess a number betwen 1 and 10: "))
while number != user:
    user = int(input("Try again!: "))
    if user == number:
        print("You did it!")
print("The number was", number)
