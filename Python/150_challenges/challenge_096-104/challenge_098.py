'''
Challenge:
Using the 2D list from program 096, ask the user
which row they would like displayed and display
just that row. Ask them to enter a new value and
add it to the end of the row and display the row
again.
'''

list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

print(list)

row = int(input("Enter a row from the list: "))
print(list[row])
add_number = int(input("Enter a number you wnt to add: "))

list[row].append(add_number)

print(list)