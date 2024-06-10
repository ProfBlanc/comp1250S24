"""
Dictionary
    looking up a word => find out definition
    Look at the First letter
        Point to the full word

    The first letter of a word
        a reference (key)

    This reference points to a value
        word definition

    Prof ask you for your firstname
        Asking you to research my personal dictionary
            find the value that represents your firstname
                output this value to me

    Dictionary is a key-value pair of information
"""

personal_data = {
    "firstname": "Ben",
    "lastname": "Blanc",
    "age": 20,
    "fav_internal_temperature": 22.5
}

# dictionary keys = index
# keys mostly string values
# keys could be any immutable data type
# values are any data type

print(personal_data["firstname"])  # Ben
print(personal_data["age"])  # 20
print(len(personal_data))
personal_data['fav_programming_language'] = "python"
print(len(personal_data))

personal_data['firstname'] = "Benny"
print(personal_data["firstname"])

personal_data['combined'] = personal_data['age'] + personal_data['fav_internal_temperature']

print(personal_data)

d2 = {"first": 1, "second": 2.2}
d3 = d2.copy()
personal_data.update(d2)

print(personal_data)

class_schedule = {
    "monday": {"11am": "python lecture", "4pm": "python lab"},
    "tuesday": ["network", "business"]
}
print(class_schedule["monday"]["11am"])
print(class_schedule["tuesday"][1])