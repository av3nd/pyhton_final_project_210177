from tkinter import *
from tkinter import messagebox
import os

admin = Tk()
admin.title("Login Page")
admin.geometry("305x210")
admin.iconbitmap('key.ico')
admin.config(bg="lightgrey")

#Function
def ok():
    uname=admin_entry.get()
    password=admin_entry1.get()
    if(uname==""and password==""):
        messagebox.showinfo("Error","Blank Not Allowed")
    elif(uname=="admin"and password=="admin"):
        messagebox.showinfo("Login Success","Username and Password correct!!")
        admin.withdraw()
        os.system("recordSaver.py")


    else:
        messagebox.showinfo("Error","Incorrect Username and Password")

#Admin Frame
admin_frame = LabelFrame(admin, text="Enter Username and Password",font=('Consolas',11),bg='#b0ebea')
admin_frame.place(x=1, y=0, width=302, height=205)
# admin_frame.config(bg=#34b1eb)

#Inside Admin Frame
admin_lbl=Label(admin_frame,text="Username: ",font=('Consolas',12),bg='#b0ebea')
admin_lbl.grid(row=0, column=0, padx=15, pady=15)
admin_entry = Entry(admin_frame,show='*')
admin_entry.grid(row=0, column=1, padx=15, pady=15)

admin_lbl1 = Label(admin_frame,text="Password: ",font=('Consolas',12),bg='#b0ebea')
admin_lbl1.grid(row=1, column=0, padx=15, pady=15)
admin_entry1 = Entry(admin_frame,show='*')
admin_entry1.grid(row=1, column=1, padx=15, pady=15)

admin_button = Button(admin_frame, text="Login",font=('Consolas',11),cursor='hand2',bg="lightgrey",command=ok)
admin_button.grid(row=2,column=1,padx=20,pady=20)

admin.mainloop()