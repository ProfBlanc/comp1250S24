import csv

headers = "Course Name,Course Code,Mark".split(",")

data = [
    ["Intro to Programming", "comp1250", "90"],
    ["Unknown Course","comp1234","95"]
]

f = open("db2.csv", "w")
writer = csv.writer(f, delimiter=";", quotechar='*', lineterminator='\n')

writer.writerow(headers)
writer.writerows(data)
f.close()