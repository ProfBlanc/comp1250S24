"""

Create a list that stores 5 numbers

Ask the user for a number

Determine if the number is found in the list
    If so, output the index (position) where the number was found

"""

numbers = list(range(10, 21, 2))  # 10, 12, 14...20

guess = int(input("Guess a number between 10 and 20: "))

if guess in numbers:
    index = numbers.index(guess)
    print(f"The number {guess} was found at index {index}")
else:
    print(f"Sorry but the number {guess} is NOT in our list")
