'''
Challenge:
Create a list containing the titles of
four TV programmes and display
them on separate lines. Ask the
user to enter another show and a
position they want it inserted into
the list. Display the list again,
showing all five TV programmes in
their new positions.
'''

tv_programs = ["Toggo","Disney","NC","RTL"]
for i in tv_programs:
    print(i)
add_show = input("enter a new show: ")
position = int(input("Enter a position for the TV program: "))
tv_programs.insert(position,add_show)
print(tv_programs)
