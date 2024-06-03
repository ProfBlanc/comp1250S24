"""
string methods?
    actions on the stirng data type

list methods
    actions on the list data type?
        CRUD
        Create
        Read
        Update
        Delete

    append()
    insert()
    remove()
    sort()

"""

numbers = list(range(5, 51, 5))  # creating a list
print(numbers)
# add a value to the list
numbers.append(55)
numbers.insert(0, -5)
numbers.insert(5, -10)
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

numbers.remove(10)  # value NEEDS to exist, if not => runtime error

if 11 in numbers:
    numbers.remove(11)

print(numbers)

del numbers[7]  # remove index 7 (8th value humanly speaking)

print(numbers)
