"""
grades tracker
    track your grades for each coursecode
"""

grades_tracker = {
    "comp1250": 90,
    "comp1235": 95,
    "comp1176": 92
}

grades_tracker['comp1234'] = 85

print(grades_tracker)

"""
Ask the user what course they are taking
Ask the user for their grade
If user enters a course code that already exists
    compare YOUR grade with theirs. Output
    Which person has the higher grade
If user enters a course that DOES NOT exists
    add it to grades tracker
"""
course_code = input("Enter your course code")
course_grade = int(input("Enter the grade for "
                       + course_code + ": "))

if course_code in grades_tracker:
    print("We are taking the same course")

if course_grade in grades_tracker.values():
    print("We have a common grade")

if course_code not in grades_tracker.keys():
    print("Adding this course code - grade combo to our dictionary")
    grades_tracker[course_code] = course_grade
else:
    who = "I" if grades_tracker[course_code] >= course_grade else "You"
    print(who, "have the highest grade for", course_code)

for data in grades_tracker.items():  # .keys(), .values(), .items()=> tuple of key-value pair
    print(data)
