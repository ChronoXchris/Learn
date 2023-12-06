'''
Challenge:
Ask the user to type in their favourite school subject.
Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.
'''

subject = input("enter your favorite school subject: ")
for letter in subject:
    print(letter,end="-")