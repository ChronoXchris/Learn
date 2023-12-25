'''
Challenge:
After gathering the four names, ages and shoe sizes, ask the
user to enter the name of the person they want to remove from
the list. Delete this row from the data and display the other rows
on separate lines.
'''

list = {}
for i in range (0,4) :
    name = input("Enter a name: ")
    shoe_size = input("Enter the shoe size from that person: ")
    age = input("and there age: ")
    list[name] = {"Age":age,"Shoe size":shoe_size}

name1 = input("Enter a name from the list that you want to remove: ")

del list [name1]

for name in list:
    print((name),list[name]["Age"],list[name]["Shoe size"])
