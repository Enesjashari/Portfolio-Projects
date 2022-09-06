import tkinter as tk


window = tk.Tk()
window.geometry("500x460")
window.config(bg="#add8e6")
window.resizable(width=False,height=False)
window.title('Email Slicer')


def email_brain():
    email = entry.get()
    updated_email = email.strip()
    username = updated_email[0:updated_email.index('@')]
    domain = updated_email[updated_email.index('@') + 1:]
    text_box.delete('1.0', tk.END)
    msg = 'Email given is: {0}\n\nEmail is: {1}\n\nDomain is: {2}'.format(updated_email,username,domain)
    text_box.insert(tk.END,msg)

def reset_all():
    text_box.delete('1.0', tk.END)
    entry.delete(0, 'end')



#Labels
label1 = tk.Label(text='',background="#add8e6",font=(25))
label2 = tk.Label(text='',background="#add8e6",font=(12))
label3 = tk.Label(text='Enter you email here',font=(12))
empty_label1=tk.Label(background="#add8e6")
empty_label2=tk.Label(background="#add8e6")
empty_label3=tk.Label(background="#add8e6")
empty_label4=tk.Label(background="#add8e6")


#Entry
e1=tk.StringVar()
entry = tk.Entry(font=(11),width=50,justify='center',textvariable=e1)

#Button
button = tk.Button(text='Submit',command=email_brain,font=(12))
reset = tk.Button(text='Reset',command=reset_all,font=(12))

text_box = tk.Text(height=5,width=50)



#Packing Everything Together
label1.pack()
label2.pack()
label3.pack()
empty_label1.pack()
entry.pack()
empty_label4.pack()
button.pack()
empty_label2.pack()
reset.pack()
empty_label3.pack()
text_box.pack()


window.mainloop()














