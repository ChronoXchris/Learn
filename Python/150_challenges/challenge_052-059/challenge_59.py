'''
Challenge:
Display five colours and ask the user to pick one. If they
pick the same as the program has chosen, say “Well
done”, otherwise display a witty answer which involves
the correct colour, e.g. “I bet you are GREEN with envy”
or “You are probably feeling BLUE right now”. Ask
them to guess again; if they have still not got it right,
keep giving them the same clue and ask the user to
enter a colour until they guess it correctly.
'''

import random
colour = random.choice(["red","black","green","blue","white"])
again = True

while again == True:
    user = input("Pick a coulor betwen rec, blue, green, white, black")
    user = user.lower()
    if colour == user:
        print("Well done")
        again = False
    else:
        if colour == "red":
            print("its like blood")
        if colour == "black":
            print("its like the night")
        if colour == "green":
            print("ist like a tree")
        if colour == "blue":
            print("its like the ocean")
        if colour == "white":
            print("You war white es paper")