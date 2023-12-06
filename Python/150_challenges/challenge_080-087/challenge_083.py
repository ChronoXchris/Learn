'''
Challenge:
Ask the user to type in a word in upper case. If they
type it in lower case, ask them to try again. Keep
repeating this until they type in a message all in
uppercase.
'''

message_upper = input("Enter a message in upper case: ")
tryagain = False
while message_upper == False:
    if message_upper.isupper():
        print("Thank you")
        tryagain = True
    else:
        print("Try again")
        message_upper = input("Enter a message in upper case: ")