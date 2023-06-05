# Import the Tkinter library
from tkinter import *
from views.authView import *
from helpers.helper import *
gui = Tk(className="Human Resources Management in School")
setWindow(gui, "Human Resources Management in School", "950x600", 850, 550, 950, 600)

center(gui)

showLoginPage(gui)

gui.mainloop()