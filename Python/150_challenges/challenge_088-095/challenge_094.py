'''
Challenge:
Display an array of five
numbers. Ask the user to
select one of the numbers.
Once they have selected a
number, display the
position of that item in the
array. If they enter
something that is not in
the array, ask them to try
again until they select a
relevant item.
'''
tryagain = False
from array import*
number = array('i',[9,13,37,42,28])

print(number)

num = int(input("Enter a number that is in the array: "))
while num == False:
    if num in number:
        print(num)
        tryagain = True
    else:
        print("Try again: ")



