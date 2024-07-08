import re

name = input("Enter first and last name separated by one, single whitespace character: ")
regex = r"^[a-z]{3,}\s[a-z]{5,}(-?[a-z]{3,})?$"  # names with or without hyphenate last names
regex = r"^[a-z]{3,}\s[a-z]{5,}$"  # what is the regex

valid = re.match(string=name, pattern=regex, flags=re.IGNORECASE)

if valid:
    print("Correct")
else:
    print("Incorrect")