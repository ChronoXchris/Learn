'''
Challenge:
Ask the user to enter numbers. If they enter a
number between 10 and 20, save it in the array,
otherwise display the message “Outside the
range”. Once five numbers have been
successfully added, display the message “Thank
you” and display the array with each item shown
on a separate line.
'''

from array import*
counter = 0
number = array('i',[])

while counter != 5:
    num1 = int(input("Enter a number between 10 and 20: "))

    if num1 >= 10 and num1 <= 20:
        number.append(num1)
        counter = counter +1
    else:
        print("Outside the Range")
        num1 = int(input("Try again: "))
print("Thank you!")
for i in number:
    print(i)



