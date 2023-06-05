from tkinter import messagebox
import helpers.constant as constant
from helpers.helper import *
from pathlib import Path
import tkinter

def handleSignUp(root : tkinter.Tk, userName, password, password1):
    path = Path(__file__).parent.absolute().parent.absolute().joinpath(constant.accountsDb)
    if not password or not password1:
        messagebox.showerror("Error", "Fill all field please !!!")
        return False
    
    if password != password1:
        messagebox.showerror("Error", "Password wasn't matching !!!")
        return False

    with open(path, "a") as file:
        file.write(f"\n{userName},{password1}")
        messagebox.showinfo("Successfully", "Sign Up Successfully !")
        root.destroy()
        return True
    
def handleLogin(gui, loginWindow: tkinter.Tk, userName, password):
    for account in getAccounts():
        if userName == account.userName and password == account.passWord:
            loginWindow.destroy()

            mainMenu = Tk(className="Human Resources Management in School")
            setWindow(mainMenu, "Main Menu","950x600", 850, 550, 950, 600)

            showMainMenu(mainMenu)
            
            gui.destroy()
            mainMenu.mainloop()
            
            return True

    messagebox.showerror("Error", 'Username or password is incorrect !!!')
    return False