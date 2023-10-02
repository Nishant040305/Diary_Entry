import pickle
from tkinter import *
import datetime as d
def procced(time):
    try:
        global login
        login.destroy()
        def trigger():
            global time
            global c
            global u
            data = c.get('1.0','end-1c')
            f = open(f'{time}.dat','wb')
            pickle.dump(data,f)
            f.close()

        t=[0,'January','February','March','April','May','June',"July","August",'September','October','November','December']
        a = Tk()
        
        a.title("My Diary")
        b=Frame(a)
        b.pack()
        dt= d.datetime.now()
        print(dt)
        c= Text(b,borderwidth=2,wrap= 'char',relief='groove',
        font =('Helvetica', 13, 'italic'),background='whitesmoke' )
        scrolllabel = Scrollbar(b,orient='vertical',command=c.yview)
        c['yscrollcommand']=scrolllabel.set
        c.pack(side=LEFT)
        scrolllabel.pack(side=RIGHT,fill='y',expand=1)
        f = open(f'{time}.dat','rb')
        text = pickle.load(f)
        c.insert(END,text)
        but = Button(b,text="Save",command= lambda: trigger())
        but.pack(anchor=S)
        a.mainloop()
    except:
        pass
def datee():
    global txt
    t = txt.get('1.0','end-1c')
    procced(t)
login = Tk()
login.title('Login Page')
page = Frame(login)
login.geometry('450x450')
login.resizable(False,False)
page.grid()
title = Label(page,text = 'Enter Date',font = ('Times',25,'italic'))
title.grid(row = 0,column =0,padx=40,pady=(60,40))
txt = Text(page,width = 45,bd=1,height=4,relief='sunken',font=('calibri',13))
txt.grid(row = 1,column = 0,padx=(20,0))
enter = Button(page,text = 'Enter',width=15,relief='sunken',bd=1,command = lambda : datee())
enter.grid(row=2,column = 0,pady=30)
login.mainloop()