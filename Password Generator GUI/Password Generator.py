#Password Generator ~ Enes Jashari
from tkinter import *
import random
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox


def password_generator():
	password_length = int(entry.get())
	if len(range(password_length)) > 60:
		messagebox.showinfo("Warning!", "Program allow at most 60 characters to be selected.")
	else:
		char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
		global password
		password = ''
		for i in range(password_length):
			password = password + random.choice(char)
		text_box.insert('1.0',password)


def reset_all():
    text_box.delete('1.0', END)
    entry.delete(0, 'end')


def save_button():
	files = [('All Files', '*.*'),
			('Python Files', '*.py'),
			('Text Document', '*.txt')]
	file = asksaveasfile(filetypes = files, defaultextension = files)
	with open('password.txt','w') as Nn:
		Nn.write(str(password))
		Nn.close()
		


#Window Geometry
root = Tk()
root.geometry("800x460")
root.config(bg="#CF9FFF")
root.resizable(width=False,height=False)
root.title('Password Generator')


#Labels
empty_label1 = Label(text='',bg="#CF9FFF")
empty_label2 = Label(text='',bg="#CF9FFF")
empty_label3 = Label(text='',bg="#CF9FFF")
label = Label(text='Enter the length of password',width=27,height=1)
e1= StringVar()
entry = Entry(font=(11),width=37,justify='center',textvariable=e1,)



#buttons
button = Button(text='Generate',command=password_generator)
reset = Button(text='Reset',width=7,command=reset_all)
btn = Button(root, text = 'Save',width=7, command = lambda : save_button())


#Text-Box
text_box = Text(height=5,width=53)



#Packing Everything Together
empty_label1.grid(row=0,column=0)
label.grid(row=17,column=0)
entry.grid(row=17,column=1)
button.grid(row=17,column=4)
reset.grid(row=24,column=4)
btn.grid(row=24,column=0)
empty_label3.grid(row=24,column=0)
empty_label2.grid(row=22,column=1)
text_box.grid(row=23,column=1)


root.mainloop()