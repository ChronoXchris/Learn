'''
Challeng: 
Task the user to enter a number over 100 and then enter 
a number under 10 and thell them how many 
times the smaller number goes into the lager number
'''
lager = int(input("Please enter a number over 100: "))
smaller = int(input("Please enter a nummber under 10: "))

answer = lager//smaller

print(answer)  