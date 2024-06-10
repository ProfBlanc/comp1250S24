"""
Create a script that will ask the users
how many countries they have visited

For each of these countries, ask user how many cities they have visited

For each of these cities, how many days did they spend in that city


canada
    toronto
        120
    montreal
        7
    vancouver
        90
    kenora
        40
    paris
        2
    waterloo
        20
    london
        25
france
    paris
        20
england
    london
        5
    waterloo
        2
usa
    new york
        10
    miami
        7
south africa
    cape town
        5


How many cities did you spend at most 5 days in?

How many cities did you visit that had the same name but were located in different countries

"""
data = {
    "canada": {"toronto": 120, "paris": 2, "waterloo": 20, "montreal": 7, "london": 25, "kenora": 20, "vancouver": 90},
    "usa": {"new york": 10, "miami": 7},
    "france": {"paris": 20},
    "england": {"london": 5, "waterloo": 2},
    "south africa": {"cape town": 5},
}

cities_only_5_days = dict()  # add a dictionary for each  value

# {"canada": ["paris"], "england": ["london", "waterloo"],
#  "south africa": ["cape town" ]}


for country in data:  # by default, iterate through the keys
    print(country)
    print("data =", data[country])
    for city, days_stayed in data[country].items():
        print("key=", city, "value=", days_stayed)
        if days_stayed <= 5:
            # cities_only_5_days[country] = [city]
            if country not in cities_only_5_days:
                cities_only_5_days[country] = list()
            cities_only_5_days[country].append(city)

print(cities_only_5_days)



list_of_city_names = []
duplicate_city_names = dict()  # country and the city

for country in data:
    for city in data[country].keys():
        if city in list_of_city_names:
            # this is a duplicate value
            duplicate_city_names[country] = city  # store the latest country with duplicate value
        list_of_city_names.append(city)

print(duplicate_city_names)

