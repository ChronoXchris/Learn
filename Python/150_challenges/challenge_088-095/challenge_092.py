'''
Challenge:
Create two arrays (one
containing three numbers that
the user enters and one
containing a set of five random
numbers). Join these two arrays
together into one large array.
Sort this large array and display
it so that each number appears
on a separate line.
'''
import random
from array import*
counter = 0
number_user = array('i',[])
number_computer = array('i',[])

while counter != 3:
    num = int(input("Enter a number: "))
    number_user.append(num)
    number_user = sorted(number_user)
    counter = counter +1

for i in range(0,5):
    num2 = random.randint(0,19)
    number_computer.append(num2)
    number_computer = sorted(number_computer)

print(number_user)
print(number_computer)

number_user.extend(number_computer)

number_user = sorted(number_user)

print(number_user)

for i in number_user:
    print(i)






