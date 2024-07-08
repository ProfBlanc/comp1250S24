import re
text = "everyone loves python not the snake but the programming language"
pattern = r"python|snake"
#pattern = r"[python|sake]"

hits = re.findall(pattern=pattern, string=text)
print(hits)