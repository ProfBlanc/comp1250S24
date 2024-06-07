picnic = list()
picnic.append("water")
print(f"I'm organizing a picnic and I'm bringing", picnic[0])

while True:
    item = input("What are you bringing to the picnic? ").lower().strip()
    if item[0] == picnic[-1][-1] and item not in picnic:
        picnic.append(item)
        print("Yes, you can come to the picnic!")
    else:
        print("Sorry, you cannot come to the picnic")
        break

print("The game is over. There were", len(picnic),
      "items added to the picnic")

for item in picnic:
    print(item)