from tkinter import *
import os
import string
from array import *
QuizList = []
a=[]
b=[]
with open('doc.txt','r') as f:
    for line in f:
        for i, c in enumerate(line):
            if c not in string.ascii_letters:
                print(line[:i])
                a.append(line[:i])
                break
f.close()
g = open("doc.txt",'r')

for line in g:
    words = line.split()
    b.append(words[-1])
g.close()
print(a)
print(b)
l=len(a)
print(l)

with open('app.txt') as s:
    #w, h = [int(x) for x in next(f).split()] # read first line
    array = []
    for line in s: # read rest of lines
        array.append([int(x) for x in line.split()])

T = [[0] *8 for i in range(0,9)]
for i in range(0,9):
    for j in range(0,8):
        T[i][j]=array[i][j]

#Functions



def apply():
    def add():

        if len(E1.get())==0 or len(E2.get())==0:
            print("You Can't leave any filed empty")
            Label(apl,text="You can't leave any field empty", font=("Courier", 9), fg="red").place(x=150, y=230)
        else:
            i = E1.get()
            w = E2.get()
            i = int(i)
            w = int(w)
            if T[i][w]==1:
                print("Slot Already Taken")
                Label(apl, text="       Slot Already Taken       ", font=("Courier", 9), fg="red").place(x=150, y=230)
            else:
                apl.destroy()
                T[i][w] = 1

    apl = Tk()
    apl.geometry("500x360")
    apl.title("Apply")
    apl.resizable(0, 0)

    Label(apl,text="Apply for Appointment", font=("Courier", 20)).place(x=90, y=20)

    Label(apl,text="Enter Doctor's Sr. no : ", font=("Courier", 14)).place(x=40, y=110)
    E1 = Entry(apl,bd=2)
    E1.place(x=320,y=115)

    Label(apl,text="Enter Slot no : ", font=("Courier", 14)).place(x=40, y=180)
    E2 = Entry(apl,bd=2)
    E2.place(x=320, y=185)
    Button(apl,text="Apply", fg="green", font=("Courier", 10), activebackground="green", height=2, width=19,command = add).place(x=180,
                                                                                                               y=260)
    apl.mainloop()


def cancel():
    def delete():
        if len(E1.get())==0 or len(E2.get())==0:
            print("You Can't leave any filed empty")
            Label(cl,text="You can't leave any field empty", font=("Courier", 9), fg="red").place(x=150, y=230)
        else:
            i = E1.get()
            i=int(i)
            w = E2.get()
            w=int(w)
            if T[i][w]==0:
                Label(cl, text="   This slot is already free   ", font=("Courier", 9), fg="red").place(x=150, y=230)
            else:
                cl.destroy()
                T[i][w] = 0

    cl = Tk()
    cl.geometry("500x360")
    cl.title("Apply")
    cl.resizable(0, 0)

    Label(cl, text="Cancel your Appointment", font=("Courier", 20)).place(x=90, y=20)

    Label(cl, text="Enter Doctor's Sr. no : ", font=("Courier", 14)).place(x=40, y=110)
    E1 = Entry(cl, bd=2)
    E1.place(x=320, y=115)

    Label(cl, text="Enter Slot no : ", font=("Courier", 14)).place(x=40, y=180)
    E2 = Entry(cl, bd=2)
    E2.place(x=320, y=185)
    Button(cl, text="Submit", fg="green", font=("Courier", 10), activebackground="green", height=2, width=19,
           command=delete).place(x=180,
                              y=260)
    cl.mainloop()




i=0

def showappointment():
    apt = Tk()
    apt.geometry("1400x400")
    f1 = Frame(apt, height=10, width=700)
    f1.pack(side=TOP)
    l1 = Label(f1, text="Sr no ", font=("Courier", 18), fg="blue")
    l1.grid(row=0, column=0)
    l1 = Label(f1, text="Doctor  ", font=("Courier", 18), fg="blue")
    l1.grid(row=0, column=1)
    l1 = Label(f1, text="Specialist  ", font=("Courier", 18), fg="blue")
    l1.grid(row=0, column=2)
    l1 = Label(f1, text="10-11(0)  ", font=("Courier", 18), fg="blue")
    l1.grid(row=0, column=3)
    l1 = Label(f1, text="11-12(1)  ", font=("Courier", 18), fg="blue")
    l1.grid(row=0, column=4)
    l1 = Label(f1, text="12-1(2)  ", font=("Courier", 18), fg="blue")
    l1.grid(row=0, column=5)
    l1 = Label(f1, text="1-2(3)  ", font=("Courier", 18), fg="blue")
    l1.grid(row=0, column=6)
    l1 = Label(f1, text="2-3(4)  ", font=("Courier", 18), fg="blue")
    l1.grid(row=0, column=7)
    l1 = Label(f1, text="3-4(5)  ", font=("Courier", 18), fg="blue")
    l1.grid(row=0, column=8)
    l1 = Label(f1, text="4-5(6)  ", font=("Courier", 18), fg="blue")
    l1.grid(row=0, column=9)
    l1 = Label(f1, text="5-6(7)  ", font=("Courier", 18), fg="blue")
    l1.grid(row=0, column=10)

    l2 = Label(f1, text=i, font=("Courier", 18))
    l2.grid(row=1, column=0)
    l2 = Label(f1, text=a[i], font=("Courier", 18))
    l2.grid(row=1, column=1)
    l2 = Label(f1, text=b[i], font=("Courier", 18))
    l2.grid(row=1, column=2)
    l2 = Label(f1, text=T[0][0], font=("Courier", 18))
    l2.grid(row=1, column=3)
    l2 = Label(f1, text=T[0][1], font=("Courier", 18))
    l2.grid(row=1, column=4)
    l2 = Label(f1, text=T[0][2], font=("Courier", 18))
    l2.grid(row=1, column=5)
    l2 = Label(f1, text=T[0][3], font=("Courier", 18))
    l2.grid(row=1, column=6)
    l2 = Label(f1, text=T[0][4], font=("Courier", 18))
    l2.grid(row=1, column=7)
    l2 = Label(f1, text=T[0][5], font=("Courier", 18))
    l2.grid(row=1, column=8)
    l2 = Label(f1, text=T[0][6], font=("Courier", 18))
    l2.grid(row=1, column=9)
    l2 = Label(f1, text=T[0][7], font=("Courier", 18))
    l2.grid(row=1, column=10)

    l2 = Label(f1, text=i + 1, font=("Courier", 18))
    l2.grid(row=2, column=0)
    l2 = Label(f1, text=a[i + 1], font=("Courier", 18))
    l2.grid(row=2, column=1)
    l2 = Label(f1, text=b[i + 1], font=("Courier", 18))
    l2.grid(row=2, column=2)
    l2 = Label(f1, text=T[1][0], font=("Courier", 18))
    l2.grid(row=2, column=3)
    l2 = Label(f1, text=T[1][1], font=("Courier", 18))
    l2.grid(row=2, column=4)
    l2 = Label(f1, text=T[1][2], font=("Courier", 18))
    l2.grid(row=2, column=5)
    l2 = Label(f1, text=T[1][3], font=("Courier", 18))
    l2.grid(row=2, column=6)
    l2 = Label(f1, text=T[1][4], font=("Courier", 18))
    l2.grid(row=2, column=7)
    l2 = Label(f1, text=T[1][5], font=("Courier", 18))
    l2.grid(row=2, column=8)
    l2 = Label(f1, text=T[1][6], font=("Courier", 18))
    l2.grid(row=2, column=9)
    l2 = Label(f1, text=T[1][7], font=("Courier", 18))
    l2.grid(row=2, column=10)

    l2 = Label(f1, text=i + 2, font=("Courier", 18))
    l2.grid(row=3, column=0)
    l2 = Label(f1, text=a[i + 2], font=("Courier", 18))
    l2.grid(row=3, column=1)
    l2 = Label(f1, text=b[i + 2], font=("Courier", 18))
    l2.grid(row=3, column=2)
    l2 = Label(f1, text=T[2][0], font=("Courier", 18))
    l2.grid(row=3, column=3)
    l2 = Label(f1, text=T[2][1], font=("Courier", 18))
    l2.grid(row=3, column=4)
    l2 = Label(f1, text=T[2][2], font=("Courier", 18))
    l2.grid(row=3, column=5)
    l2 = Label(f1, text=T[2][3], font=("Courier", 18))
    l2.grid(row=3, column=6)
    l2 = Label(f1, text=T[2][4], font=("Courier", 18))
    l2.grid(row=3, column=7)
    l2 = Label(f1, text=T[2][5], font=("Courier", 18))
    l2.grid(row=3, column=8)
    l2 = Label(f1, text=T[2][6], font=("Courier", 18))
    l2.grid(row=3, column=9)
    l2 = Label(f1, text=T[2][7], font=("Courier", 18))
    l2.grid(row=3, column=10)

    l2 = Label(f1, text=i + 3, font=("Courier", 18))
    l2.grid(row=4, column=0)
    l2 = Label(f1, text=a[i + 3], font=("Courier", 18))
    l2.grid(row=4, column=1)
    l2 = Label(f1, text=b[i + 3], font=("Courier", 18))
    l2.grid(row=4, column=2)
    l2 = Label(f1, text=T[3][0], font=("Courier", 18))
    l2.grid(row=4, column=3)
    l2 = Label(f1, text=T[3][1], font=("Courier", 18))
    l2.grid(row=4, column=4)
    l2 = Label(f1, text=T[3][2], font=("Courier", 18))
    l2.grid(row=4, column=5)
    l2 = Label(f1, text=T[3][3], font=("Courier", 18))
    l2.grid(row=4, column=6)
    l2 = Label(f1, text=T[3][4], font=("Courier", 18))
    l2.grid(row=4, column=7)
    l2 = Label(f1, text=T[3][5], font=("Courier", 18))
    l2.grid(row=4, column=8)
    l2 = Label(f1, text=T[3][6], font=("Courier", 18))
    l2.grid(row=4, column=9)
    l2 = Label(f1, text=T[3][7], font=("Courier", 18))
    l2.grid(row=4, column=10)

    l2 = Label(f1, text=i + 4, font=("Courier", 18))
    l2.grid(row=5, column=0)
    l2 = Label(f1, text=a[i + 4], font=("Courier", 18))
    l2.grid(row=5, column=1)
    l2 = Label(f1, text=b[i + 4], font=("Courier", 18))
    l2.grid(row=5, column=2)
    l2 = Label(f1, text=T[4][0], font=("Courier", 18))
    l2.grid(row=5, column=3)
    l2 = Label(f1, text=T[4][1], font=("Courier", 18))
    l2.grid(row=5, column=4)
    l2 = Label(f1, text=T[4][2], font=("Courier", 18))
    l2.grid(row=5, column=5)
    l2 = Label(f1, text=T[4][3], font=("Courier", 18))
    l2.grid(row=5, column=6)
    l2 = Label(f1, text=T[4][4], font=("Courier", 18))
    l2.grid(row=5, column=7)
    l2 = Label(f1, text=T[4][5], font=("Courier", 18))
    l2.grid(row=5, column=8)
    l2 = Label(f1, text=T[4][6], font=("Courier", 18))
    l2.grid(row=5, column=9)
    l2 = Label(f1, text=T[4][7], font=("Courier", 18))
    l2.grid(row=5, column=10)

    l2 = Label(f1, text=i + 5, font=("Courier", 18))
    l2.grid(row=6, column=0)
    l2 = Label(f1, text=a[i + 5], font=("Courier", 18))
    l2.grid(row=6, column=1)
    l2 = Label(f1, text=b[i + 5], font=("Courier", 18))
    l2.grid(row=6, column=2)
    l2 = Label(f1, text=T[5][0], font=("Courier", 18))
    l2.grid(row=6, column=3)
    l2 = Label(f1, text=T[5][1], font=("Courier", 18))
    l2.grid(row=6, column=4)
    l2 = Label(f1, text=T[5][2], font=("Courier", 18))
    l2.grid(row=6, column=5)
    l2 = Label(f1, text=T[5][3], font=("Courier", 18))
    l2.grid(row=6, column=6)
    l2 = Label(f1, text=T[5][4], font=("Courier", 18))
    l2.grid(row=6, column=7)
    l2 = Label(f1, text=T[5][5], font=("Courier", 18))
    l2.grid(row=6, column=8)
    l2 = Label(f1, text=T[5][6], font=("Courier", 18))
    l2.grid(row=6, column=9)
    l2 = Label(f1, text=T[5][7], font=("Courier", 18))
    l2.grid(row=6, column=10)

    l2 = Label(f1, text=i + 6, font=("Courier", 18))
    l2.grid(row=7, column=0)
    l2 = Label(f1, text=a[i + 6], font=("Courier", 18))
    l2.grid(row=7, column=1)
    l2 = Label(f1, text=b[i + 6], font=("Courier", 18))
    l2.grid(row=7, column=2)
    l2 = Label(f1, text=T[6][0], font=("Courier", 18))
    l2.grid(row=7, column=3)
    l2 = Label(f1, text=T[6][1], font=("Courier", 18))
    l2.grid(row=7, column=4)
    l2 = Label(f1, text=T[6][2], font=("Courier", 18))
    l2.grid(row=7, column=5)
    l2 = Label(f1, text=T[6][3], font=("Courier", 18))
    l2.grid(row=7, column=6)
    l2 = Label(f1, text=T[6][4], font=("Courier", 18))
    l2.grid(row=7, column=7)
    l2 = Label(f1, text=T[6][5], font=("Courier", 18))
    l2.grid(row=7, column=8)
    l2 = Label(f1, text=T[6][6], font=("Courier", 18))
    l2.grid(row=7, column=9)
    l2 = Label(f1, text=T[6][7], font=("Courier", 18))
    l2.grid(row=7, column=10)

    l2 = Label(f1, text=i + 7, font=("Courier", 18))
    l2.grid(row=8, column=0)
    l2 = Label(f1, text=a[i + 7], font=("Courier", 18))
    l2.grid(row=8, column=1)
    l2 = Label(f1, text=b[i + 7], font=("Courier", 18))
    l2.grid(row=8, column=2)
    l2 = Label(f1, text=T[7][0], font=("Courier", 18))
    l2.grid(row=8, column=3)
    l2 = Label(f1, text=T[7][1], font=("Courier", 18))
    l2.grid(row=8, column=4)
    l2 = Label(f1, text=T[7][2], font=("Courier", 18))
    l2.grid(row=8, column=5)
    l2 = Label(f1, text=T[7][3], font=("Courier", 18))
    l2.grid(row=8, column=6)
    l2 = Label(f1, text=T[7][4], font=("Courier", 18))
    l2.grid(row=8, column=7)
    l2 = Label(f1, text=T[7][5], font=("Courier", 18))
    l2.grid(row=8, column=8)
    l2 = Label(f1, text=T[7][6], font=("Courier", 18))
    l2.grid(row=8, column=9)
    l2 = Label(f1, text=T[7][7], font=("Courier", 18))
    l2.grid(row=8, column=10)

    l2 = Label(f1, text=i + 8, font=("Courier", 18))
    l2.grid(row=9, column=0)
    l2 = Label(f1, text=a[i + 8], font=("Courier", 18))
    l2.grid(row=9, column=1)
    l2 = Label(f1, text=b[i + 8], font=("Courier", 18))
    l2.grid(row=9, column=2)
    l2 = Label(f1, text=T[8][0], font=("Courier", 18))
    l2.grid(row=9, column=3)
    l2 = Label(f1, text=T[8][1], font=("Courier", 18))
    l2.grid(row=9, column=4)
    l2 = Label(f1, text=T[8][2], font=("Courier", 18))
    l2.grid(row=9, column=5)
    l2 = Label(f1, text=T[8][3], font=("Courier", 18))
    l2.grid(row=9, column=6)
    l2 = Label(f1, text=T[8][4], font=("Courier", 18))
    l2.grid(row=9, column=7)
    l2 = Label(f1, text=T[8][5], font=("Courier", 18))
    l2.grid(row=9, column=8)
    l2 = Label(f1, text=T[8][6], font=("Courier", 18))
    l2.grid(row=9, column=9)
    l2 = Label(f1, text=T[8][7], font=("Courier", 18))
    l2.grid(row=9, column=10)
    apt.title("Appointment")
    apt.mainloop()


def about_window():
    os.system("AboutUs.py")

def openemr():
    os.system("emergency.py")



#Main Window
root = Tk()
root.geometry("750x500")

f1=Frame(root,height =50 , width = 1200)
f1.pack(side=BOTTOM,)
f4=Frame(root,height=150, width=800)

head=Label(f4,text="+ AKC HOSPITAL +", font=("Courier", 36),fg="red")
ttag=Label(f4,text="We always care for you....",font=("Courier", 18),fg="green")
ttag.pack(side=BOTTOM)
head.pack()

f4.pack(side=TOP)
f2=Frame(root,height=400, width=400 )
f3=Frame(root,height=600, width=400 )
f3.pack(side=LEFT)
#f3=Frame(root,height=400, width=400 ,bg="green")

label=Label(f2,text="Logged In Successful", font=("Courier", 18))
label.place(x=45,y=50)
label12=Label(f2,text="AKC HOSPITAL ", font=("Courier", 18))





b1=Button(f2,text="Check Doctor Details",fg="green",font=("Courier",10),activebackground="green",height=2,width=19,command=showappointment)
b1.place(x=180,y=220)


newb=Button(f2,text="Check Appointment list",font=("Courier",10),fg="blue",activebackground="blue",height=2,width=40,command = showappointment)
newb.place(x=10,y=100)

newb=Button(f2,text="Apply for Appointment",font=("Courier",10),fg="blue",activebackground="blue",height=2,width=40,command = apply)
newb.place(x=10,y=160)

newb=Button(f2,text="Cancel Appointment",font=("Courier",10),fg="blue",activebackground="blue",height=2,width=19,command = cancel)
newb.place(x=10,y=220)


f2.pack(side=RIGHT)

b3=Button(f1,text="EMERGENCY",font=("Courier", 20),activebackground="red",fg="red",command=openemr)
#b4=Button(f1,text="APPOINTMENT",font=("Courier", 15),activebackground="green",fg="blue")
#b5=Button(f1,text="AVILABILITY",font=("Courier", 15),activebackground="green",fg="blue")


b6=Button(f1,text="About us",font=("Courier", 20),activebackground="green",fg="blue",command=about_window)
b3.grid(row=0,column=0)
#b4.grid(row=0,column=1)
#b5.grid(row=0,column=2)
b6.grid(row=0,column=3)

photo=PhotoImage(file='medical.png')       #Importing picture
label0=Label(f3,image=photo)
label0.pack()


root.title("Main Window")
root.resizable(0,0)
root.mainloop()

k=open("app.txt","w")
for i in range(0,9):
    for j in range(0,8):
        k.write(str(T[i][j]))
        k.write(" ")
    k.write("\n")