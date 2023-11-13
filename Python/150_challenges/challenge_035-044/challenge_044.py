'''
Challenge:
Ask how many people the user wants to invite to a party. If they enter a number below
10, ask for the names and after each name display “[name] has been invited”. If they
enter a number which is 10 or higher, display the message “Too many people”.
'''

people = int(input("How many guest do you wanne invite into your party?: "))
if people > 10:
    print("To many people!")
else:
    for i in range(0,people) :
        name = input("Please enter a name: ")
        print(name, "has been invited")
