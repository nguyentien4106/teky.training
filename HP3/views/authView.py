from tkinter import *
from helpers.helper import *
from services.authServices import *
from tkinter.ttk import *
import helpers.constant as constant
def renderLabelAndEntry(signUpWindow, column = 0, row = 0, text = "", isPassword = False):
    # username
    Label(signUpWindow, text=text).grid(column=column, row=row, sticky=W, padx=5, pady=5)

    username = Entry(signUpWindow, width=50, show="*") if isPassword else Entry(signUpWindow, width=50)
    username.grid(column=column + 1, row=row, sticky=W, padx=5, pady=5)
    return username

def signUpClickCommand(gui):
    signUpWindow = Toplevel(gui)
    setWindow(signUpWindow, "Sign Up", "400x120", minWidth=400, minHeight=120, maxWidth=500, maxHeight=120)
    center(signUpWindow)

    username = renderLabelAndEntry(signUpWindow, column = 0, row = 0, text = "Username")

    password1 = renderLabelAndEntry(signUpWindow, column = 0, row = 1, text = "Password", isPassword=True)

    password2 = renderLabelAndEntry(signUpWindow, column=0 , row=2, text="Re-password", isPassword=True)

    # sign button
    Button(signUpWindow, text="Submit", command= lambda: handleSignUp(signUpWindow, username.get(), password1.get(), password2.get())).grid(column=0, row=3, sticky=NSEW, columnspan=2)

    signUpWindow.grab_set()

def exitClickCommand(gui):
    gui.destroy()

def loginClickCommand(gui : tkinter.Tk):
    loginWindow = Toplevel(gui)
    setWindow(loginWindow, "Login", "400x100", minWidth=400, minHeight=100, maxWidth=400, maxHeight=100)
    center(loginWindow)
    # username
    username = renderLabelAndEntry(loginWindow, column=0, row=0, text="Username")

    # password
    password = renderLabelAndEntry(loginWindow, column=0, row=1, text="Password", isPassword=True)

    # login button
    Button(loginWindow, text="Login", command= lambda: handleLogin(gui, loginWindow, username.get(), password.get())).grid(column=0, row=3, sticky=NSEW, columnspan=2)

    loginWindow.grab_set()

def showLoginPage(gui : tkinter.Tk):
    # Create Buttons in the frame
    showLabel(gui, "Login\nUse your account to login!", font = constant.titleHeaderFont, side=TOP, pady=10, height=3)
    showButton(gui, "Login", 50, x = 300, y = 300,command=lambda : loginClickCommand(gui))
    showButton(gui, "Sign Up", 50, x = 300, y = 350, command= lambda : signUpClickCommand(gui))
    showButton(gui, "Exit", 50, x = 300, y = 400, command= lambda : exitClickCommand(gui))