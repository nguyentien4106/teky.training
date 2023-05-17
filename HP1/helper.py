from validate import *
import pwinput

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
        return "{0}-{1}-{2}-{3}-{4}".format(self.id, self.fName, self.lName, self.grade, "Female" if self.sex == "f" else "Male")

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
        return "{0}-{1}-{2}-{3}-{4}-{5}-{6}".format(self.id, self.fName, self.lName, self.grade, "Female" if self.sex == "f" else "Male", "True" if self.isGraduated else "False", self.school)
    
class Account():
    def __init__(self, userName, passWord) -> None:
        self.userName = userName
        self.passWord = passWord

    def toString(self):
        return self.userName + " " + self.passWord

def getGeneralInformation(obj = "Student"):
    fName = getString(f"First Name's {obj}: ")
    lName = getString(f"Last Name's {obj}: ")
    grade = getNumber(f"Class's {obj}: ", 1, 12)
    sex = getByOption(f"Sex's {obj}: Female (f) or Male (m): ", ["f", "m"])

    return (fName, lName, grade, sex)

def getSelection(optionMin, optionMax):
    return getNumber("Your choose is: ", optionMin, optionMax)

def handleStundetInDB(action, data, db = "db/students.txt"):
    if action == "add" :
        with open(db, "r+") as f:
            idLast = ""
            allStudents = f.readlines()
            if len(allStudents) == 0:
                idLast = 999
            else:
                idLast = int(allStudents[-1].split("-")[0].split("STU")[1])
            data.configId(idLast)
            f.write('\n' + data.toString())

            return True
        
    if action == "del":
        with open(db, "r") as f:
            allStudents = f.readlines()
            students = [student for student in allStudents if allStudents.index(student) != data]
            print(students)
            with open(db, 'w') as filedata:
                filedata.writelines(students)

            return True
        
    if action == "upd":
        with open(db, "r") as f:
            allStudents = f.readlines()
            student = allStudents[data]
            info = getGeneralInformation()
            id = student.split("-")[0]
            newStudent = id + "-" + info[0] + "-" + info[1] + "-" + str(info[2]) + "-" 
            newStudent += "Female" if info[3] == "f" else "Male" + "\n"
            allStudents[data] = newStudent
            with open(db, 'w') as filedata:
                filedata.writelines(allStudents)

            return True
    if action == "get":
        with open(db, "r") as f:
            allStudents = f.readlines()

            return allStudents[data]
        
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
        

def login():
    userName = getString("Please input username: ")
    passWord = pwinput.pwinput(prompt='Password: ')
    for account in getAccounts():
        if userName == account.userName and passWord == account.passWord:
            return True
    
    print("Username or password incorrect!!!")
    return False

def signUp():
    userName = getString("Please input userName: ")
    pw1 = pwinput.pwinput(prompt='Password: ')
    pw2 = pwinput.pwinput(prompt='Re-Password: ')

    while pw1 != pw2:
        print("Password was not matching!!! Try again !!!")
        pw1 = pwinput.pwinput(prompt='Password: ')
        pw2 = pwinput.pwinput(prompt='Re-Password: ')
    
    with open("db/accounts.txt", "a") as file:
        file.writelines(f"\n{userName},{pw1}")
    print("Sign Up Successfully!!!")

    return True