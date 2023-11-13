'''
Challenge:
Set a variable called total to 0. Ask the user to enter
five numbers and after each input ask them if they
want that number included. If they do, then add the
number to the total. If they do not want it included,
don’t add it to the total. After they have entered all five
numbers, display the total.
'''

total = 0

for i in range(0,5):
    number = int(input("Please enter a number that will be added to your total: "))
    add = input("Do you wane add the number?: ")
    if add == "yes":
        total = total+number
        print("Your total is", total,"!")
    else:
        print("You dont wanne add this number than type a new one")
print("Your Total at the end is:", total,"!")





