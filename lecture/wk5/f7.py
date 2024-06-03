"""
Ask the user for 5 DISTINCT numbers
"""

nums = list()  # nums = []

while len(nums) < 5:
    number = int(input("Enter a distinct/unique number: "))
    if number in nums:
        print("Sorry but", number, "is already in the list")
    else:
        nums.append(number)
        print(number, "has been added to our list. Please add", 5 - len(nums) , "more unqiue numbers")

print("*" * 20)
print("Here are the values that you inputted in ascending order")
# nums.sort()  # change original numbers, does not return a new list
# sorted(collection of values) returns a new list
for each_number in sorted(nums, reverse=True):
    print(each_number)