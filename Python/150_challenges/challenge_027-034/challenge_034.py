'''
Challenge:
Display the following message:
If the user enters 1, then it should ask them for
the length of one of its sides and display the
area. If they select 2, it should ask for the base
and height of the triangle and display the area. If
they type in anything else, it should give them a
suitable error message.
'''

num1 = "1) Square"
num2 = "2) Triangle"

print(num1)
print(num2)
print()
selection = int(input("Enter a number: "))

if selection == 1:
    side = int(input("Please enter the side lengt of one side: "))
    area = side*side
    print("The are of the Square is:",area)
elif selection == 2:
    base = int(input("Please enter the base of the Triangle: "))
    height = int(input("Please enter the height of the Triangle: "))
    area2 = (base*height)/2
    print("The area of the Triangle is:", area2)
else:
    print("Please enter a number 1 or 2")