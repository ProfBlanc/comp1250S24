import csv

with open("db2.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")
    for line in reader:
        print(line)
        print(line[0], line[1], line[2])