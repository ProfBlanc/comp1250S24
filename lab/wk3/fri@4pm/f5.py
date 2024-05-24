"""
ask the user for an age
determine their age category
    baby < 4
    child 4-12
    teen 13-17
    adult 18-64
    senior: 65+
"""

age = int(input("Enter your age: "))

if age >= 0 and age < 4:
    category = "baby"
elif age <= 12:
    category = "child"
elif age < 18:
    category = "teen"
elif age < 65:
    category = "adult"
else:
    category = "senior"

print(f"At the age of {age}, you are a {category}")