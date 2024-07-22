import csv

fields = "Course Name;Course Code;Mark".split(";")


with open("db3.csv", "r") as file:

    reader = csv.DictReader(file, fieldnames=fields, delimiter=";", lineterminator="\n")

    for line in reader:
        print(line) # dictionary
        print("Course Name =", line[fields[0]])
        print("Course Code =", line[fields[1]])
        print("Course Mark =", line[fields[2]])