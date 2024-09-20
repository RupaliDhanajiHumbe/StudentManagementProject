from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import mysql
import mysql.connector as sql
import pandas as pd

def iExit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pd.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved succesfully')

def field_data(title,button_text,command):
    global idEntry,nameEntry,mobileEntry,emailEntry,addressEntry,genderEntry,dobEntry,screen_window
    screen_window = Toplevel()
    screen_window.title(title)
    screen_window.grab_set()
    screen_window.resizable(False, False)
    idlabel = Label(screen_window, text='Id', font=('times new roman', 20, 'bold'))
    idlabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen_window, font=('times new roman', 20, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=15, pady=10)

    namelabel = Label(screen_window, text='Name', font=('times new roman', 20, 'bold'))
    namelabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen_window, font=('times new roman', 20, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=15, pady=10)

    mobilelabel = Label(screen_window, text='Mobole', font=('times new roman', 20, 'bold'))
    mobilelabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    mobileEntry = Entry(screen_window, font=('times new roman', 20, 'bold'), width=24)
    mobileEntry.grid(row=2, column=1, padx=15, pady=10)

    emaillabel = Label(screen_window, text='Email', font=('times new roman', 20, 'bold'))
    emaillabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(screen_window, font=('times new roman', 20, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, padx=15, pady=10)

    addresslabel = Label(screen_window, text='Address', font=('times new roman', 20, 'bold'))
    addresslabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(screen_window, font=('times new roman', 20, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, padx=15, pady=10)

    genderlabel = Label(screen_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderlabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(screen_window, font=('times new roman', 20, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, padx=15, pady=10)

    doblabel = Label(screen_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    doblabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(screen_window, font=('times new roman', 20, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, padx=15, pady=10)
    Student_button = ttk.Button(screen_window, text=button_text, command=command)
    Student_button.grid(row=7, columnspan=3)


    if title=='Update Student':
        indexing = studentTable.focus()
        # print(indexing)
        content = studentTable.item(indexing)
        listdata = content['values']
        # print(listdata)
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        mobileEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])
        genderEntry.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])

def update_data():
    query='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
    cur.execute(query,(nameEntry.get(),mobileEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,ctime,idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {idEntry.get()} is updated successfully',parent=screen_window)
    screen_window.destroy()
    show_stusent()


def show_stusent():
    query = 'select * from student'
    cur.execute(query)
    fetched_data = cur.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)
def delete_student():
    #cur = con.cursor()
    indexing = studentTable.focus()
    print(indexing)
    content = studentTable.item(indexing)
   # print(content)
    content_id = content['values'][0]
    #print(content_id)
    query = 'delete from student where id=%s'
    cur.execute(query, (content_id,))
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted successfully')
    query = 'select * from student'
    cur.execute(query)
    fetched_data=cur.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)
def search_data():
    query = 'select * from student where id=%s or name=%s or mobile=%s or email=%s or address=%s or gender=%s or dob=%s'
    cur.execute(query, (idEntry.get(),nameEntry.get(),mobileEntry.get(),mobileEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data=cur.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)


def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or mobileEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror('Errer','All feilds are required',parent=screen_window)

    else:
        try:
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(query,(idEntry.get(),nameEntry.get(),mobileEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,ctime))
            con.commit()
            result=messagebox.askyesno('Confirm Insert Record Status','Data added successfuly.Do youwant to clean the form?',parent=screen_window)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                mobileEntry.delete(0,END)
                emailEntry.delete(0,END)
                addressEntry.delete(0,END)
                genderEntry.delete(0,END)
                dobEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','Id connot be repeated',parent=screen_window)
            return
        query='select *from student'
        cur.execute(query)
        fetched_data=cur.fetchall()
        print(fetched_data)
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('',END,values=data)

def connectDB():
    def connect():
        global cur,con
        try:
            con=sql.connect(host=hostEntry.get(),user=userEntry.get(),password=passwordEntry.get())
            cur=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
        try:
            query='create database studentmanagementsystem'
            cur.execute(query)
            query='use studentmanagementsystem'
            cur.execute(query)
            query="create table student(id int not null primary key,name varchar(40),mobile varchar(10),email varchar(40),address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))"
            cur.execute(query)
        except:
            query='use studentmanagementsystem'
            cur.execute(query)
        messagebox.showinfo('Success','Database Connection is Successful',parent=connectWindow)
        connectWindow.destroy()
        addstudentB.config(state=NORMAL)
        searchstudentB.config(state=NORMAL)
        updatestudentB.config(state=NORMAL)
        showstudentB.config(state=NORMAL)
        exportstudentB.config(state=NORMAL)
        deletestudentB.config(state=NORMAL)
        exitstudentB.config(state=NORMAL)

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x400+730+230')
    connectWindow.title('Dtabase Connection')
    connectWindow.grab_set()
    connectWindow.resizable(0,0)

    hostname=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostname.grid(row=0,column=0,pady=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    username=Label(connectWindow,text='User Name',font=('arial',20,'bold'))
    username.grid(row=1,column=0,pady=20)

    userEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    userEntry.grid(row=1,column=1,padx=40,pady=20)

    password=Label(connectWindow,text='Password ',font=('arial',20,'bold'))
    password.grid(row=2,column=0,pady=20)

    passwordEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)

    connectButton1=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton1.grid(row=3,columnspan=2)

def clock():
    global date,ctime
    date=time.strftime("%d/%m/%Y")
    ctime=time.strftime('%H:%M:%S')
    #datetimeleble.config(text=f'  Date: {date}\nTime:{ctime}')
    datetimeleble.config(text=f'  Date: {date}  Time:{ctime}')
    datetimeleble.after(1000,clock)

count=0
text=''
def slider():
    global text, count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    Slable.config(text=text)
    Slable.after(300,slider)
    count+=1

root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1174x680+0+0')
root.resizable(0,0)
root.title('Student Management System')

"""datetimeleble=Label(root,font=('times new roman',18,'bold'))
datetimeleble.place(x=10,y=10)
clock()"""

s='Student Managament System'
Slable=Label(root,text=s,font=('times new roman',32,'bold'),bg='teal',fg='gold',bd=9,relief=GROOVE)
#Slable.place(x=320,y=0)
Slable.pack(fill=X)
slider()

datetimeleble=Label(root,font=('times new roman',18,'bold'))
datetimeleble.place(x=570,y=80)
clock()

"""s='Student Managament System'
Slable=Label(root,text=s,font=('arial',28,'italic bold'))
Slable.place(x=200,y=0)
slider()"""

connectButton=ttk.Button(root,text='Connect database',command=connectDB)
connectButton.place(x=980,y=80)

leftframe=Frame(root)
leftframe.place(x=50,y=80,width=300,height=600)

logo_img=PhotoImage(file='studentslogo.png')
logolabel=Label(leftframe,image=logo_img)
logolabel.grid(row=0,column=0)

addstudentB=ttk.Button(leftframe,text='Add Student', state=DISABLED, width=25,command=lambda :field_data('Add Student','Add',add_data))
addstudentB.grid(row=1,column=0,pady=20)

searchstudentB=ttk.Button(leftframe,text='Search Student',state=DISABLED,width=25,command= lambda :field_data('Search Student','Search',search_data))
searchstudentB.grid(row=2,column=0,pady=20)

deletestudentB=ttk.Button(leftframe,text='Delete Student',state=DISABLED,width=25,command=delete_student)
deletestudentB.grid(row=3,column=0,pady=20)

updatestudentB=ttk.Button(leftframe,text='Update Student',state=DISABLED,width=25,command=lambda :field_data('Update Student','Update',update_data))
updatestudentB.grid(row=4,column=0,pady=20)

showstudentB=ttk.Button(leftframe,text='Show Student',state=DISABLED,width=25,command=show_stusent)
showstudentB.grid(row=5,column=0,pady=20)

exportstudentB=ttk.Button(leftframe,text='Export Student',state=DISABLED,width=25,command=export_data)
exportstudentB.grid(row=6,column=0,pady=20)

exitstudentB=ttk.Button(leftframe,text='Exit Student',width=25,command=iExit)
exitstudentB.grid(row=7,column=0,pady=20)


rightframe=Frame(root)
rightframe.place(x=350,y=130,width=820,height=600)

scrollBarx=Scrollbar(rightframe,orient=HORIZONTAL)
scrollBarx.pack(side=BOTTOM,fill=X)
scrollBary=Scrollbar(rightframe,orient=VERTICAL)
scrollBary.pack(side=RIGHT,fill=Y)

studentTable=ttk.Treeview(rightframe,columns=('Sid','Sname','SMobile No','Email','Address','Gender','D.O.B','Added Date'
                                            ,'Added Time'),xscrollcommand=scrollBarx.set,yscrollcommand=scrollBary.set)
scrollBarx.config(command=studentTable.xview)
scrollBary.config(command=studentTable.yview)
studentTable.pack(fill=BOTH,expand=1)
studentTable.heading('Sid',text='Sid')
studentTable.heading('Sname',text='Sname')
studentTable.heading('SMobile No',text='SMobile No')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.column('Sid',width=50,anchor=CENTER)
studentTable.column('Sname',width=300,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('SMobile No',width=200,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('D.O.B',width=100,anchor=CENTER)
studentTable.column('Added Date',width=100,anchor=CENTER)
studentTable.column('Added Time',width=100,anchor=CENTER)

#style=ttk.Style()
#style.configure('Treeview',rowheight=10,font=('arial',10,'bolb'))

studentTable.config(show='headings')
root.mainloop()