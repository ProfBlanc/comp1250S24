picnic = list()
picnic.append("water")

print("I, the organizer, am organizing "
      "a picnic. I am bringing", picnic[0])

while True:

    print("Please recite all of the previous items")
    copied_picnic = picnic.copy()
    tracker = 0
    can_add = True
    while len(copied_picnic) > 0:
        tracker += 1
        ask = input(f"Enter item {tracker} of {len(picnic)}: ").lower()
        if ask in copied_picnic:
            print("Correct!", ask, "is in the picnic")
            copied_picnic.remove(ask)
        else:
            print("Sorry, but", ask, "is not in the picnic")
            can_add = False
            break

    if not can_add:
        break

    new_item = input("Enter a new item to add to the picnic")
    picnic.append(new_item)
    print("Moving on to the next turn")