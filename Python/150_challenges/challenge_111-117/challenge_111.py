'''
Challenge:
Create a .csv file that will store the following data. Call it “Books.csv”.
'''

import csv

file = open("Books.csv","w")
newRecord = "To Kill A Mockingbird, Harper Lee, 1960"
file.write(str(newRecord))
newRecord = "A brief History of Time, Stephen Hawking, 1988"
file.write(str(newRecord))
newRecord = "The Great Gatsby, F.Scott Fitzgerald, 1922"
file.write(str(newRecord))
newRecord = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985"
file.write(str(newRecord))
newRecord = "Pride and Prejudice, Jane Austen, 1813"
file.write(str(newRecord))
file.close() 



