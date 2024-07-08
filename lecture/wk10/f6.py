# Program to extract numbers from a string

import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'  # all digits one or many times  = [0-9]+

result = re.findall(pattern, string)
print(result)

# Output: ['12', '89', '34']