dow = input("Enter the day of the week: ")
tod = int(input('Enter the time of the day: '))


# monday, mon, Mon, MONDAY, MON
if dow.lower().startswith("fri") or dow == "5" or dow[0] == "5" and tod >= 9 and tod <=11:
    print("Please attend the awesome comp1250 lab")
else:
    print("I don't know the rest of your schedule")
