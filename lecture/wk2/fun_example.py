"""
Ask the user for their year of birth
Calculate how old they are in
    years
    days
    weeks

Output their age in 10 years in the future.
Output their age in dog years (7 human years = 1 dog year)
"""
birth_year = input("Enter your birth year: ")
# Question: what is the data type of birth_year?
# ANS: string

# how do we convert this to a numerical value
birth_year = int(birth_year)
# Question: what is the data type of birth_year?
# ANS: int

current_year = 2024

# calculate

age_in_years = current_year - birth_year
age_in_days = 365.25 * age_in_years
age_in_weeks = 52 * age_in_years

print("You are", age_in_years, "years old")
# use different args to print statement

# print(age_in_years + " in days is equal to " + age_in_days)
    #    int       +        str              +      int

print(str(age_in_years) + " in days is equal to " + str(age_in_days))
print(f"{age_in_years} in days is equal to {age_in_days}")