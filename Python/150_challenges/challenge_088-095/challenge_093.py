'''
Challenge:
Ask the user to enter five
numbers. Sort them into order
and present them to the user.
Ask them to select one of the
numbers. Remove it from the
original array and save it in a
new array.
'''

from array import*
counter = 0
number_1 = array('i',[])
number_2 = array('i',[])

for i in range(0,5):
    num = int(input("Enter a number: "))
    number_1.append(num)
    number_1 = sorted(number_1)

print(number_1)

remove = int(input("Enter a number to remove number: "))

number_1.remove(remove)
number_2.append(remove)

print(number_1)
print(number_2)





