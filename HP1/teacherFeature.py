from helper import *
from validate import *
from tabulate import tabulate

def addNewTeacher():
    info = getGeneralInformation("Teacher")
    isGraduated = True if getByOption("You have been graduated? (y/n): ", ['y','n']) == "y" else False
    school = getString("Your school: ")
    newTeacher = Teacher(info[0], info[1], info[2], info[3], isGraduated, school)

    result = handleStundetInDB('add', newTeacher, db = "db/teachers.txt")
    print("Added Successfully" if result == True else "Added Fail")

def deleteTeacher():
    result = handleStundetInDB("del", chooseStudentToAction(obj = "Teacher"), db = "db/teachers.txt")
    print("Deleted Successfully" if result == True else "Deleted Fail")

def updateTeacher():
    result = handleStundetInDB("upd", chooseStudentToAction(obj = "Teacher"), db = "db/teachers.txt")
    print("Deleted Successfully" if result == True else "Deleted Fail")

def showInfoTeacher():
    teacher = handleStundetInDB("get", chooseStudentToAction(obj = "Teacher"), db = "db/teachers.txt")
    teachers = [teacher.split("-")]
    print(tabulate(teachers, headers=['ID', 'First Name', "Last Name", "Grade", "Sex", "isGraduated", "School"]))

def showAllTeachers():
    print("\t\tAll Teachers")
    teachers = []
    for teacher in readFiles("db/teachers.txt"):
        teachers.append(teacher.split("-"))
    print(tabulate(teachers, headers=['ID', 'First Name', "Last Name", "Grade", "Sex", "isGraduated", "School"]))
