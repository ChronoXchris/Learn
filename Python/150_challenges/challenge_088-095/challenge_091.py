'''
Challenge:
Create an array which contains
five numbers (two of which
should be repeated). Display
the whole array to the user. Ask
the user to enter one of the
numbers from the array and
then display a message saying
how many times that number
appears in the list.
'''
from array import*
number = array('i',[1,2,3,4,1])

print(number)
num = int(input("Enter a number which is in the array: "))
number.append(num)

number = sorted(number)
number_in_list = number.count(num)

print("The number", num, "is", number_in_list, "times in the list")
print(number)
