from helper import *
from validate import *
from tabulate import tabulate
import constant

def addNew(db = constant.studentsDb):
    info = getGeneralInformation(determineWhatTypeOfObject(db))
    if db == constant.studentsDb:
        newObj = Student(info[0], info[1], info[2], info[3])
    else:
        isGraduated = True if getByOption("You have been graduated? (y/n): ", ['y','n']) == "y" else False
        school = getString("Your school: ")
        newObj = Teacher(info[0], info[1], info[2], info[3], isGraduated, school)

    result = handleStundetInDB('add', newObj, db)
    print(noticeResult(constant.added, result))

def delete(db = constant.studentsDb):
    result = handleStundetInDB("del", chooseObjToAction(db), db)
    print(noticeResult(constant.deleted, result))

def update(db = constant.studentsDb):
    result = handleStundetInDB("upd", chooseObjToAction(db), db)
    print(noticeResult(constant.updated, result))

def show(db = constant.studentsDb):
    obj = handleStundetInDB("get", chooseObjToAction(db), db)
    objShow = [obj.split("-")]

    if db == constant.studentsDb:
        print(tabulate(objShow, headers=['ID', 'First Name', "Last Name", "Grade", "Sex"]))
    else:
        print(tabulate(objShow, headers=['ID', 'First Name', "Last Name", "Grade", "Sex", "Graduated", "School"]))

def showAll(db = constant.studentsDb):
    text = "All Students" if db == constant.studentsDb else "All Teachers"
    print(f"\t\t{text}")
    all = []

    for obj in readFiles(db):
        all.append(obj.split("-"))

    if db == constant.studentsDb:
        print(tabulate(all, headers=['ID', 'First Name', "Last Name", "Grade", "Sex"]))
    else:
        print(tabulate(all, headers=['ID', 'First Name', "Last Name", "Grade", "Sex", "Graduated", "School"]))

        
