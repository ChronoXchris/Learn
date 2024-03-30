'''
Display the following menu to the user:
If they enter a 1, it should run a subprogram that will
generate two random numbers between 5 and 20, and
ask the user to add them together. Work out the correct
answer and return both the user’s answer and the
correct answer.
If they entered 2 as their selection on the menu, it
should run a subprogram that will generate one number
between 25 and 50 and another number between 1 and
25 and ask them to work out num1 minus num2. This
way they will not have to worry about negative answers.
Return both the user’s answer and the correct answer.
Create another subprogram that will check if the user’s
answer matches the actual answer. If it does, display
“Correct”, otherwise display a message that will say
“Incorrect, the answer is” and display the real answer.
If they do not select a relevant option on the first menu
you should display a suitable message.
'''

import random

def addition():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    print(num1,"+", num2); user_answer= int(input("="))
    actual_answer =  num1 + num2
    answers = (actual_answer,user_answer)
    return answers


def subtraction():
    num1 = random.randint(25,50)
    num2 = random.randint(1,25)
    print(num1,"-", num2); user_answer= int(input("="))
    actual_answer =  num1 -  num2
    answers = (actual_answer,user_answer)
    return answers


def check(user_answer,actual_answer):
    if user_answer == actual_answer:
        print("Correct")
    else:
        print("Incorrect")

def menu():
    print("1) Addition")
    print("2) Subtraction")
    chose = int(input("Enter 1 or 2: "))
    if chose == 1:
        user_answer, actual_answer = addition()
        check(user_answer, actual_answer)
    elif chose == 2:
        user_answer, actual_answer = subtraction()
        check(user_answer,actual_answer)
    else:
        print("Incorrect selection")
menu()





