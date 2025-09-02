import os
from tkinter import *
from tkinter import messagebox

main = Tk()
main.geometry("1366x768")
main.title("Big Bazaar")
main.resizable(0, 0)
def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()
        
main.protocol("WM_DELETE_WINDOW", Exit)

def emp():
    main.withdraw()
    os.system("python employee.py")
    main.deiconify()


def adm():
    main.withdraw()
    os.system("python admin.py")
    main.deiconify()

import tkinter as tk
import webbrowser

def open_website():
    webbrowser.open("https://totalchaos.online")


# Background image
bg_img = PhotoImage(file="./images/main.png")
label_bg = Label(main, image=bg_img)
label_bg.place(relx=0, rely=0, width=1366, height=768)

# Transparent PNG (for later)
admin_logo = PhotoImage(file="./images/adminlogo.png")
emp_logo = PhotoImage(file="./images/emplogo.png")
support_logo = PhotoImage(file="./images/supportlogo.png")
about_logo = PhotoImage(file="./images/aboutlogo.png")

# BUTTONS (initially with border for alignment)
button1 = Button(main, image=admin_logo, command=adm, cursor="hand2",
                 borderwidth=0, highlightthickness=0, relief="solid", bg="red")  # temporary visible border
button1.place(x=460, y=300, width=180, height=110)


button2 = Button(main, image=emp_logo, command=emp, cursor="hand2",
                 borderwidth=0, highlightthickness=0, relief="solid", bg="blue")  # temporary visible border
button2.place(x=720, y=300, width=180, height=110)

button3 = Button(main, image=support_logo, command=emp, cursor="hand2",
                 borderwidth=0, highlightthickness=0, relief="solid", bg="blue")  # temporary visible border
button3.place(x=460, y=460, width=180, height=110)


button4 = Button(main, image=about_logo, command=open_website, cursor="hand2",
                 borderwidth=0, highlightthickness=0, relief="solid", bg="blue")  # temporary visible border
button4.place(x=720, y=460, width=180, height=110)


main.mainloop()