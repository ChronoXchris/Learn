'''
Challenge:
Enter a list of ten colours. Ask the user for a starting number between 0 and 4
and an end number between 5 and 9. Display the list for those colours
between the start and end numbers the user input.
'''

colours =  ["green","black","red","white","blue","orange","pink","yellow","brown","grey"]
startnum = int(input("Give me a number between 0 and 4: "))
endnum   = int(input("Give me a number between 5 and 9: "))
print(colours[startnum:endnum])
