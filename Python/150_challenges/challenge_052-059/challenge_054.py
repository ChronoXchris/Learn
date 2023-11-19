'''
Challenge:
Randomly choose either heads or tails (“h” or “t”). Ask
the user to make their choice. If their choice is the same
as the randomly selected value, display the message
“You win”, otherwise display “Bad luck”. At the end, tell
the user if the computer selected heads or tails.
'''

import random
com = random.choice(["h","t"])
player = input("Select heads or tails (h/t): ")
if com == player:
    print("You win!")
    print("The computer got:", com)
else:
    print("You lose :(")
    print(com)
