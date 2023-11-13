'''
Challenge:
Ask the user to enter their name and a number. If the
number is less than 10, then display their name that
number of times; otherwise display the message “Too
high” three times.
'''

name = input("Please enter your name: ")
number = int(input("Please enter a number under 10: "))

if number < 10:
    for i in range(0,number):
        print(name)
else:
    for i in range (0,3):
        print("Too high!")
