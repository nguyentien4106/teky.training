from tkinter import *
import helpers.constant as constant
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

def showTextBox(gui, width = 3, height = 1, font = constant.defaultFont, x = 0, y = 0, side=None, padx=0, pady=0):
    text = Text(gui, font=font, width=width, height=height)
    text.place(x=x, y=y)

def setWindow(gui : Tk, geometry, minWidth, minHeight, maxWidth, maxHeight):
    gui.geometry(geometry)
    gui.maxsize(maxWidth, maxHeight)
    gui.minsize(minWidth, minHeight)

def renderRow(root, side=TOP, fill="x", anchor="c"):
    row = Frame(root,  borderwidth=2, relief="solid")
    row.pack(side=side, fill=fill, anchor=anchor)
    
    return row

def renderLabel(root, text, font = "Times 11", width = 15, height = 1, anchor="center", side=LEFT, padx=0, pady=0):
    label = Label(root, text=text, font=font, width=width, height=height, anchor=anchor, borderwidth=2)
    label.pack(side=side, padx=padx, pady=pady)

def renderEntry(root, font = "Times 11", width = 30, side=LEFT, padx=0, pady=0, fill='x'):
    entry = Entry(root, width=width, font=font) #Create input boxes
    entry.pack(side=side, padx=padx, pady=pady, fill=fill)

    return entry