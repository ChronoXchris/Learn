'''
Challenge:
Ask the user to enter their
first name and then display
the length of their first name.
Then ask for their surname
and display the length of
their surname. Join their first
name and surname together
with a space between and
display the result. Finally,
display the length of their full
name (including the space).
'''

firstname = input("Enter your fist name: ")
print(firstname)
print(len(firstname))
lastname = input("Now enter your lastname: ")
print(lastname)
print(len(lastname))
fullname = firstname+" "+lastname
print(fullname)
print(len(fullname))