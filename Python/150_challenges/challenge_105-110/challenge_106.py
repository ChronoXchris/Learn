'''
Challenge:
Create a new file called “Names.txt”. Add five names to the
document, which are stored on separate lines. Once you have
run the program, look in the location where your program is
stored and check that the file has been created properly.
'''

file = open("Names.txt","w")
file.write("Theo\n")
file.write("Mac\n")
file.write("Chris\n")
file.write("Anton\n")
file.write("Roman\n")
file.close()
