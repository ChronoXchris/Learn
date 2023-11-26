'''
Challenge:
Create a list of six school subjects. Ask the user which of these
subjects they don’t like. Delete the subject they have chosen from the
list before you display the list again.
'''

subjects = ["Sport", "Math","English","German","History","Sience"]
print(subjects)
subjects.remove(input("Which subject do you not like: "))
subjects.sort()
print(subjects)