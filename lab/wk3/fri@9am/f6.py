"""
if <boolean expression>:
    statements if expression is true
elif <boolean expression>:
    statements if expression is true
else
"""

age = int(input("Enter your age: "))

# determine their age category
category = ""
if age <= 4 and age >= 0:
    category = "baby"
elif age <= 12:
    category = "child"
elif age <= 18:
    category = "teen"
elif age <= 65:
    category = "adult"
else:
    category = "elder"

print(f"At the age of {age}, you are a {category}")