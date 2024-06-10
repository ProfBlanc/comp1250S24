picnic = list()
picnic.append("water")

print("I am organizing a picnic and I'm bringing",
      picnic[0])

allow = True

while allow:
      print("Please recite all of the previous items")
      tracker = 0
      copied_picnic = picnic.copy()
      while len(copied_picnic) > 0:
            tracker += 1
            print("Enter item", tracker, "of", len(picnic), ": ")
            ask = input()
            if ask in copied_picnic:
                  copied_picnic.remove(ask)
                  print("Correct", ask, "is in the picnic")
            else:
                  print("Sorry, but", ask, "is NOT on the list")
                  allow = False
                  break

      if allow:
            print("You have earned the right to add a picnic item")
            item = input("Enter a new item: ").lower()
            if item not in picnic:
                  picnic.append(item)
                  print("Let's move on to the next player")
            else:
                  allow = False
                  print("Sorry, but", item, "is already in the picnic")

