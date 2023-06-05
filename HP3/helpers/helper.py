from tkinter import *
import helpers.constant as constant
from pathlib import Path

class Account():
    def __init__(self, userName, passWord) -> None:
        self.userName = userName
        self.passWord = passWord

def showLabel(gui, text, font = constant.defaultFont, x = 0, y = 0, width = 50, height = 1, side=None, padx = 0, pady=0, anchor="center", input=None):
    label = Label(gui, text=text, font=font, width=width, height=height, anchor=anchor)
    if side:
        if input:
            input.pack()
            label.pack(side=side, padx=padx, pady=pady, before=input)
        else:
            label.pack(side=side, padx=padx, pady=pady)
    else:
        label.place(x=x, y=y)
    
    return input

def showButton(gui, text, width = 3, command = None, font = constant.defaultFont, x = 0, y = 0, side=None, padx=0, pady=0):
    button = Button(gui, text=text, font=font, width=width, command=command)
    button.place(x=x, y=y)
    if side:
        button.pack(side=side, padx=padx, pady=pady)

def setWindow(gui : Tk, title, geometry, minWidth, minHeight, maxWidth, maxHeight):
    gui.geometry(geometry)
    gui.maxsize(maxWidth, maxHeight)
    gui.minsize(minWidth, minHeight)
    gui.title(title)

def readFiles(fileName = constant.studentsDb):
    path = Path(__file__).parent.absolute().parent.absolute().joinpath(fileName)

    with open(path, "r") as file:
        return file.readlines()

def getAccounts():
    return [Account(account.split(",")[0], account.split(",")[1].replace("\n", "")) for account in readFiles(constant.accountsDb)]



def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()