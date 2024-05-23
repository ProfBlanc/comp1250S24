# ask the user for there georgebrown college email
# validate the GBC email

email = input("Enter your George Brown College Email")

#123456789@georgebrown.ca

# string slicing

only_student_id = email[0:9]
"""
email: 101896521@georgebrown.ca

0   1   2   3   4   5   6   7   8   9

1   0   1   8   9   6   5   2   1   @         
"""

if "@georgebrown.ca" in email and email[0:9].isdigit():
    print("Valid GBC email! Good job!")
else:
    print("Invalid email")