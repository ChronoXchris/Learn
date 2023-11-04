'''
Challeng: 
Ask how many slices of pizza the user started with and ask how many slices they have eaten.
Work out how many slices they have left and display the answer
'''
startedslices = int(input("With how many slices of pizza do you have?: "))
eatenslices = int(input("how many slices did you eat?: "))
leftslices = startedslices - eatenslices
print("You are left with", leftslices, "of pizza!")