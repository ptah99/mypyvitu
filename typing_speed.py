from tkinter import *
from timeit import default_timer as timer
import random

window = Tk()
window.geometry('400 x 200')


def game():
    words = ['programming', 'coding', 'samosa', 'tea', 'blahblah', 'youtube']
    word = random.randit(0, (len(words) - 1))
    start = timer()
    windows = Tk()
    windows.geometry('400 x 200')
    x2 = Label(window, text=words[word], font="times 20")


x1 = Label(window, text="lets start this game...", font="times 20")
x1.place(x=10, y=50)

b1 = Button(window, text="goo", command=game, width=12, bg='gray')
b1.place(x=150, y=100)

window.mainloop()
