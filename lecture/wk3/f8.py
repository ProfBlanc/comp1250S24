grade = int(input("Enter your grade: "))
if grade >= 90:
    print("You are on the Dean's List!")
elif grade >=80 and grade <= 89:
    print("You are on the honor roll")
elif grade >= 70:
    print("You got a B")
elif grade >= 60:
    print("You got a C")
elif grade >= 50:
    print("You got a D")
else:
    print("Uh oh! You didn't pass")
