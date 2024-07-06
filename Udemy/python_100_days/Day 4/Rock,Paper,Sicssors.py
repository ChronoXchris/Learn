'''
Rock Paper Scissors Game
'''
import random

number = random.randint(0,2)

pnumber = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if pnumber == "0":
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif pnumber == "1":
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("Computer chose:",number)

if number == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif number == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
#----------------------------------------------------------
if pnumber == "0" and number == 0:
    print("Its a draw")
elif pnumber == "0" and number == 1:
    print("You lose")
elif pnumber == "0" and number == 2:
    print("You win!")
#----------------------------------------------------------
if pnumber == "1" and number == 1:
    print("Its a draw")
elif pnumber == "1" and number == 2:
    print("You lose")
elif pnumber == "1" and number == 0:
    print("You win!")
#----------------------------------------------------------
if pnumber == "2" and number == 2:
    print("Its a draw")
elif pnumber == "2" and number == 0:
    print("You lose")
elif pnumber == "2" and number == 1:
    print("You win!")