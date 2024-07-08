import re
text = "everyone loves python not the snake but the programming language"
pattern = r"python|snake"

match = re.search(pattern=pattern, string=text) # returns match object
print(match)

span1 = match.span()
print(span1[0], span1[1])
