from tkinter import *
root = Tk()
root.geometry("750x500")
root.title("Sign UP")
root.resizable(0,0)

def doc():
    f = open("docc.txt", "a")
    name=namebox.get()
    f.write(name)
    f.write("\t")
    phone=phonebox.get()
    f.write(phone)
    f.write("\t")
    age = agebox.get()
    f.write(age)
    f.write("\t")
    gender = genderbox.get()
    f.write(gender)
    f.write("\t")
    password = passwordbox.get()
    f.write(password)
    f.write("\t")
    city = citybox.get()
    f.write(city)
    f.write("\t")
    speciality = specialitybox.get()
    f.write(speciality)
    f.write("\n")
    f.close()
    root.destroy()

head=Label(text="     Sign UP\n", font=("Courier", 25))
head.grid(column=0,row=0,columnspan=2)
para = Label(text="          Please fill the following details.\n", font=("Courier", 18))
para.grid(column=0,row=1,columnspan=2)

f1=Frame(root)
f1.place(x=130,y=140)

namel=Label(f1,text="Name :", font=("Courier", 18))
namel.grid(column=0,row=2)
namebox=Entry(f1,bd=2)
namebox.grid(column=1,row=2)

phonel=Label(f1,text="Phone no. :", font=("Courier", 18))
phonel.grid(column=0,row=3)
phonebox=Entry(f1,bd=2)
phonebox.grid(column=1,row=3)

agel=Label(f1,text="Age :", font=("Courier", 18))
agel.grid(column=0,row=4)
agebox=Entry(f1,bd=2)
agebox.grid(column=1,row=4)

agel=Label(f1,text="Age :", font=("Courier", 18))
agel.grid(column=0,row=4)
agebox=Entry(f1,bd=2)
agebox.grid(column=1,row=4)

genderl=Label(f1,text="Gender(Male\Female) :", font=("Courier", 18))
genderl.grid(column=0,row=5)
genderbox=Entry(f1,bd=2)
genderbox.grid(column=1,row=5)

passwordl=Label(f1,text="Create Password :", font=("Courier", 18))
passwordl.grid(column=0,row=6)
passwordbox=Entry(f1,bd=2,show="*")
passwordbox.grid(column=1,row=6)

cityl=Label(f1,text="City :", font=("Courier", 18))
cityl.grid(column=0,row=7)
citybox=Entry(f1,bd=2)
citybox.grid(column=1,row=7)

specialityl=Label(f1,text="Speciality :", font=("Courier", 18))
specialityl.grid(column=0,row=8)
specialitybox=Entry(f1,bd=2)
specialitybox.grid(column=1,row=8)


submit = Button(text="Submit Details", font=("Courier", 18),command=doc)
submit.place(x=250,y=400)


root.mainloop()
