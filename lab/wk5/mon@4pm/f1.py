"""

Picnic Game
    I am planning a picnic and I am bringing water

    Each person is going to determine what the last item added to the picnic list
    was, add an item that starts with the last letter for the most recently added item

    1st: add an item that starts with R
        prompt: what are you going to bring? RICE
            I am going to RICE
                evaluate the input => ensure that it follows the rule
                    if does, add it to the picnic list
                    if does not, stop playing the game.

    2nd: add an items that starts with e
        prompt what are you going to bring? EGGS

"""

picnic = ["water"]

print("Me, the picnic organizer is planning a picnic. I am going to bring ", picnic[0])

while True:  # continually ask
    ask = input("What are you going to bring? ").strip().lower()
    last_letter = picnic[-1][-1].lower()
    if ask[0] == last_letter:
        print("Yes, you can bring", ask, "to the picnic")
        picnic.append(ask)
    else:
        print("Uh oh, you broke the game. You had to enter an item that started with "
              "the letter", last_letter)
        break  # escape, stop a loop

print("*" * 20)
print("The picnic will have", len(picnic), "items.")
print("Here are the items:", ", ".join(picnic)  )
