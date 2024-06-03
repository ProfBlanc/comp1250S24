"""
Ask the user for 5 numbers and add these numbers to a list?
"""
nums = list()
for ask in range(5):
    number = int(input("Enter a number: "))
    nums.append(number)

print("The numbers that you inputted where")
for each_number in nums:
    print(each_number)