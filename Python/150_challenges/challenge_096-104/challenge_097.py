'''
Challenge:
Using the 2D list from program 096, ask the user to
select a row and a column and display that value.
'''

list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

print(list)

row = int(input("Enter a row from the list: "))
column = int(input("Enter a column: "))

print(list[row][column])