from tkinter import *
from helpers.helper import *
import helpers.constant as constant

def signUpClickCommand(gui):
    signUpWindow = Toplevel(gui)
    # signUpWindow.maxsize(500, 300)
    # signUpWindow.minsize(400, 200)
    # signUpWindow.geometry("500x300")
    
    showLabel(signUpWindow, "Sign Up", font = constant.titleHeaderFont, side = TOP, pady=0, height=1)

    #row = renderRow(signUpWindow)
    row = Frame(signUpWindow, relief=SOLID, borderwidth=2)
    row.pack()
    renderLabel(row, "Username", side=LEFT, padx=10, pady=50)
    renderEntry(row, side=LEFT, padx=10, pady=50)

    row1 = renderRow(signUpWindow)
    renderLabel(row1, "Username", side=LEFT, padx=10, pady=50)
    renderEntry(row1, side=LEFT, padx=10, pady=50)

def exitClickCommand(gui):
    gui.destroy()

def showLoginPage(gui):
    # Create Buttons in the frame
    showLabel(gui, "Login\nUse your account to login!", font = constant.titleHeaderFont, side=TOP, pady=10, height=3)

    showButton(gui, "Login", 50, x = 300, y = 300,command=None)
    showButton(gui, "Sign Up", 50, x = 300, y = 350, command= lambda : signUpClickCommand(gui))
    showButton(gui, "Exit", 50, x = 300, y = 400, command= lambda : exitClickCommand(gui))