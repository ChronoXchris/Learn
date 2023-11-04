'''
Challeng: 
Ask the user to enter three numbers. Add toghter the first two numbers
and then multiply this total by the third. Display the answer
'''
n1 = int(input("Please enter a number: ")) 
n2 = int(input("Please enter a second number to add them: "))
n3 = int(input("Please enter a third number to multiply the answer: "))
print("If you add", n1, "and" ,n2 ,"together you will get", n1+n2,"!")
print("And if you multiply that by", n3, "you will get",(n1+n2)*n3, "!" )
