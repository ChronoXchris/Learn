'''
Challenge:
Alter program 035 so that it will ask the user to enter their
name and a number and then display their name that
number of times.
'''

name = str(input("Please enter your name: "))
number = int(input("Please enter a number: "))
for i in range (0,number):
    print(name)