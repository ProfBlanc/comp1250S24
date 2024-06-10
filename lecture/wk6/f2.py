"""
A set is used if
    store unique values
    use set operations
        compare, differentiate, combine, etc

            union, difference, symetrical difference, intersection

            1) common values (intersection)
            2) values in set 1 but not in set 2 (difference)
            3) values not in both sets (symetrical difference)
            4) combine values



    do not need to store a list value


"""
test = list("benny")  # list ['b','e','n'...]

letters1 = set("benny")  # how many values stored in letters1?
print(len(letters1))  # 4
letters2 = set("blancb")  # how many values stored in letters2? 5

common_letters_in_first_last_name = letters1.intersection(letters2)

print(common_letters_in_first_last_name)

unique_letters_in_first_last_name = letters1.union(letters2)
print(unique_letters_in_first_last_name)

s1 = {"hi", "bye"}
s2 = {"dry", "cry"}

s1.update(s2)

s1.intersection_update(s2)

print(s1)
