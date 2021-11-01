from tkinter import *
from tkinter import messagebox



win = Tk()
win.title('Hello world')
win.geometry('400x400')
win.resizable(False, False)



myLabel1 = Label(win, text='Hello').place(x=10, y=10)
myLabel2 = Label(win, text='world').place(x=10, y=30)


win.mainloop()