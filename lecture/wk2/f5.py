length = int(input("Enter a length value: "))
width = int(input("Enter a width value value: "))

perimeter = 2 * (length + width)

# formatted printing
# + => additional if operand1 and operand2 are numerical
print(1 + 2)
print(1.1 + 2.1)
print(0x1 + 0b01111)
# three examples above result in sum

# + any operand not numerical
# only supports same data types for non numerical operands
# print("The perimeter of the two values is perimeter" + perimeter)

print(f"The perimeter of the two values is {'perimeter'}")

print(f"The perimeter of the two values is {perimeter}")

print(f"If length is {length} and width is {width}, then the perimeter is {perimeter}")
