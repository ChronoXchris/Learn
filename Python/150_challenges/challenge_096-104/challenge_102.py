'''
Challenge:
Ask the user to enter the name, age and shoe size for four
people. Ask for the name of one of the people in the list and
display their age and shoe size.
'''

list = {}
for i in range (0,4) :
    name = input("Enter a name: ")
    shoe_size = input("Enter the shoe size from that person: ")
    age = input("and there age: ")
    list[name] = {"Age":age,"Shoe size":shoe_size}

name1 = input("Enter a name from the list: ")
print(list[name1])

