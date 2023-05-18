from helper.validate import *
import helper.constant as constant

class Person():
    def __init__(self, fName, lName, grade, sex) -> None:
        self.fName = fName
        self.lName = lName
        self.grade = grade
        self.sex = sex

    def configId(self):
        raise NotImplementedError()
    def toString(self):
        raise NotImplementedError()

class Student(Person):
    def __init__(self, fName, lName, grade, sex):
        super().__init__(fName, lName, grade, sex)
        self.id = str(grade) + sex.upper() + "STU"

    def configId(self, id):
        id += 1
        self.id += str(id)

    def toString(self):
        return "{0}-{1}-{2}-{3}-{4}\n".format(self.id, self.fName, self.lName, self.grade, "Female" if self.sex == "f" else "Male")

class Teacher(Person):
    def __init__(self, fName, lName, grade, sex, isGraduated, school):
        super().__init__(fName, lName, grade, sex)
        self.isGraduated = isGraduated
        self.school = school
        self.id = str(grade) + sex.upper() + "TEA"

    def configId(self, id):
        id += 1
        self.id += str(id)

    def toString(self):
        return "{0}-{1}-{2}-{3}-{4}-{5}-{6}\n".format(self.id, self.fName, self.lName, self.grade, "Female" if self.sex == "f" else "Male", "True" if self.isGraduated else "False", self.school)
    
class Account():
    def __init__(self, userName, passWord) -> None:
        self.userName = userName
        self.passWord = passWord

def getGeneralInformation(db = constant.studentsDb):
    obj = determineTextToShow(db)

    fName = getString(f"First Name's {obj}: ")
    lName = getString(f"Last Name's {obj}: ")
    grade = getNumber(f"Class's {obj} (Valid value from 1 -> 12)", 1, 12)
    sex = getByOption(f"Sex's {obj}: Female (f) or Male (m): ", ["f", "m"])

    return (fName, lName, grade, sex)

def getSelection(optionMin, optionMax):
    return getNumber(f"Your choice (Valid value from {optionMin} -> {optionMax}): ", optionMin, optionMax)

def handleStundetInDB(action, data, db = constant.studentsDb):
    if action == "add" :
        with open(db, "r+") as f:
            idLast = ""
            all = f.readlines()
            if len(all) == 0:
                idLast = 999
            else:
                txtSplit = "STU" if db == constant.studentsDb else "TEA"
                idLast = int(all[-1].split("-")[0].split(txtSplit)[1])

            data.configId(idLast)
            f.writelines(data.toString())

            return True
        
    if action == "del":
        with open(db, "r") as f:
            all = f.readlines()
            filtered = [student for student in all if all.index(student) != data]
            with open(db, 'w') as filedata:
                filedata.writelines(filtered)

            return True
        
    if action == "upd":
        with open(db, "r") as f:
            all = f.readlines()
            obj = determineTextToShow(db)
            info = getGeneralInformation(obj)
            id = all[data].split("-")[0] # get id

            newObj = id + "-" + info[0] + "-" + info[1] + "-" + str(info[2]) + "-" 
            newObj += "Female" if info[3] == "f" else "Male"

            if db == constant.teachersDb:
                isGraduated = True if getByOption("You have been graduated? (y/n): ", ['y','n']) == "y" else False
                school = getString("Your school: ")
                newObj += "-True" if isGraduated else "-False"
                newObj += "-" + school

            newObj += "\n"
            all[data] = newObj
            with open(db, 'w') as filedata:
                filedata.writelines(all)

            return True
        
    if action == "get":
        with open(db, "r") as f:
            all = f.readlines()

            return all[data]
        
    return False

def readFiles(fileName = constant.studentsDb):
    with open(fileName, "r") as file:
        return file.readlines()

def getAccounts():
    return [Account(account.split(",")[0], account.split(",")[1].replace("\n", "")) for account in readFiles(constant.accountsDb)]

def getIds(db = constant.studentsDb):
    return [student.split("-")[0] for student in readFiles(db)]

def chooseObjToAction(db = constant.studentsDb):
    ids = getIds() if db == constant.studentsDb else getIds(constant.teachersDb)
    idsString = ", ".join(ids)

    txt = determineTextToShow(db)
    print(f"All ID of {txt} in DB: {idsString}")

    while 1:
        id = getString("Choose one of these ID to delete? Your choose: ")

        if id not in ids:
            print("ID input was not matching with each other!!! Try again!!!\n")
        else:
            return ids.index(id)
        
def determineTextToShow(db = constant.studentsDb):
    return constant.student if db == constant.studentsDb else constant.teacher

def determineWhatTypeOfObject(typeOfDb):
    return constant.studentsDb if typeOfDb == constant.studentsDb else constant.teachersDb

def noticeResult(type, result):
    return type + " Successfully" if result else " Failure"