from studentFeature import *
from teacherFeature import *
from searchFeature import search

def showMenu():
    print("\n\t\t\tStudent Management System")
    print("\t-------------------------------------------------\t")
    print("/*\t1. Add Stundent\t\t\t\t\t*/")
    print("/*\t2. Delete Student\t\t\t\t*/")
    print("/*\t3. Update Student\t\t\t\t*/")
    print("/*\t4. Information's Student\t\t\t*/")
    print("/*\t5. All Students\t\t\t\t\t*/")
    print("/*\t6. Add Teacher\t\t\t\t\t*/")
    print("/*\t7. Delete Teacher\t\t\t\t*/")
    print("/*\t8. Update Teacher\t\t\t\t*/")
    print("/*\t9. Information's Teacher\t\t\t*/")
    print("/*\t10. All Teachers\t\t\t\t*/")
    print("/*\t11. Search\t\t\t\t\t*/")
    print("/*\t0. Exit\t\t\t\t\t\t*/")
    print("\t-------------------------------------------------\t")

def determineSelection(selection):
    match selection:
        case 1:
            addNewStudent()
        case 2:
            deleteStudent()
        case 3:
            updateStudent()
        case 4:
            showInfo()
        case 5:
            showAllStudents()
        case 6:
            addNewTeacher()
        case 7:
            deleteTeacher()
        case 8:
            updateTeacher()
        case 9:
            showInfoTeacher()
        case 10:
            showAllTeachers()
        case 11:
            search()
        case 0:
            print('Goodbye!!!')
            exit()
    input("Press any key to back Menu...")

def start():
    print("\n\t\t\tStudent Management System")
    print("\t-------------------------------------------------\t")
    print("/*\t1. Login\t\t\t\t*/")
    print("/*\t2. Sign Up\t\t\t\t\t*/")
    print("/*\t0. Exit\t\t\t\t\t\t*/")
    print("\t-------------------------------------------------\t")
    selection = getSelection(0, 2)
    if selection == 0:
        exit()
    elif selection == 1:
        login()
    else:
        signUp()

def main():
    print("\n\t\t\tStudent Management System")
    print("\t-------------------------------------------------\t")
    print("/*\t1. Login\t\t\t\t\t*/")
    print("/*\t2. Sign Up\t\t\t\t\t*/")
    print("/*\t0. Exit\t\t\t\t\t\t*/")
    print("\t-------------------------------------------------\t")
    selection = getSelection(0, 2)
    if selection == 0:
        exit()
    elif selection == 1:
        result = login()

        if result:
            while 1:
                showMenu()
                determineSelection(getSelection(0, 11))
    else:
        res = signUp()
        if res:
            main()

if __name__ == "__main__":
    main()