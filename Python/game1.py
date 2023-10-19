import random
ratezahl = random.randint(1,10)
Try = 0
aktiv = True

while Try < 3:
    print('Du bist beim', Try,'Versuch')
    Try = Try +1
    eingabe = int(input('Pleas type a number: '))
        
    if eingabe == ratezahl:
        print('You win')
        aktive = False
    elif eingabe > ratezahl:
        print('Deine geratene Zahl ist zu groß')
    else:
        print('Deine geratene Zahl ist zu klein')
    if Try == 3:
        print('Du hast verloren :(')
        print('Die Zahl war', ratezahl)
        aktiv = False   
        print('Spiel vorbei')