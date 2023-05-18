from helper.helper import *
from tabulate import tabulate
import helper.constant as constant

def search():
    print("\n\t\tChoose Your Search Function!!!")
    print("\t-------------------------------------------------\t")
    print("/*\t1. Search By Name\t\t\t\t*/")
    print("/*\t2. Search By Grade\t\t\t\t*/")
    print("/*\t3. Search By All\t\t\t\t*/")
    print("/*\t0. Exit\t\t\t\t\t\t*/")
    print("\t-------------------------------------------------\t")

    selection = getSelection(0, 3)

    if selection == 1:
        searchByName()
    elif selection == 2:
        searchByGrade()
    elif selection == 3:
        searchByAll()
    else:
        exit()

def searchByName():
    name = getString("What name do you wanna search ? ")
    students = readFiles()
    teachers = readFiles(constant.teachersDb)
    studentsFilter = list(filter(lambda student: name in student.split("-")[1] or name in student.split("-")[2], students))
    studentFilterShow = list(map(lambda student: student.split("-"), studentsFilter))
    teachersFilter = list(filter(lambda teacher: name in teacher.split("-")[1] or name in teacher.split("-")[2], teachers))
    teachersFilterShow = list(map(lambda teacher: teacher.split("-"), teachersFilter))

    print("\t\t\tStudents")
    print(tabulate(studentFilterShow, headers=['ID', 'First Name', "Last Name", "Grade", "Sex"]))
    print("\t\t\tTeachers")
    print(tabulate(teachersFilterShow, headers=['ID', 'First Name', "Last Name", "Grade", "Sex", "Graduated", "School"]))


def searchByGrade():
    grade = getNumber("What grade do you wanna search ? ", 1, 12)
    students = readFiles()
    teachers = readFiles(constant.teachersDb)
    studentsFilter = list(filter(lambda student: grade == int(student.split("-")[3]), students))
    studentFilterShow = list(map(lambda student: student.split("-"), studentsFilter))
    teachersFilter = list(filter(lambda teacher: grade == int(teacher.split("-")[3]), teachers))
    teachersFilterShow = list(map(lambda teacher: teacher.split("-"), teachersFilter))

    print("\t\t\tStudents")
    print(tabulate(studentFilterShow, headers=['ID', 'First Name', "Last Name", "Grade", "Sex"]))

    print("\t\t\tTeachers")
    print(tabulate(teachersFilterShow, headers=['ID', 'First Name', "Last Name", "Grade", "Sex", "Graduated", "School"]))

def searchByAll():
    value = getString("Which value to search ? ")
    students = readFiles()
    teachers = readFiles(constant.teachersDb)
    studentsFilter = list(filter(lambda student: lambdaFunction(student, value), students))
    studentFilterShow = list(map(lambda student: student.split("-"), studentsFilter))
    teachersFilter = list(filter(lambda teacher: lambdaFunction(teacher, value), teachers))
    teachersFilterShow = list(map(lambda teacher: teacher.split("-"), teachersFilter))

    print("\t\t\tStudents")
    print(tabulate(studentFilterShow, headers=['ID', 'First Name', "Last Name", "Grade", "Sex"]))

    print("\t\t\tTeachers")
    print(tabulate(teachersFilterShow, headers=['ID', 'First Name', "Last Name", "Grade", "Sex", "Graduated", "School"]))


def lambdaFunction(student, value):
    result = []
    for element in student.split("-") :
        if value in element:
            result.append(student)
            break
    return result

