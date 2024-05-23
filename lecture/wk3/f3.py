"""
Boolean expression
    A statement (expression)
        that results in True or False

    Relational operators
        <, >, ==, !=
    Logical Operations
        reverse or combine boolean expression
"""
n1 = 10
n2 = 3
print(n1 < n2)  # False

print(n1 != n2)   # True
print(not n1 == n2)  # True

print(n1 / 5 < n2 or n2 * 10 > n1)

print(not n1 / 3 < n2 or n2 + 1 * 10 > n1 % 2)
#     not     False or n2 + 1 * 10 > n1 % 2
#     True           or n2 + 1 * 10 > n1 % 2

# is this a valid boolean expressions

"""
order of operations
not
and
or

relational operators
==, !=, <, >, <=, >=
"""

print(not n1 / 3 > n2 or n2 + 1 * 10 > n1 % 2)

print(n1 > n2 and n1 * 5 == n2 * 1.5)
