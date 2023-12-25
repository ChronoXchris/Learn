'''
Challenge:
Using program 100, ask the user for a name and a region. Display the relevant data. Ask
the user for the name and region of data they want to change and allow them to make
the alteration to the sales figure. Display the sales for all regions for the name they
choose.
'''

list = {"John":{"N":3056,"S":8463,"E":8441,"W":2694},
        "Tom":{"N":4832,"S":6786,"E":4737,"W":3612},
        "Anne":{"N":5239,"S":4802,"E":5820,"W":1859},
        "fiona":{"N":3904,"S":3645,"E":8821,"W":2451}}

print(list)

name = input("Enter a name from the list: ")
region = input("Enter a name from the list: ")

print(list[name][region])

change = input("Do you want to change the data (y/n): ")

if change == "y":
    new_region = input("Enter a new sles figure: ")
    list[name][region] = new_region
    print(list)
    print(list[name])
else:
    print("Than not")
