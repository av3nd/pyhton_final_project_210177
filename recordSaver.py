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

# data frame
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x",expand="yes",padx=20)

# functions
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row),my_tree.index(row)-1)

def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row,my_tree.parent(row),my_tree.index(row)+1)

# inside data frame
fn_label = Label(data_frame, text="First Name")
fn_label.grid(row=0,column=0,padx=10,pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0,column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Last Name")
ln_label.grid(row=0,column=2,padx=10,pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0,column=3, padx=10, pady=10)

id_label = Label(data_frame, text="ID")
id_label.grid(row=0,column=4,padx=10,pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0,column=5, padx=10, pady=10)

address_label = Label(data_frame, text="Address")
address_label.grid(row=1,column=0,padx=10,pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1,column=1, padx=10, pady=10)

city_label = Label(data_frame, text="City")
city_label.grid(row=1,column=2,padx=10,pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1,column=3, padx=10, pady=10)

state_label = Label(data_frame, text="State")
state_label.grid(row=1,column=4,padx=10,pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1,column=5, padx=10, pady=10)

zipcode_label = Label(data_frame, text="Zipcode")
zipcode_label.grid(row=1,column=6,padx=10,pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=1,column=7, padx=10, pady=10)

# Button frame
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill='x',expand="yes",padx=20)

update_button = Button(button_frame,text="Update")
update_button.grid(row=0,column=0,padx=10,pady=10)

add_button = Button(button_frame,text="Add")
add_button.grid(row=0,column=1,padx=10,pady=10)

delete_button = Button(button_frame,text="Delete")
delete_button.grid(row=0,column=2,padx=10,pady=10)

move_up_button = Button(button_frame,text="Move Up",command=up)
move_up_button.grid(row=0,column=3,padx=10,pady=10)

move_down_button = Button(button_frame,text="Move Down",command=down)
move_down_button.grid(row=0,column=4,padx=10,pady=10)

clear_record_button = Button(button_frame,text="Clear Entry Boxes")
clear_record_button.grid(row=0,column=5,padx=10,pady=10)

search_record_button = Button(button_frame,text="Search Record")
search_record_button.grid(row=0,column=6,padx=10,pady=10)



root.mainloop()