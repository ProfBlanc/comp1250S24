f = open("notes.txt")

print("First 50 characters of notes.txt\n\n")
print(f.read(50))
print("*" * 50)
f.seek(0)
print(f.readlines())