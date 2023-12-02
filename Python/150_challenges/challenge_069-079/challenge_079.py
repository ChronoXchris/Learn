'''
Challenge:
Create an empty list called “nums”.
Ask the user to enter numbers.
After each number is entered, add
it to the end of the nums list and
display the list. Once they have
entered three numbers, ask them if
they still want the last number they
entered saved. If they say “no”,
remove the last item from the list.
Display the list of numbers.
'''

nums = []
for i in range(0,3):
    number = int(input("Enter a number: "))
    nums.append(number)
print(nums)
keep = input("Do you want to keep the last nummer?(y/n): ")
if keep == "n":
    nums.remove(number)
    print(nums)
else:
    print(nums)
