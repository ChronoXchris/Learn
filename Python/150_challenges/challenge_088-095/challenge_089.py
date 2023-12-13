'''
Challenge:
Create an array which will store a list of integers.
Generate five random numbers and store them in
the array. Display the array (showing each item on
a separate line).
'''

import random
from  array import *

nums = array('i', [])

for i in range(0,5):
    number = random.randint(1,100)
    nums.append(number)

for x in nums:
    print(x)
