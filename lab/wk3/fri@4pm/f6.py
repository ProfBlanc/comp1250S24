"""
mon @ 11
    comp1250 lecture

fri
    @ 16
    comp1250 lab
    @ 14
    comp1176

tues @ 15
    comp3105 lab
"""

dow = input("Enter a day of the week: ")
tod = int(input("Enter a time of the day"))

if "mon" in dow.lower() and tod >= 11 and tod <= 13:
    print("YOu should attend the comp1250 lecture")
elif dow.upper()[0] == "F" and tod >= 14 and tod <= 16:
    print("You should attend your comp1176 lab")
elif dow.upper()[0] == "F" and tod >16 and tod <= 18:
    print("You should attend your comp1250 lab")

# elif dow.upper()[0] == "F":
#     if tod >= 14 and tod <= 16:
#         print("You should attend your comp1176 lab")
#     elif tod > 16 and tod <= 18:
#         print("You should attend your comp1250 lab")