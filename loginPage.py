from tkinter import *

admin = Tk()
admin.title("Login Page")
admin.geometry("305x210")
admin.iconbitmap('key.ico')
admin.config(bg="lightgrey")

admin_frame = LabelFrame(admin, text="Enter Username and Password",font=('Consolas',11))
admin_frame.place(x=1, y=0, width=302, height=205)


admin_lbl = Label(admin_frame,text="Username: ",font=('Consolas',11))
admin_lbl.grid(row=0, column=0, padx=20, pady=20)
admin_entry = Entry(admin_frame,show='*')
admin_entry.grid(row=0, column=1, padx=20, pady=20)

admin_lbl1 = Label(admin_frame,text="Password: ",font=('Consolas',11))
admin_lbl1.grid(row=1, column=0, padx=20, pady=20)
admin_entry1 = Entry(admin_frame,show='*')
admin_entry1.grid(row=1, column=1, padx=20, pady=20)

admin_button = Button(admin_frame, text="Login",font=('Consolas',11),cursor='hand2',bg="lightgrey")
admin_button.grid(row=2,column=1,padx=20,pady=20)

admin.mainloop()