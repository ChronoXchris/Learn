'''
Challenge:
Ask the user for a list of five
integers. Store them in an array.
Sort the list and display it in
reverse order.
'''

from  array import *

nums = array('i', [])

for i in range(0,5):
    number = int(input("Enter a number: "))
    nums.append(number)

nums = sorted(nums)
nums.reverse()

print(nums)