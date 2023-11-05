'''
Challenge:
Ask the user if it is raining and convert their answer to lower case
so it doesn’t matter what case they type it in. If they answer “yes”,
ask if it is windy. If they answer “yes” to this second question,
display the answer “It is too windy for an umbrella”, otherwise
display the message “Take an umbrella”. If they did not answer yes
to the first question, display the answer “Enjoy your day”.
'''

q1 = input("Is it raining?: ")
q2 = input("Is it windy?: ")

q1 = q1.lower()
q2 = q2.lower()

if q1 == "no":
    print("Enjoy your day!")


if q1 == "yes" and q2 == "no":
    print("You need a umbrella")
elif q1 == "yes" and q2 == "yes":
    print("It is to windy for a umbrella, stay at home")

