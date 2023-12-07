'''
Challenge:
Ask the user to type in their name
and then tell them how many vowels
are in their name.
'''

count = 0
name = input("Enter your name: ")
name = name.lower()
for x in name:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
     count = count + 1
print("You have", count, "vowels in your name!")