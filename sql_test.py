from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if(id=="" or name=="" or phone==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("insert into student values( "+ id +" , "+ name +" , "+ phone +"')")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        MessageBox.showinfo("Insert Status", "Inserted Successfully");
        con.close()

def delete():
    if(e_id.get() == ""):
        MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("delete from student where id='"+ e_id.get() +"¹")
        cursor.execute("commit")
        
        e_id.delete(0, 'end')
        e_name.delete(0, 'end' )
        e_phone.delete(0, 'end')
        MessageBox.showinfo("Delete Status", "Deleted Successfully");
        con.close()

def update():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()
    
    if(id =="" or name =="" or phone ==""):
        MessageBox.Showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("update student set name='"+ name +" , phone='"+ phone +" where id='"+ id +"¹")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end' )
        e_phone.delete(0, 'end')
        MessageBox.showinfo("Update Status", "Updated Successfully");
        con.close()

root = Tk()
root.geometry("600x300")
root.title("Python+Tkinter+MySql")

id = Label(root,text='Enter ID' , font= ('bold', 10))
id.place(x=20,y=30)

name = Label(root,text= 'Enter Name', font=('bold' , 10) )
name.place(x=20,y=60)

phone = Label (root,text='Enter Phone', font=('bold' , 10))
phone.place(x=20,y=90)

e_id = Entry()
e_id.place(x=150, y=30)

e_name = Entry()
e_name.place(x=150, y=60)

e_phone = Entry()
e_phone.place(x=150, y=90)

insert = Button(root, text="Insert", font= ("italic" , 10) , bg="white", command=insert)
insert.place(x=20, y=140)

delete = Button(root, text="Delete", font=("italic", 10) , bg="white", command=delete)
delete.place(x=70, y=140)

update = Button(root, text="Update", font= (" italic" , 10) , bg="white", command=update)
update.place(x=130, y=140)

get = Button(root, text="Get" , font=(" italic" , 10) , bg="white", command=get)
get.place(x=190, y=140)

root.mainloop()