'''
Challenge:
Add to program 069 to ask the
user to enter a number and
display the country in that
position.
'''

countries_tuple = ("Pakistan","Germany","France","Greece","Italy")

print(countries_tuple)
print()
countrie = input("enter a country from the list: ")
print(countrie,"has the index number",countries_tuple.index(countrie))
print()
number = int(input("enter a number from 0-4 to show a country: "))
print()
print(countries_tuple[number])
