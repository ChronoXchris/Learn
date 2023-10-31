##########################################
#   Datne aus einer Datei auslesen 6.2   #
##########################################
fobj = open('woerterbuch.txt', 'r')

fobj.close

# Zeilenweise auslesen

fobj = open("woerterbuch.txt," "r")
for line in fobj:
   print(line)
fobj.close()
###############################################
woerter = {}

fobj = open("woerterbuch.txt", "r")
for line in fobj:
    zuordnung = line.split(" ")
    woerter[zuordnung[0]] = zuordnung[1]
fobj.close()
##################################################
woerter = {}

fobj = open("woerterbuch.txt", "r")
for line in fobj:
    line = line.strip()
    zuordnung = line.split(" ")
    woerter[zuordnung[0]] = zuordnung[1]
fobj.close()
#####################################################
woerter = {}
fobj = open("woerterbuch.txt", "r")
for line in fobj: 
    line = line.strip()
    zuordnung = line.split(" ")
    woerter[zuordnung[0]] = zuordnung[1] 
fobj.close()
while True: 
    wort = input("Geben Sie ein Wort ein: ")
    if wort in woerter: 
        print("Das deutsche Wort lautet:", woerter[wort]) 
    else: 
        print("Das Wort ist unbekannt")
    


