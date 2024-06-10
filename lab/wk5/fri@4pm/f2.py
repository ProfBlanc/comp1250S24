picnic = list()
picnic.append('water')

print("I am organizing a picnic. I will bring", picnic[0])

game = True

while game:
    item = input("What will you bring to the picnic? ").lower()
    if item not in picnic and item[0] == picnic[-1][-1]:
        print("You can come to the picnic")
        picnic.append(item)
    else:
        print("Sorry but", item, "is not valid")
        game = False

print("There are", len(picnic), "items in the picnic")
for item in picnic:
    print(item)
