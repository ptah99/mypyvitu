from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("my digital clock")
clocklabel = Label(root, font=("Helvatica", 100), background="orange", foreground="red")
clocklabel.pack(anchor='sw')

def time():
    timestring = strftime('%H:%M:%S %p')
    clocklabel.config(text=timestring)
    clocklabel.after(1000, time)

time()
mainloop()
