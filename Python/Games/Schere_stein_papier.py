import random
#scores
player = 0
computer = 0
while player or computer < 3:
    stp = random.randint(1,3)
    eingabe = int(input('Bitte gebe 1, 2 oder 3 ein. (1=Schere 2= Stein 3=Papier) : '))

    if eingabe == 1:
     print('Du hast Schere genommen')
    elif eingabe == 2:
     print('Du hast Stein genommen')
    else:
     print('Du hast Papier genommen')
#
    
    if stp == 1:
     print('Der Computer hat Schere genommen')
    elif stp == 2:
     print('Der Computer hat Stein genommen')
    elif stp == 3:
     print('Der Computer hat Papier genommen')
################################################################################
    if eingabe == 2 and stp == 1: 
     print('Du hast gewonnen')
     player = player +1 # player += 1
    elif eingabe == 3 and stp == 1:
     print('Der Computer hat gewonnen')
     computer = computer +1
##################################################################################
    if eingabe == 1 and stp == 2:
     print('Der computer hat gewonnen')
     computer = computer +1
    elif eingabe == 3 and stp == 2:
     print('Du gewinnst')
     player = player +1
####################################################################################
    if eingabe == 1 and stp == 3:
     print('Du gewinnst')
     player = player +1
    elif eingabe == 2 and stp == 3:
     print('Der computer gweinnt')
     computer = computer +1
    
    if eingabe == stp:
     print("Unentschieden")
    
    print('Dein Score ist', player)
    print('Der Score com Computer ist', computer)

    if player == 3: # versuch mal hier mit 'else' zu definieren
     print('Du hast Gewonnen!')
     break
    elif computer == 3:
     print('Der Computer hat Gewonnen!')
     break



