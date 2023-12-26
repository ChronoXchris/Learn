'''
Challenge:
Open the Names.txt file. Ask the user to input a
new name. Add this to the end of the file and
display the entire file.
'''

file = open("Names.txt","a")
name = input("Enter a new name for the file: ")
file.write(name + "\n")
file.close()

