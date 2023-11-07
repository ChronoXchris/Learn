'''
Challenge:
Ask the user to type in the first line of a nursery rhyme and
display the length of the string. Ask for a starting number and an
ending number and then display just that section of the text
(remember Python starts counting from 0 and not 1).
'''

ryhme = str(input("Please enter the first line of a nursery rhyme: "))

length = len(ryhme)

print("The ryme has", length, "in it!")

startnum = int(input("Please enter a Starting number: "))
endnum = int(input("Please enter a Ending number: "))

section = lenth[startnum:endnum]

print(section)

