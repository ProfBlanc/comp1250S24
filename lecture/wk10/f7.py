import re

string = 'Twelve:12 Eighty nine:89.'
list_string = 'Twelve:',' Eighty nine:','.'

pattern = '\d+'

result = re.split(pattern, string)
print(result)

# Output: ['Twelve:', ' Eighty nine:', '.']