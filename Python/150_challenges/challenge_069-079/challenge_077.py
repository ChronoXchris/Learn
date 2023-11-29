'''
Challenge:
Change program 076 so that once the user has completed their list of names, display the
full list and ask them to type in one of the names on the list. Display the position of that
name in the list. Ask the user if they still want that person to come to the party. If they
answer “no”, delete that entry from the list and display the list again.
'''

invite = 3
dude1 = input("Invite a dude to your party: ")
dude2 = input("Invite a second dude to your party: ")
dude3 = input("Invite a third dude to your party: ")
invite_list = [dude1,dude2,dude3]
another = input("do you wane invite more dudes? (yes/no): ")
while another == "yes":
    moredudes = invite_list.append(input("Invite a dude: "))
    invite = invite+1
    another = input("Do you wane invite more dudes (yes/no): ")
print(invite_list)
print(invite)
userceck = input("Enter a dude from the list: ")
print(userceck,"is in the position",invite_list.index(userceck))
ask = input("Should the person still come (y/n): ")
if ask == "n":
    invite_list.remove(userceck)
    print(invite_list.sort())
