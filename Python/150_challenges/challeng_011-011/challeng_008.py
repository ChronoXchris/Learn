'''
Challeng: 
ask for the total price of the bill, then ask how many siners there are.
Divide the total bill by the number of diners and show hpw much each person must pay.
'''
bill = int(input("How much is the bill?: $"))
diners = int(input("how many diners were ther?: "))
dinereach = bill/diners
print("Each person needs to pay", dinereach, "$!")
