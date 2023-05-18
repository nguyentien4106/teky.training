from validate import *

class Person():
    def __init__(self, fName, lName, sex) -> None:
        self.fName = fName
        self.lName = lName
        self.sex = sex

    def configId(self):
        raise NotImplementedError()
    def toString(self):
        raise NotImplementedError()

class Student(Person):
    def __init__(self, fName, lName, grade, sex):
        super().__init__(fName, lName, sex)
        self.grade = grade
        self.id = str(grade) + sex.upper() + "STU"

    def configId(self, id):
        id += 1
        self.id += str(id)

    def toString(self):
        return "{0}-{1}-{2}-{3}-{4}\n".format(self.id, self.fName, self.lName, self.grade, "Female" if self.sex == "f" else "Male")

class Teacher(Person):
    def __init__(self, fName, lName, grade, sex, isGraduated, school):
        super().__init__(fName, lName, sex)
        self.grade = grade
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

    def toString(self):
        return self.userName + " " + self.passWord

def getGeneralInformation(obj = "Student"):
    fName = getString(f"First Name's {obj}: ")
    lName = getString(f"Last Name's {obj}: ")
    grade = getNumber(f"Class's {obj}: from 1 -> 12 ", 1, 12)
    sex = getByOption(f"Sex's {obj}: Female (f) or Male (m): ", ["f", "m"])

    return (fName, lName, grade, sex)

def getSelection(optionMin, optionMax):
    return getNumber("Your choose is: ", optionMin, optionMax)

def handleStundetInDB(action, data, db = "db/students.txt"):
    if action == "add" :
        with open(db, "r+") as f:
            idLast = ""
            all = f.readlines()
            if len(all) == 0:
                idLast = 999
            else:
                txtSplit = "STU" if db == "db/students.txt" else "TEA"
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
            obj = "Student" if db == "db/students.txt" else "Teacher"
            info = getGeneralInformation(obj)
            id = all[data].split("-")[0] # get id
            newObj = id + "-" + info[0] + "-" + info[1] + "-" + str(info[2]) + "-" 
            newObj += "Female" if info[3] == "f" else "Male"

            if db == "db/teachers.txt":
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

def readFiles(fileName = "db/students.txt"):
    with open(fileName, "r") as file:
        return [ line for line in file ]

def getAccounts():
    return [Account(account.split(",")[0], account.split(",")[1].replace("\n", "")) for account in readFiles("db/accounts.txt")]

def getIds(db = "db/students.txt"):
    return [student.split("-")[0] for student in readFiles(db)]

def chooseStudentToAction(obj = "Student"):
    ids = getIds() if obj == "Student" else getIds("db/teachers.txt")
    idsString = ", ".join(ids)
    print(f"All ID of {obj} in DB: {idsString}")
    while 1:
        id = getString("Choose one of these ID to delete? Your choose: ")

        if id not in ids:
            print("No matching ID")
        else:
            return ids.index(id)
        