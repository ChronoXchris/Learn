'''
Challenge:
Using the Books.csv file, ask the user
to enter a starting year and an end
year. Display all books released
between those two years.
'''
import csv

start_year = int(input("Enter a start year: "))
end_year = int(input("Enter a end year: "))

file = list(csv.raeder(open("Books.csv")))
tmp = []
for row in file:
    tmp.append.row

x = 0
for row in tmp
    if int(tmp[x][2]) >= start_year and int(tmp[x][2]) <= end_year:
        print(tmp[x])
    x = x+1
