'''
Challange:
Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result.
'''

name = input("Please enter your name: ")
surname = input("Please enter your name: ")

lname = name.lower()
lsurname = surname.lower()

tname = lname.title()
tlastname = lsurname.title()

print(tname, tlastname)