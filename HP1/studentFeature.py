from helper import *
from validate import *
from tabulate import tabulate
import pwinput

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

def login():
    userName = getString("Please input username: ")
    passWord = pwinput.pwinput(prompt='Password: ')
    for account in getAccounts():
        if userName == account.userName and passWord == account.passWord:
            return True
    
    print("Username or password incorrect!!!")
    return False

def signUp():
    userName = getString("Please input username: ")
    passWord1 = pwinput.pwinput(prompt='Password: ')
    passWord2 = pwinput.pwinput(prompt='Re-Password: ')

    while passWord1 != passWord2:
        print("Your password was not matching !!! Please try again !!!\n")
        passWord1 = pwinput.pwinput(prompt='Password: ')
        passWord2 = pwinput.pwinput(prompt='Re-Password: ')

    with open("db/accounts.txt", "a") as file:
        file.write(f"\n{userName},{passWord1}")
        return True