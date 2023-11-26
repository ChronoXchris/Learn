'''
Challenge:
Ask the user to enter four of their favourite foods and store them in
a dictionary so that they are indexed with numbers starting
from 1. Display the dictionary in full, showing the index number
and the item. Ask them which they want to get rid of and remove it
from the list. Sort the remaining data and display the dictionary.
'''

foods = {1:input("what is your 1 favorite food: "),2:input("what is your 2 favorite food: "),3:input("what is your 3 favorite food: "),4:input("what is your 4 favorite food: ")}
print(foods)
dislike = int(input("What do you wanne remove:"))
del foods[dislike]
print(sorted(foods.values()))