'''
Challenge:
Show the user a line of text from your favourite poem
and ask for a starting and ending point. Display the
characters between those two points.
'''

poem = "Two roads diverged in a yellow wood,And sorry I could not travel both"

print(poem)
start = int(input("Enter a starting point: "))
end   = int(input("Enter a end point: "))
print(poem[start:end])
