'''
challenge:
Using the Books.csv file, ask the user how many records
they want to add to the list and then allow them to add
that many. After all the data has been added, ask for an
author and display all the books in the list by that author.
If there are no books by that author in the list, display a
suitable message.
'''

import csv

add = int(input("How many records do you ant to add?: "))

for x in range(0,add):
    file = open("Books.csv", "a")
    title = input("Enter the title of the book: ")
    author = input("Enter the author: ")
    year = int(input("Enter the year: "))
    newrecord = title + ", " + author + ", " + year + "\n"
    file.write(str(newrecord))
file.close()

file = open("Books.csv","r")
count = 0
author = input("enter a Author from the record: ")
reader = csv.reader(file)
for row in file:
    if author in str(row):
        print(row)
        count = count + 1
if count == 0:
    print("ERROR there are no books from this author!")
file.close()

