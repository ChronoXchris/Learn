'''
Challenge:
Ask the user to enter two numbers. Use whole number division to divide
the first number by the second and also work out the remainder and
display the answer in a user-friendly way (e.g. if they enter 7 and 2 display
“7 divided by 2 is 3 with 1 remaining”).
'''

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))

divison = num1//num2
rest = num1%num2

print(num1, "divided by", num2, "is", divison, "with", rest, "remaining")