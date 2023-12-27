'''
Challenge:
Using the Names.txt file you
created earlier, display the list of
names in Python. Ask the user to
type in one of the names and then
save all the names except the one
they entered into a new file called
Names2.txt.
'''

file = open("Names.txt","r")
print(file.read())
file.close()

file = open("Names.txt","r")
name = input("enter a name from the data: ")
name = name +"\n"

for row in file:
    if row != name:
        file = open("Name2.txt","a")
        new = row
        file.write(new)
        file.close()
file.close()
