'''
Today we will program a calculator that can give tips and split the bill
'''
print("Welcome to the tip calculator!")
number = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill? "))
newnumber = int(number)
pay = round(((newnumber+(newnumber*(tip/100)))/people),3)

print("Each person should pay:",pay)