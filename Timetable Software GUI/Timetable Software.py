import tkinter as tk
from base64 import encode
import encodings
from tkinter import filedialog
import csv
from tkinter.ttk import Combobox
from tkinter import messagebox
import re
from tkinter import *

class TimeTable(object):
    def __init__(self, root):

        #Samledata entry design        
        FilePath=Label(root, width=15)
        FilePath.config(text="Enter the file Path: ", bg="White")
        FilePath.grid(row=2, column=1, padx=(5, 10), pady=(20, 0))
        
        #Year entry design
        year=Label(root, width=15)
        year.config(text="Year: ", bg="White")
        year.grid(row=4, column=1, padx=(5, 10), pady=(20, 0))
        
        #Departament entry design
        department=Label(root, width=15)
        department.config(text="Department: ",bg="White")
        department.grid(row=4, column=3, padx=(5, 10), pady=(20, 0))
        
        #Warning design of 'You can choose only 6 courses'
        warnings=Label(root, width=15)
        warnings.config(text="Warnings: ", bg="White")
        warnings.grid(row=6, column=1, padx=(0, 0), pady=(50, 0), sticky=W)
        
        courses=Label(root, width=15)
        courses.config(text="Courses: ", bg="White")
        courses.grid(row=6, column=4, padx=(0, 0), pady=(50, 0), sticky=W)

        #Entry of sampledata path.
        self.pathEntry=Entry(root)
        self.pathEntry.grid(row=2, column=2, padx=(0, 0), pady=(20, 0), columnspan=2, sticky=W+E)

        #Entry of departament path.        
        self.departmentEntry=Entry(root)
        #for each Entry,Label,Button etc.A grid is attached that is used to design preview variable.
        self.departmentEntry.grid(row=4, column=4, padx=(0, 0), pady=(20, 0), columnspan=2)
        
        self.comboBox = Combobox(root)
        self.comboBox.bind('<<ComboboxSelected>>')
        self.comboBox.grid(row=4, column=2, padx=(5, 10), pady=(20, 0))
        self.comboBox['values']=(1, 2, 3, 4, 5)
        self.comboBox.current(0)
        
        #Primary button
        btnDisplay=Button(root) 
        btnDisplay.config(text="Display", bg="white", command=self.display)
        btnDisplay.grid(row=5, column=1, sticky=E, padx=(0, 10), pady=(50, 0))
        
        #This clear the data that was stored by the user.
        btnClear=Button(root)
        btnClear.config(text="Clear", bg="white", command=self.clear)
        btnClear.grid(row=5, column=2, sticky=W+E, padx=(0, 10), pady=(50, 0))
    
        #Save information.
        btnSave=Button(root)
        btnSave.config(text="Save", bg="white", command=self.save)
        btnSave.grid(row=5, column=3, sticky=W+E, padx=(0, 10), pady=(50, 0))
        
        self.warBox=Listbox(root, width=65)
        self.warBox.grid(row=7, column=1, columnspan=3, pady=(50,0), sticky=E+W)

        self.coursesBox=Listbox(root, width=65)
        self.coursesBox.bind("<Double-1>", self.click)
        self.coursesBox.grid(row=7, column=4, columnspan=3, padx=(10, 0), pady=(50,0), sticky=E+W)

        

    def display(self):
        csv_file=self.pathEntry.get()
        #This line open the sampledata file in reading mode 
        file=open(str(csv_file), 'r', encoding="unicode_escape")
        courses=list()        
        #This line iterate in each line row of sampledata file and append them in courses
        for each_row in file:
            courses.append(each_row)
        #This line iterate and select the rows who started with a specific letter
        for each_element in courses:
            if (each_element.split(' ')[0].startswith(self.departmentEntry.get().upper())) and (each_element.split(' ')[0].endswith(self.departmentEntry.get().upper())) and (each_element.split(' ')[1].startswith(self.comboBox.get())):
                self.coursesBox.insert(END, each_element)
    #All this line do is clear the entry of year/department/file and also clear the output
    def clear(self):
        self.pathEntry.delete(0, END)
        self.comboBox.delete(0, END)
        self.departmentEntry.delete(0, END)
        self.coursesBox.delete(0, END)
        self.warBox.delete(0, END)
    
    #This one is about the warning message,for not allowing more than 6 courses to be selected.
    global lista
    lista=[]
    def click(self, event):
        selection=event.widget.curselection()
        if self.warBox.size() > 5:
            messagebox.showinfo("Warning!", "Program allow at most 6 courses to be selected.")
        else:
            for i in selection:
                self.f_selected = event.widget.get(i)
                self.warlist = self.warBox.get(0, END)
                fo_selected = self.f_selected.split(',')[2]
                fif_selected = fo_selected.split(' ')[0]
                # This split the line if its too long.
                if  (len(selection) <= 6) and selection:
                    th_selected = self.f_selected.split(',')[0]
                    se_selected = self.f_selected.split(',')
                    if (f"Added {th_selected}") not in self.warlist:
                        self.warBox.insert(0, (f"Added {th_selected}"))
        event_1=event.widget
        click_select = event_1.curselection()
        if click_select:
            for each_select in click_select: 
                global save_select
                save_select=event_1.get(each_select)
        lista.append(save_select)    
    #This save data that was given.
    def save(self):
        save_csv=open("sampledata.csv", 'w')
        write = csv.writer(save_csv)
        #This split the rows
        for each_row in lista:
            write.writerow(each_row.split(", "))
        save_csv.close()
#Design of project.
def main():
    root = Tk()
    ex=TimeTable(root)
    root.geometry("820x500+300+300")
    root.minsize(820,500)
    root.maxsize(820,500)
    root.config(bg="Gray")
    root.mainloop()

main()
    
