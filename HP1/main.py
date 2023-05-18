from features.searchFeature import *
from features.commonFeature import *
from features.auth import *
import helper.constant as constant

def showMenu():
    print("\n\t\t\tHuman Resources Management in School")
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
            addNew()
        case 2:
            delete()
        case 3:
            update()
        case 4:
            show()
        case 5:
            showAll()
        case 6:
            addNew(constant.teachersDb)
        case 7:
            delete(constant.teachersDb)
        case 8:
            update(constant.teachersDb)
        case 9:
            show(constant.teachersDb)
        case 10:
            showAll(constant.teachersDb)
        case 11:
            search()
        case 0:
            print('Goodbye!!!')
            exit()
    input("Press Enter to back Menu...\n")

def solveLoginSelection():
    while 1:
        result = login()

        if result:
            while 1:
                showMenu()
                determineSelection(getSelection(0, 11))
        else:
            print("Login Fail!!! Try again !!!")
def main():
    print("\n\t\t\tStudent Management System")
    print("\t-------------------------------------------------\t")
    print("/*\t1. Login\t\t\t\t\t*/")
    print("/*\t2. Sign Up\t\t\t\t\t*/")
    print("/*\t0. Exit\t\t\t\t\t\t*/")
    print("\t-------------------------------------------------\t")
    
    selection = getSelection(0, 2)
    if selection == 1:
        solveLoginSelection()
    elif selection == 2:
        result = signUp()
        if result:
            main()
    elif selection == 0:
        exit()

if __name__ == "__main__":
    main()