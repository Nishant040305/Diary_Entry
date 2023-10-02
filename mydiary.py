import pickle
from tkinter import *
import datetime as d
def trigger():
    global c
    global u
    data = c.get('1.0','end-1c')
    f = open(f'{u}.dat','wb')
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
u = f"{str(dt)[8:10]} {t[dt.month]} {str(dt)[0:4]}"
text = f"{dt.strftime('%A')}\n{u}\nDear Diary\n"
c.pack(side=LEFT)
scrolllabel.pack(side=RIGHT,fill='y',expand=1)
c.insert(END,text)
but = Button(b,text="Save",command= lambda: trigger())
but.pack(anchor=S)
a.mainloop()