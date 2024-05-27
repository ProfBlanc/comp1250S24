# ask the user for the DOW
# ask the user for TOD

# using IF statements
# determine which class they
# should attend

"""
What day of the week is it?
Monday

What time is it?
11

Hey, you should attend comp1250 lecture

"""
dow = input("What day is it?")
tod = int(input("What time is it?"))

if dow.lower() == "monday" and tod >= 11 and tod <= 13:
    print("Attend comp1250 lecture!")
elif "MON" in dow.upper() and tod >= 9 and tod <= 11:
    print("Attend Network Security class")
elif dow.title()[0:5] == "Thurs":
    if tod >= 13 and tod <= 15:
        print("Attend Math class")
    elif tod >= 8 and tod <= 10:
        print("Attend Linux class")
elif dow[0:2] == "tu" or dow[0:2] == "Tu" and tod >= 12 and tod <= 14:
    print("Attend Comp3105 lab")
