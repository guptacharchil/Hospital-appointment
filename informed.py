from tkinter import *
import os
a = Tk()
a.geometry("990x400")
a.title("informed")
a.resizable(0,0)
photo = PhotoImage(file='emergency-plan.png')
labelp = Label(a, image=photo)
labelp.pack()
a.mainloop()