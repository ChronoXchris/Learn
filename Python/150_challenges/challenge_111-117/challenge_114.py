'''
Challenge:
Using the Books.csv file, ask the user
to enter a starting year and an end
year. Display all books released
between those two years.
'''

file = open("Books.csv","r")
start_year = int(input("Enter a start year: "))
end_year = int(input("Enter a end year: "))
