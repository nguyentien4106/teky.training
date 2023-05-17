from helper import *
from validate import *
from tabulate import tabulate

def addNewStudent():
    info = getGeneralInformation()
    newStudent = Student(info[0], info[1], info[2], info[3])
    result = handleStundetInDB('add', newStudent)
    print("Added Successfully" if result == True else "Added Fail")
    
def deleteStudent():
    result = handleStundetInDB("del", chooseStudentToAction())
    print("Deleted Successfully" if result == True else "Deleted Fail")

def updateStudent():
    result = handleStundetInDB("upd", chooseStudentToAction())
    print("Deleted Successfully" if result == True else "Deleted Fail")

def showInfo():
    student = handleStundetInDB("get", chooseStudentToAction())
    students = [student.split("-")]
    print(tabulate(students, headers=['ID', 'First Name', "Last Name", "Grade", "Sex"]))

def showAllStudents():
    print("\t\tAll Students")
    students = []
    for student in readFiles("db/students.txt"):
        students.append(student.split("-"))
    print(tabulate(students, headers=['ID', 'First Name', "Last Name", "Grade", "Sex", "Courses", "Reward"]))
