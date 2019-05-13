from tkinter import *

apl = Tk()
apl.geometry("500x360")
apl.title("Apply")
apl.resizable(0,0)

Label(text="Apply for Appointment", font=("Courier", 20)).place(x=90,y=20)

Label(text="Enter Doctor's Sr. no : ", font=("Courier", 14)).place(x=40,y=110)
E1=Entry(bd =2).place(x=320,y=115)

Label(text="Enter Slot no : ", font=("Courier", 14)).place(x=40,y=180)
E2=Entry(bd =2).place(x=320,y=185)

Button(text="Apply",fg="green",font=("Courier",10),activebackground="green",height=2,width=19).place(x=180,y=260)



apl.mainloop()