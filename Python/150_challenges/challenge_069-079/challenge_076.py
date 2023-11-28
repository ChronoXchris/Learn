'''
Challenge:
Ask the user to enter the names of three people they want to
invite to a party and store them in a list. After they have entered
all three names, ask them if they want to add another. If they do,
allow them to add more names until they answer “no”. When
they answer “no”, display how many people they have invited to
the party.
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

