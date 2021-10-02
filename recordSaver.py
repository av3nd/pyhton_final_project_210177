from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Management System')
root.geometry("1000x500")


# style for treeview
style = ttk.Style()
style.theme_use('default')

style.configure("Treeview",
    background='#D3D3D3',
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

style.map('Treeview',
          background=[('selected',"#347083")])