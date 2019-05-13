from tkinter import *
import os
emrg = Tk()
emrg.geometry("1300x750")

def inform():
    os.system("informed.py")

f1=Frame(emrg,height =10, width = 1200)
f1.pack(side=BOTTOM)


l1=Label(f1,text="Enter the Sr no  -  ", font=("Courier", 18))
l1.grid(row=0,column=0)

E1 = Entry(f1,bd =5)
E1.grid(row=0,column=1)

b1=Button(f1,text="Informed",fg="green",activebackground="green",height=2,width=15,command=inform)
b1.grid(row=0,column=2)


photo=PhotoImage(file='emergency.png')       #Importing picture
label0=Label(emrg,image=photo)
label0.pack()

emrg.title("Emergency+")

emrg.mainloop()
