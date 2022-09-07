from tkinter import *
from tkinter import messagebox

def tempconver():
    entry1 = entry.get()
    f_entry = (int(entry1) * 9/5) + 32
    text_box.delete('1.0', END)
    text_box.insert('1.0',f_entry)
    messagebox.showinfo("Successfully", f"{entry1} °C converted to {f_entry} ℉.")


def reset_all():
    text_box.delete('1.0', END)
    entry.delete(0, 'end')

root = Tk()


root.geometry("500x460")
root.config(bg="#8FBC8F")
root.resizable(width=False,height=False)
root.title('Temperature Convertor')

#labels
label =Label(text='Convert Celsius to Fahrenheit ')


#entry
e1= IntVar()
entry = Entry(font=(11),width=50,justify='center',textvariable=e1)
entry.delete(0,"end")

#button
button = Button(text='Submit',command=tempconver)
reset = Button(text='Reset',command=reset_all,font=(12))

text_box = Text(height=5,width=50)


#pack

label.pack()
entry.pack()
button.pack()
reset.pack()
text_box.pack()


root.mainloop()