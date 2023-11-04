'''
Challeng: 
Write a program that will ask for a number of days and 
then will show how many hours, minutes and seconds are in that number of days
'''
days = int(input("How many days would you like to know in hours, minuts and secends: "))
hours = days*24
minutes = hours*60
secend = minutes*60
print(days, "days would be",hours, "hours")
print(minutes, "minutes")
print(secend, "seconds")
