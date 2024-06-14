# fav team by sport

fav_team_by_sport = {
    "football": "FC Barcelona",
    "cricket": "West Indies",
    "rugby": "Australia",
    "basketball": "Toronto Raptors",
    "tennis": "Nadal"
}

print(fav_team_by_sport['basketball'])
print()

# Ask user for a sport
# Determine if sport is in our fav list
# YES: ask them for a team
    # determine if we like the same file
# NO
    # ask for a team
        # add the team to the fav list

sport = input("Enter your favorite sport: ")

if sport in fav_team_by_sport:
    print("YES! We support you!")
    team = input("Enter your fav " + sport + " team: ")
    if team == fav_team_by_sport[sport]:
        print("Well, well, well. We like the same sport team also!")
    else:
        print("We are arch enemies because we like", fav_team_by_sport[sport])
else:
    team = input("Enter a " + sport + " team. We will add it to our list: ")
    fav_team_by_sport[sport] = team

print()

print("Here is our list")
for value in fav_team_by_sport:  # ViewObject => collection (list)  .keys(), .values(), .items()
    print(f"{value} - {fav_team_by_sport[value]}")
