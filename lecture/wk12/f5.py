import os

f = open("t1.bin", "rb")

content = f.read()

string = content.decode()

# print(content)
print(string, file=open("str.txt", "w"))
