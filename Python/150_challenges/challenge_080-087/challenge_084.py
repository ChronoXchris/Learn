'''
Challenge:
Ask the user to type in their
postcode. Display the first
two letters in uppercase.
'''

postcode = input("Enter your postcode: ")
upper = postcode.upper()
print(upper[0:2])