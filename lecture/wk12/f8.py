import csv

fields = "Course Name;Course Code;Mark".split(";")

data = [
    {"Course Name": "Web Server", "Course Code": "comp4321", "Mark": "90"},
    {fields[0]: "CCNA", fields[1]: "comp2468", fields[2]: "80"},
    {fields[1]: "comp8642", fields[2]: "85",fields[0]: "Data Structure", },
]

with open("db3.csv", "w") as file:

    writer = csv.DictWriter(file, fieldnames=fields, delimiter=";", lineterminator="\n")

    writer.writeheader()
    writer.writerow({fields[2]: "100", fields[0]: "Intro to Programming", fields[1]: "comp1250"})

    writer.writerows(data)
    writer.writeheader()
