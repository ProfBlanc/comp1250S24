"""

Organizer: states 1 item that they will bring to the picnic
    I will bring water to the picnic

Each person must state what items were previously added to the picnic BEFORE adding a new item to the picnic

    Person 1:
        What things were brought the picnic
            Thing 1 of 1: water
        If correctly guessed
            Good, what new item will you bring to the picnic? RICE
        If not,
            display sorry message and stop the game

    Person 2:
        What things were brought the picnic
            Thing 1 of 2: water
            Thing 2 of 2: rice
        If correctly guessed
            Good, what new item will you bring to the picnic? EGGS
        If not,
            display sorry message and stop the game

    Person 3:
        What things were brought the picnic
            Thing 1 of 3: water
            Thing 2 of 3: rice
            Thing 3 of 3: eggs
        If correctly guessed
            Good, what new item will you bring to the picnic? SUGAR
        If not,
            display sorry message and stop the game

"""

picnic = ["water"]

print("I will bring water to the picnic", picnic[-1])
end_game = False
while not end_game:
    print("What things were brought the picnic?")
    test_memory = picnic.copy()

    for item_number in range(0, len(picnic)):
        prompt = f"Enter item {item_number + 1} of {len(picnic)}: "
        guess = input(prompt).strip().lower()  # strip removes whitespace b4 and after content
        # ' water ' => 'water'
        # '      rice      ' => 'rice'
        # 'e   g   g   s'  => remains the same
        if guess in test_memory:
            test_memory.remove(guess)
            print("Correct guess")
        else:
            end_game = True
            break

    if end_game:
        print("Sorry but you did not correctly guess a previous item")
    else:
        new_item = input("Enter a new item to bring to the picnic: ").strip().lower()
        if new_item not in picnic:
            picnic.append(new_item)
        else:
            print("Sorry, but", new_item, "is already found in the list")
            end_game = True

print("*" * 20)
print("The picnic will have", len(picnic), "items.")
print("Here are the items:", ", ".join(picnic)  )




