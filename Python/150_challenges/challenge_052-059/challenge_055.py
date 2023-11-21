'''
Challenge:
Randomly choose a number between 1 and 5. Ask the user to pick a
number. If they guess correctly, display the message “Well done”,
otherwise tell them if they are too high or too low and ask them to pick a
second number. If they guess correctly on their second guess, display
“Correct”, otherwise display “You lose”.
'''

import random
tries = 0
number = random.randint(1,5)

while tries != 2:
    user = int(input("Guess a number von 1 to 5: "))
    if user == number:
        print("You win!")
    elif user < number:
        print("Your number is to small")
        tries = tries + 1
    elif user > number:
        print("Your number is to big")
        tries = tries+1
print("You lose")
print("The number was", number)


