from tkinter import *
from PIL import ImageTk     #pip install pillow  python Image laibrary
from tkinter import messagebox

def login():
    if userEntery.get()=='' or passwordEntery.get()=='' :
        messagebox.showerror('Error','Fields cannot be empty')
    elif userEntery.get()=='Rupali Humbe' and passwordEntery.get()=='Rupali@123':
        messagebox.showinfo('Success','Welcome')
        root.destroy()
        import MainSMS

    else:
        messagebox.showinfo('Error','please enter correct Information')

root=Tk()
root.geometry('1100x700+120+150')
root.resizable(False,False)
root.title('Admin Login Page')
bimg=ImageTk.PhotoImage(file="bg2.jpg")
bgL=Label(root,image=bimg,bg='pink')
bgL.place(x=0,y=0,)
Loginf=Frame(root,bg='pink')
Loginf.place(x=200,y=130)
logoI=PhotoImage(file="log.png")
logoL=Label(Loginf,image=logoI)
logoL.grid(row=0,column=0,pady=10,columnspan=2)
userImg=PhotoImage(file='user.png')
username=Label(Loginf,image=userImg,text='Usrename',compound=LEFT,font=('times new roman',20,'bold'),bg='pink')
username.grid(row=1,column=0,pady=10,padx=20)

userEntery=Entry(Loginf,font=('times new roman',20,'bold'),bd=5,fg='royalblue' )
userEntery.grid(row=1 ,column=1,padx=20)
passwordImg=PhotoImage(file='password.png')
password=Label(Loginf,image=passwordImg,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='pink')
password.grid(row=2,column=0,pady=5,padx=20)

passwordEntery=Entry(Loginf,font=('times new roman',20,'bold'),bd=5,fg='royalblue' )
passwordEntery.grid(row=2 ,column=1,padx=20)

B=Button(Loginf,text='Login',font=('times new roman',15,'bold'),width=16,fg='white',
         bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='white',
         cursor='hand2',command=login)
B.grid(row=3,column=1,pady=10)
root.mainloop()