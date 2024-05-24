dow = input("Enter the day of the week: ")
tod = int(input('Enter the time of the day: '))


# monday, mon, Mon, MONDAY, MON
if dow.lower().startswith("fri") or dow == "5" or dow[0] == "5":
    if tod >= 9 and tod <=11:
        print("Please attend the awesome comp1250 lab")
    elif tod >= 11 and tod <=13:
        print("Please attend the Networking lab class")
    else:
        print("You can now go home and enjoy your weekend")
elif dow.lower().startswith("mon") or dow == "1":
    if tod >= 11 and tod <= 13:
        print("Please attend the even more awesome comp1250 lecture")
else:
    print("I don't know the rest of your schedule")
