'''
Define a subprogram that will ask the user to pick a low and a high
number, and then generate a random number between those
two values and store it in a variable called “comp_num”.

Define another subprogram that will give the instruction “I am
thinking of a number…” and then ask the user to guess the number they
are thinking of.

Define a third subprogram that will check to see if the
comp_num is the same as the user’s guess. If it is, it should display the
message “Correct, you win”, otherwise it should keep looping, telling the user if they are too low or
too high and asking them to guess again until they guess correctly.
'''
import random

def pick_num():
    low = int(input("Enter a low number: "))
    high = int(input("Enter a high number: "))
    comp_num = random.randint(low,high)
    return comp_num

def guess_num():
    print("I am thinking of a number...")
    num_user = int(input("Guess the number: "))
    return num_user

def check(comp_num,num_user):
    while comp_num != num_user:
        if num_user >= comp_num:
            print("Your number is to high")
            num_user = int(input("Guess again: "))
        elif num_user <= comp_num:
            print("Your number is to low")
            num_user = int(input("Guess again: "))
    print("Correct,you win!")


def main ():
         comp_num = pick_num()
         num_user = guess_num()
         check(comp_num, num_user)

main()





