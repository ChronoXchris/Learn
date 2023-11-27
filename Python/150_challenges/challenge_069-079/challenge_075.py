'''
Challenge:
Create a list of four three-digit
numbers. Display the list to the
user, showing each item from
the list on a separate line. Ask
the user to enter a three-digit
number. If the number they
have typed in matches one in
the list, display the position of
that number in the list,
otherwise display the message
“That is not in the list”.
'''

numbers = [243,324,142]
for i in numbers:
    print(i)
usernumber = int(input("please enter a number: "))
if usernumber in numbers :
    print(numbers.index(usernumber))
else:
    print("That is not in the list!")