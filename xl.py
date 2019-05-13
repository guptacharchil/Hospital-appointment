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
    name = E1.get()
    password = E2.get()
    if len(name)==0 or len(password)==0:
        print("You cant leave any field empty")
        Label(text="    You can't leave any field empty         ", font=("Courier", 9),fg="red").place(x=440,y=248)
    else:
        if (k[0] == 1):

            t = open("doc.txt", "r")
            for line in t:
                if name in line:
                    if password in line:
                        print("got it")
                        f=open("current.txt","w")
                        f.write(name)
                        root.destroy()
                        os.system("afterlogin.py")
                        found = True
                        z = 1
                        break
            if (z == 0):
                print("not found")
                Label(text="Username and password did not matched", font=("Courier", 9), fg="red").place(x=440, y=248)



        else:
            t = open("patp.txt", "r")
            for line in t:
                if name in line:
                    if password in line:
                        print("got it")
                        cu = open("current.txt", "w")
                        cu.write(name)
                        root.destroy()
                        os.system("afterlogin.py")
                        found = True
                        z = 1
                        break
            if (z == 0):
                print("not found")
                Label(text="Username and password did not matched", font=("Courier", 9), fg="red").place(x=440, y=248)

def about_window():
    os.system("AboutUs.py")

def openemr():
    os.system("emergency.py")

def openpatsignup():
    os.system("pat_signup.py")

def opendocsignup():
    os.system("doc_signup.py")

def forgetpass():
    def close():
        fp.destroy()
    fp = Tk()
    fp.geometry("550x200")
    Label(fp,text="Please contact Hospital authority\nto retrive password\n\n",font = ("courier",18)).pack()
    Button(fp,text="Ok",font = ("courier",18),command=close).pack()
    fp.mainloop()


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
b2=Button(f2,text="forgot password",fg="red",activebackground="red",height=2,width=15,command = forgetpass)
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
