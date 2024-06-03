"""
Iteration Structure
    a struction where we repeat instruction
    2 iteration structures (loops)
        For
            iterate through a collection of values
                string, list, tuple, range and others
        While
            continually repeat instruction until a boolean condition is met

"""
for each_letter in "Ben Blanc":
    print(each_letter)

print("*" * 20)

values = ["hi", "dry", "bye", "cry"]

for each_item in values:
    print(each_item)

print("*" * 20)

for each_number in range(10, 101, 10):
    print(each_number)

print("*" * 20)

# "Index 0 has a value of hi"
for index in range( len(values) ):
    print(f"Index {index} has a value of {values[index]}")


range(10)  # 0-9

range(1, 11)  # 1-10

range(1, 11, 3)  # 1, 4, 7, 10
