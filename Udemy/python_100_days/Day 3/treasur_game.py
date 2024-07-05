'''
Today we will programm a mini game with many different elemts an choices to make so you can make many wrong or right choices
'''

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island. Your mission is to find the treasure")
LorR = input("You can go left or right where do you wanne go? : ")
if LorR == "left": 
    WoreS = input("You came to a beach you can go swim or wait for a boat: ")
else:
    print("You gone the wrong way and got lost")
if WoreS == "wait":
    wichD = input("Right before you there are 3 doors: Blue, Yellow and Red.\n Wich door do you choose? : ")
else:
    print("You drowned while swimming beacouse you danot have any stamina")

if wichD == "Yellow":
    print("You won and found the treasure!")
elif wichD == "Red":
    print("The door was fieled with fier")
else:
    print("The Blue door was full with water and you drowned")
