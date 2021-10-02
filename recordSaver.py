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

# frame for treeview
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# scroll bar for treeview
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

# create tree view
my_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll,selectmode = "extended")
my_tree.pack()

tree_scroll.config(command=my_tree.yview)
my_tree['columns']=("First Name","Last Name","ID","Address","City","State","Zipcode")

# Format the column
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("First Name",anchor=W,width=140)
my_tree.column("Last Name",anchor=W,width=140)
my_tree.column("ID",anchor=CENTER,width=100)
my_tree.column("Address",anchor=CENTER,width=140)
my_tree.column("City",anchor=CENTER,width=140)
my_tree.column("State",anchor=CENTER,width=140)
my_tree.column("Zipcode",anchor=CENTER,width=140)

# Create headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name",anchor=W)
my_tree.heading("Last Name", text="Last Name",anchor=W)
my_tree.heading("ID", text="ID",anchor=CENTER)
my_tree.heading("Address", text="Address",anchor=CENTER)
my_tree.heading("City", text="City",anchor=CENTER)
my_tree.heading("State", text="State",anchor=CENTER)
my_tree.heading("Zipcode", text="Zipcode",anchor=CENTER)

# Create Striped Row Tags
my_tree.tag_configure('oddrow',background="white")
my_tree.tag_configure('evenrow',background="lightblue")