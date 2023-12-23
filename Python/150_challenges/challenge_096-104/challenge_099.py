'''
Challenge:
Change your previous program
to ask the user which row they
want displayed. Display that
row. Ask which column in that
row they want displayed and
display the value that is held
there. Ask the user if they want
to change the value. If they do,
ask for a new value and change
the data. Finally, display the
whole row again.
'''

list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

print(list)

row = int(input("Enter a row from the list: "))
print(list[row])

column = int(input("Enter a column you want do display in that row: "))
print(list[row[column]])

change_value = input("Do you want to change the value? (y/n):  ")

if change_value == "y":
    new_value = int(input("Enter a new value: "))
    list[row][column]= new_value
    print(list)
else:
    print(list)


