'''
Challenge:
Using the Books.csv file
from program 111, ask
the user to enter another
record and add it to the
end of the file. Display
each row of the .csv file
on a separate line.
'''
import csv

file = open("Books.csv","a")
title = input("Enter the title of the book: ")
author = input("Enter the author: ")
year = int(input("Enter the year: "))
newrecord = title + ", " + author + ", " + year + "\n"
file.write(str(newrecord))
file.close()

file = open("Books.csv","r")
for row in file:
    print(row)
file.close()


