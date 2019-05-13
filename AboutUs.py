from tkinter import *
import os
ab = Tk()
ab.geometry("990x550")
ab.title("About US")
ab.resizable(0,0)
photo = PhotoImage(file='About.png')
labelp = Label(ab, image=photo)
labelp.pack()
ab.mainloop()