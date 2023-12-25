'''
Challenge:
Adapt program 102
to display the
names and ages of
all the people in
the list but do not
show their shoe
size.
'''

list = {}
for i in range (0,4) :
    name = input("Enter a name: ")
    shoe_size = input("Enter the shoe size from that person: ")
    age = input("and there age: ")
    list[name] = {"Age":age,"Shoe size":shoe_size}

for name in list:
    print((name),list[name]["Age"])