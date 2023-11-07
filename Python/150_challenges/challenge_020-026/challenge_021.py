'''
Challenge:
Ask the user to enter their first name and then ask them to
enter their surname. Join them together with a space between
and display the name and the length of whole name.
'''
name = input("Please enter your name: ")
lastname = input("Please enter your lastname: ")
fullname = name + " " + lastname
length = len(fullname)
print(length)
