'''
Challenge:
Create a list of two sports. Ask the
user what their favourite sport is and
add this to the end of the list. Sort the
list and display it.
'''

sport = ["Swimming","Football"]
sport.append(input("What is your favourite sport: "))
sport.sort()
print(sport)