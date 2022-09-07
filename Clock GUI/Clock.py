# Enes Jashari ~ Clock
#Importing Modeules
from tkinter import *
from time import strftime

root = Tk()
root.geometry("250x50")
root.resizable(width=False,height=False)
root.title('Clock')

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font = ('calibri', 35, 'bold'),
            background = 'blue',
            foreground = 'white')
label.pack()
time()
root.mainloop()