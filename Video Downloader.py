#Video Downloader ~ Enes Jashari
from pytube import YouTube
from tkinter import *


def video_downloader():
    entry1 = str(entry.get())
    entry_url = entry1[:]
    video  = YouTube(entry_url)
    video_title = video.title
    if len(video_title) > 50:
        a = video_title[0:31]
        b =video_title[31:]
        label3.config(text=f'{a}\n{b}',height=2)
    else:
        label3.config(text=video_title)
    video_finish = video.streams.get_by_itag(22)
    video_finish.download()
    label5.config(text='Download Completed',fg="#00CC00")

#Window Geometry
root = Tk()
root.geometry("500x400")
root.config(bg="#FF0000")
root.resizable(width=False,height=False)
root.title('Video Downloader for Youtube')


#labels
empty_label1 = Label(text='',bg="#FF0000")
empty_label2 = Label(text='',width=15,bg="#FF0000")
empty_label3 = Label(text='',width=37,bg="#FF0000")
empty_label4 = Label(text='',width=37,bg="#FF0000")
empty_label5 = Label(text='',width=37,bg="#FF0000")
empty_label6 = Label(text='',width=37,bg="#FF0000")
empty_label7 = Label(text='',width=37,bg="#FF0000")
empty_label8 = Label(text='',width=37,bg="#FF0000")
empty_label9 = Label(text='',width=37,bg="#FF0000")
empty_label10 = Label(text='',width=37,bg="#FF0000")
label = Label(text='Download Youtube Video',width=30,height=1,bg="#EFEBE9")
label1 = Label(text='Enter Video URL below:',width=17,height=1,bg="#EFEBE9")
label2 = Label(text='Video Title:',width=25,height=1,bg="#EFEBE9")
label3 = Label(text='No Title Aviable!',width=40,height=1,bg="#EFEBE9")
label4 = Label(text='Download Status:',width=25,height=1,bg="#EFEBE9")
label5 = Label(text='No URL to Download!:',fg="#FF0033",width=25,height=1,bg="#EFEBE9")



e1= StringVar()
entry = Entry(width=35,justify='center',textvariable=e1)

#buttons
button = Button(text='Download Video',bg="green",fg='white',width=17,command=video_downloader)

#packing
empty_label1.grid(row=0,column=0)
empty_label2.grid(row=1,column=1)
empty_label3.grid(row=2,column=2)
empty_label4.grid(row=3,column=2)
empty_label5.grid(row=5,column=2)
empty_label6.grid(row=8,column=2)
empty_label7.grid(row=11,column=2)
empty_label8.grid(row=13,column=2)
label.grid(row=1,column=2)
label1.grid(row=4,column=2)
entry.grid(row=6,column=2)
button.grid(row=7,column=2)
label2.grid(row=9,column=2)
label3.grid(row=10,column=2)
label4.grid(row=12,column=2)
label5.grid(row=14,column=2)


root.mainloop()