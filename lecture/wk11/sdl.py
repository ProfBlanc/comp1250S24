import os
import sys

"""
This application will allow a user to CRUD files and folders to organize a Student Directory Listing

User will be able to create a school, year,  semester, course AND add student firstname, lastname and student id to a specific course
"""

def ask_for_semester():
    school = input("Enter school: ")
    year = input("Enter year: ")
    semester = input("Enter semester: ")

    return school, year, semester
def create_course():
    school, year, semester = ask_for_semester()
    # create folders school/year/semester
       # georgebrown/2024/summer

    if not os.path.exists(f"sdl/{school}/{year}/{semester}"):
        os.makedirs(f"sdl/{school}/{year}/{semester}")

    course = input("Enter course: ")
    os.mkdir(f"sdl/{school}/{year}/{semester}/{course}")

def edit_course():
    school, year, semester = ask_for_semester()
    ocourse = input("Enter the old course name: ")
    ncourse = input("Enter new course name")

    if os.path.exists(f"sdl/{school}/{year}/{semester}/{ocourse}"):
        os.rename(f"sdl/{school}/{year}/{semester}/{ocourse}", f"sdl/{school}/{year}/{semester}/{ncourse}")
    else:
        print("The course", ocourse, "was not found", file=sys.stderr)  # text = red

def ask_for_student_info():
    student_id = input("Enter student ID: ")
    student_first_name = input("Enter student first name: ")
    student_last_name = input("Enter student last name: ")

    return student_id, student_first_name, student_last_name

def add_student():
    school, year, semester = ask_for_semester()
    course = input("Enter course: ")

    student_id, student_first_name, student_last_name = ask_for_student_info()

    path = f"sdl/{school}/{year}/{semester}/{course}/{student_id}.txt"

    file = open(path, "w")
    file.write(student_first_name + "\n")
    file.write(student_last_name + "\n")
    file.close()



def edit_student():
    school, year, semester = ask_for_semester()
    course = input("Enter course: ")

    student_id = input("Enter student id that you would like to overwrite: ")
    path = f"sdl/{school}/{year}/{semester}/{course}/{student_id}.txt"
    if os.path.exists(path):
        n_student_fn = input("Enter new student first name: ")
        n_student_ln = input("Enter new student last name: ")
        with open(path, "r+") as file:
            lines = file.readlines()  # ['firstname\n', 'lastname\n']

            new_content = [n_student_fn + "\n", n_student_ln + '\n']
            file.seek(0)
            file.writelines(new_content)




def delete_student():
    school, year, semester = ask_for_semester()
    course = input("Enter course: ")

    student_id = input("Enter student id that you would like to delete: ")
    path = f"sdl/{school}/{year}/{semester}/{course}/{student_id}.txt"
    if os.path.exists(path):
        os.remove(path)
    else:
        print("Cannot delete student with id", student_id)

def view_all_courses():
    school, year, semester = ask_for_semester()

    courses = os.listdir(f"sdl/{school}/{year}/{semester}")
    print("Here are the courses")
    for course in courses:
        print(course)

def view_all_students():
    school, year, semester = ask_for_semester()
    course = input("Enter course: ")
    path = f"sdl/{school}/{year}/{semester}/{course}"

    students = os.listdir(path)
    print("Here are the student")
    for student_id in students:
        just_student_id = student_id.split(".txt")[0]
        print(just_student_id)
        content = open(path + "/" + student_id).readlines()
        print("".join(content))




def main():
    print("Welcome to our SDL application")
    print("What would you like to do?")

    choice = input("1)Create course\n2)Edit Course\n3)Add Student to Course\n4)Edit Student Info\n5)Delete Student\n6)View all Courses\n7)View all Students\n8)Exit Program\nEnter choice: ")

    match choice:
        case "1":
            create_course()
        case "2":
            edit_course()
        case "3":
            add_student()
        case "4":
            edit_student()
        case "5":
            delete_student()
        case "6":
            view_all_courses()
        case "7":
            view_all_students()
        case _:  # default case/ no other case applies
            print("End of program")


if __name__ == "__main__":
    main()