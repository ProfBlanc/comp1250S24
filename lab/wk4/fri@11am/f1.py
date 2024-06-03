"""
generate a list of numbers between 30 and 50, counting by 2's
ask the user for a number
    determine if the number is in the list
        output the index
    display a sorry message
"""

numbers = list(range(30, 51, 2))
guess = int(input("Guess a number between 30 and 50: "))

if guess in numbers:
    index = numbers.index(guess)
    print(f"The number {guess} was found at index {index}")
else:
    print(f"Sorry but the number {guess} was not found in the list. ")
