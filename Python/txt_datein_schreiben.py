# In datein etwas schreiben und abspeichern
datei = open('Text.txt','w')

print(datei.write(input('Schriebe was in deine Datei und mit Enter abspeichern', )))

datei.close()