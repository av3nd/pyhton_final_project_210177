from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

root = Tk()
root.title('Customer Record Saver')
root.geometry("1000x500")
root.config(bg="lightgrey")
root.iconbitmap('record_saver.ico')

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

# connecting to database
conn = sqlite3.connect('tree_crm.db')
c = conn.cursor()
c.execute("""CREATE TABLE if not exists customers (
    first_name text,
    last_name text,
    id integer,
    address text,
    city text,
    state text,
    zipcode text
)
""")
conn.commit()
conn.close()

# functions
def query_database():
    conn = sqlite3.connect('tree_crm.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    records = c.fetchall()

    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='',index='end',iid=count,text='',values=(record[1],record[2],record[0],record[4],record[5],record[6],record[7]),tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',values=(record[1], record[2], record[0], record[4], record[5], record[6],record[7]),tags=('oddrow',))
        count+=1

    conn.commit()
    conn.close()


def add_record():

    conn = sqlite3.connect('tree_crm.db')
    c = conn.cursor()

    c.execute("INSERT INTO customers VALUES (:first,:last,:id,:address,:city,:state,:zipcode)",
        {
            'first': fn_entry.get(),
            'last': ln_entry.get(),
            'id':id_entry.get(),
            'address': address_entry.get(),
            'city' : city_entry.get(),
            'state': state_entry.get(),
            'zipcode': zipcode_entry.get(),

        })

    conn.commit()
    conn.close()

    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)

    my_tree.delete(*my_tree.get_children())
    query_database()
    messagebox.showinfo("Added!", "Selected record is added sucessfully")

def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row),my_tree.index(row)-1)

def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row,my_tree.parent(row),my_tree.index(row)+1)

def clear_entries():
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)

def select_record(e):
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    id_entry.delete(0,END)
    address_entry.delete(0,END)
    city_entry.delete(0,END)
    state_entry.delete(0,END)
    zipcode_entry.delete(0,END)

    # select row in treeview
    selected = my_tree.focus()
    values = my_tree.item(selected,'values')

    # put the select row in entry boxes
    fn_entry.insert(0,values[0])
    ln_entry.insert(0,values[1])
    id_entry.insert(0,values[2])
    address_entry.insert(0,values[3])
    city_entry.insert(0,values[4])
    state_entry.insert(0,values[5])
    zipcode_entry.insert(0,values[6])

# data frame
data_frame = LabelFrame(root, text="Record",font=('Consolas',11))
data_frame.pack(fill="x",expand="yes",padx=20)

# inside data frame
fn_label = Label(data_frame, text="First Name",font=('Consolas',11))
fn_label.grid(row=0,column=0,padx=10,pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0,column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Last Name",font=('Consolas',11))
ln_label.grid(row=0,column=2,padx=10,pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0,column=3, padx=10, pady=10)

id_label = Label(data_frame, text="ID",font=('Consolas',11))
id_label.grid(row=0,column=4,padx=10,pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0,column=5, padx=10, pady=10)

address_label = Label(data_frame, text="Address",font=('Consolas',11))
address_label.grid(row=1,column=0,padx=10,pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1,column=1, padx=10, pady=10)

city_label = Label(data_frame, text="City",font=('Consolas',11))
city_label.grid(row=1,column=2,padx=10,pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1,column=3, padx=10, pady=10)

state_label = Label(data_frame, text="State",font=('Consolas',11))
state_label.grid(row=1,column=4,padx=10,pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1,column=5, padx=10, pady=10)

zipcode_label = Label(data_frame, text="Zipcode",font=('Consolas',11))
zipcode_label.grid(row=1,column=6,padx=10,pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=1,column=7, padx=10, pady=10)

# Button frame
button_frame = LabelFrame(root, text="Commands",font=('Consolas',11))
button_frame.pack(fill='x',expand="yes",padx=20)

update_button = Button(button_frame,text="Update",font=('Consolas',11))
update_button.grid(row=0,column=0,padx=10,pady=10)

add_button = Button(button_frame,text="Add",font=('Consolas',11),command=add_record)
add_button.grid(row=0,column=1,padx=10,pady=10)

delete_button = Button(button_frame,text="Delete",font=('Consolas',11))
delete_button.grid(row=0,column=2,padx=10,pady=10)

move_up_button = Button(button_frame,text="Move Up",command=up,font=('Consolas',11))
move_up_button.grid(row=0,column=3,padx=10,pady=10)

move_down_button = Button(button_frame,text="Move Down",command=down,font=('Consolas',11))
move_down_button.grid(row=0,column=4,padx=10,pady=10)

clear_record_button = Button(button_frame,text="Clear Entry Boxes",command=clear_entries,font=('Consolas',11))
clear_record_button.grid(row=0,column=5,padx=10,pady=10)

search_record_button = Button(button_frame,text="Search Record",font=('Consolas',11))
search_record_button.grid(row=0,column=6,padx=10,pady=10)

#binding the treeview
my_tree.bind("<ButtonRelease-1>",select_record)
query_database()

root.mainloop()