from tkinter import Tk, Label, Entry, Button, Frame

root = Tk()
root.title("Login Information Help")
root.configure(background='black')
root.geometry("1920x1080")

def button_click(number):
    textbox.delete(0, END)
    textbox.insert(0, number)

row0 = Frame(root, bg='black')
row0.pack(side='top', fill='y', anchor='nw')

row1 = Frame(root, bg='black')
row1.pack(side='top', fill='y', anchor='nw')

row2 = Frame(root, bg='black')
row2.pack(side='top', fill='y', anchor='nw')

row3 = Frame(root, bg='black')
row3.pack(side='top', fill='y', anchor='nw')

instructions = Label(row0, text="Please fill in all information below to recieve student account details.", bg="black", fg="white", font="times, 20") #Create instructions line
first_name_text = Label(row1, text="Enter First Name", bg="black", fg="white", font="times, 20" ) #enter first name text
inputbox1 = Entry(row1, width=30, font="times, 20") #Create input boxes
last_name_text = Label(row2, text="Enter Last Name", bg="black", fg="white", font="times, 20" ) #enter last name text
inputbox2 = Entry(row2, width=30, font="Times, 20") #Create input boxes
button_1 = Button(row3, text="Get Info", padx=45, pady=5, bg="#808080", font="times, 15", command=lambda: button_click("1")) #Define Buttons

instructions.pack(side='left')
first_name_text.pack(side='left')
inputbox1.pack(side='left')
last_name_text.pack(side='left')
inputbox2.pack(side='left', padx=2)
button_1.pack(side='left')

root.mainloop()