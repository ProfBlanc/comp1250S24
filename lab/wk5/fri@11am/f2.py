picnic = list()
picnic.append("water")

print("I am organizing a picnic and I'm bringing",
      picnic[0])

while True:
    attempt = input("What are you bringing to the picnic? ").lower()
    if attempt[0] == picnic[-1][-1] and attempt not in picnic:
        print("Yes, you can come to the picnic")
        picnic.append(attempt)
    else:
        print("Sorry, but", attempt, "is unacceptable")
        break

print("Here are the picnic items")
for item in picnic:
    print(item)

