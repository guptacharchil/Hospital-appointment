from tkinter import *
import os


#Functions

def togglecheck1():
    C2.toggle()
    if k[0] == 0:
        k[0] = 1
    else:
        k[0]=0


def togglecheck2():
    C1.toggle()
    if k[0] == 0:
        k[0] = 1
    else:
        k[0]=0

def signin():
    z = int(0)
    if (k[0] == 1):
        name = E1.get()
        password = E2.get()
        t = open("doc.txt", "r")
        for line in t:
            if name in line:
                if password in line:
                    print("got it")
                    C1.destroy()
                    f2 = Frame(root, height=400, width=400)
                    f2.pack(side=RIGHT)
                    label = Label(f2, text="Logged In Successful", font=("Courier", 18))
                    label.place(x=45, y=50)
                    label12 = Label(f2, text="AKC HOSPITAL ", font=("Courier", 18))

                    b1 = Button(f2, text="Check Doctor Details", fg="green", font=("Courier", 10),
                                activebackground="green", height=2, width=19)
                    b1.place(x=180, y=220)

                    newb = Button(f2, text="Check Appointment list", font=("Courier", 10), fg="blue",
                                  activebackground="blue", height=2, width=40)
                    newb.place(x=10, y=100)

                    newb = Button(f2, text="Apply for Appointment", font=("Courier", 10), fg="blue",
                                  activebackground="blue", height=2, width=40)
                    newb.place(x=10, y=160)

                    newb = Button(f2, text="Cancel Appointment", font=("Courier", 10), fg="blue",
                                  activebackground="blue", height=2, width=19)
                    newb.place(x=10, y=220)


                    found = True
                    z = 1
                    break
        if (z == 0):
            print("not found")




    else:
        name = E1.get()
        password = E2.get()
        t = open("pat.txt", "r")
        for line in t:
            if name in line:
                if password in line:
                    print("got it")

                    found = True
                    z = 1
                    break
        if (z == 0):
            print("not found")


def about_window():
    ab = Tk()
    ab.geometry("500x500")
    ab.title("About US")
    ab.resizable(0,0)
    photo = PhotoImage(file='About.png')
    labelp = Label(ab, image=photo)
    labelp.pack()
    ab.mainloop()

def openemr():
    os.system("emergency.py")

def openpatsignup():
    os.system("pat_signup.py")

def opendocsignup():
    os.system("doc_signup.py")


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

label=Label(f2,text="Sign In ", font=("Courier", 18))
label.grid()
label12=Label(f2,text="AKC HOSPITAL ", font=("Courier", 18))
label12.grid(row=0,column=1)

label1=Label(f2,text="USER NAME", font=("Courier", 18))
label1.grid(row=2,column=0)
E1 = Entry(f2,bd =2,highlightcolor="yellow")
E1.grid(row=2,column=1)
label2=Label(f2,text="PASSWORD", font=("Courier", 18))
E2 = Entry(f2,bd =2,show="*")
E2.grid(row=3,column=1)
label2.grid(row=3,column=0)

C1 = Checkbutton(f2, text = "PATIENT", onvalue = 0, offvalue = 1, height=5,  width = 20,command = togglecheck1)
C1.select()
C2 = Checkbutton(f2, text = "DOCTOR", onvalue = 1, offvalue = 0, height=5, width = 20,command = togglecheck2)
C1.grid(row=1,column=0)
C2.grid(row=1,column=1)
k=[0]

b1=Button(f2,text="sign in",fg="green",activebackground="green",height=2,width=15,command=signin)
b1.grid(row=5,column=0)
b2=Button(f2,text="forgot password",fg="red",activebackground="red",height=2,width=15)
b2.grid(row=5,column=1)
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

patsignup_but=Button(root,text="Patient sign up",fg="green",activebackground="green",height=2,width=15,command=openpatsignup)
patsignup_but.place(x=420,y=390)

docsignup_but=Button(root,text="Doctor sign up",fg="green",activebackground="green",height=2,width=15,command = opendocsignup)
docsignup_but.place(x=600,y=390)

root.title("Main Window")
root.resizable(0,0)
root.mainloop()
