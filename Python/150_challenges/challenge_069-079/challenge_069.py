'''
Challenge:
Create a tuple containing the names of five countries and display the whole tuple. Ask
the user to enter one of the countries that have been shown to them and then display
the index number (i.e. position in the list) of that item in the tuple.
'''

countries_tuple = ("pakistan","germany","france","greece","italy")

print(countries_tuple)
print()
countrie = input("enter a country from the list: ")
print(countrie,"has the index number",countries_tuple.index(countrie))
