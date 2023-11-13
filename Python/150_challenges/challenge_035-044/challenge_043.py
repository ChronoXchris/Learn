'''
Challenge:
Ask which direction the user wants to count (up or down). If they select up, then ask
them for the top number and then count from 1 to that number. If they select down, ask
them to enter a number below 20 and then count down from 20 to that number. If they
entered something other than up or down, display the message “I don’t understand”.
'''

direction = input("Do you wane count down or up? ")
if direction == "up":
    number = int(input("Please enter a number to count up to: "))
    for i in range(0,number+1):
        print(i)
elif direction == "down":
    number = int(input("Please enter a number to count down to that is below 20: "))
    for i in range(20,number-1,-1):
        print(i)
else:
    print("I dont understand")