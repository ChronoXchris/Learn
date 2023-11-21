'''
Challenge:
Update program 056 so that it
tells the user if they are too high
or too low before they pick again.
'''

import random

number = random.randint(1,10)
user = int(input("Guess a number von 1 to 10: "))
while number != user:
    if user < number:
        print("Your number is to small")
        user = int(input("Try again!"))
    elif user > number:
        print("Your number is to big")
        user = int(input("Try again!"))
print("You win!")
print("The number was", number)