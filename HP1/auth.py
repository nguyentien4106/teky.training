from helper import *
import pwinput
import constant

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

    with open(constant.accountsDb, "a") as file:
        file.write(f"\n{userName},{passWord1}")
        return True