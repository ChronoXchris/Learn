'''
Challenge:
Using the Books.csv file, display the data in
the file along with the row number of each.
'''

import csv

file = open("Books.csv","r")
x = 0
for row in file:
    display = "Row: " +str[x] + "-" + row
    print(display)
    x = x+1
