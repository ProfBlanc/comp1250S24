picnic = list()
picnic.append('water')
print("I am organizing a picnic. I will bring", picnic[0])
game = True

while game:
    counter = 0
    copy_of_picnic = picnic.copy()
    print("Please recall all of the picnic items")
    while len(copy_of_picnic) > 0:
        counter += 1
        print(f"Enter item", counter, "of", len(picnic))
        guess = input().lower()
        if guess in copy_of_picnic:
            print(guess, "is, indeed in the picnic")
            copy_of_picnic.remove(guess)
        else:
            print("Sorry, but", guess, "is NOT in the picnic")
            game = False
            break

    if game:
        print("You have earned the right to enter a new picnic item")
        item = input().lower()
        if item not in picnic:
            picnic.append(item)
            print("Next person's turn!")
        else:
            game = False
            print("Sorry but", item, "already exists in the picnic")


