'''
Challenge:
Ask the user to enter a number that is under 20.
If they enter a number that is 20 or more, display the
message “Too high”, otherwise display
“Thank you”.
'''
num = int(input("Please enter a number that is lower than 20: "))

if num <= 20:
    print("Thank you!")
else:
    print("The number is to high!")