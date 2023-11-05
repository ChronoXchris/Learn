'''
Challenge:
Ask the user to enter their favourite colour. If they enter “red”, “RED” or
“Red” display the message “I like red too”, otherwise display the message
“I don’t like [colour], I prefer red”.
'''

colour = input("What colour do you like?: ")

if colour == "RED" or colour == "red" or colour == "Red":
    print("I like red too!")
else:
    print("I dont like the colour", colour, "I prefer Red")