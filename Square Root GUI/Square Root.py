#Square Root Calculator ~ Enes Jashari
from tkinter import *
import math

def squeare_root():
    number = int(entry.get())
    square = math.sqrt(number)
    label2.configure(text=f'The square root of {number} is \n {square}',font=0)



#Window Geometry
root = Tk()
root.geometry("500x460")
root.config(bg="#8D6E63")
root.resizable(width=False,height=False)
root.title('Calculator')



#labels
empty_label1 = Label(text='',bg="#8D6E63")
empty_label2 = Label(text='',width=15,bg="#8D6E63")
empty_label3 = Label(text='',width=37,bg="#8D6E63")
empty_label4 = Label(text='',width=37,bg="#8D6E63")
empty_label5 = Label(text='',width=37,bg="#8D6E63")
empty_label6 = Label(text='',width=37,bg="#8D6E63")
empty_label7 = Label(text='',width=37,bg="#8D6E63")
empty_label8 = Label(text='',width=37,bg="#8D6E63")


label = Label(text='Calculate The Square Root',width=30,height=1,bg="#EFEBE9")
label1 = Label(text='Enter the Numbers:',width=17,height=1,bg="#EFEBE9")
label2 = Label(text='No square is aviable!\nEnter a number above',width=25,height=3,bg="#EFEBE9")

e1= StringVar()
entry = Entry(font=(11),width=20,justify='center',textvariable=e1,)

#buttons
button = Button(text='Get the Square Root',fg="red",width=17,command=squeare_root)

#packing
empty_label1.grid(row=0,column=0)
empty_label2.grid(row=1,column=1)
empty_label3.grid(row=2,column=2)
empty_label4.grid(row=3,column=2)
empty_label5.grid(row=5,column=2)
empty_label6.grid(row=8,column=2)


label.grid(row=1,column=2)
label1.grid(row=4,column=2)
entry.grid(row=6,column=2)
button.grid(row=7,column=2)
label2.grid(row=9,column=2)

root.mainloop()