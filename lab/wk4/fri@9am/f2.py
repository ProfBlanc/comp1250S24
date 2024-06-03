numbers = list(range(5, 101, 5))
# get all the even numbers of this list => create a new list

even_numbers1 = list()

for single_number in numbers:
    if single_number % 2 == 0:
        even_numbers1.append(single_number)

# list comprehension
# x = placeholder_that_represents_a_target_value
even_numbers2 = [ x for x in numbers if x % 2 == 0 ]

print(numbers)
print(even_numbers1)
print(even_numbers2)

