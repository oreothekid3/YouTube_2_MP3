#framework to create a GUI
from tkinter import *
from tkinter import ttk

#library for downloading videos from youtube
from pytube import YouTube

#Creating display window

#initialize tkinter: creating display window
main = Tk()
#set window width and height
main.geometry('500x250')
#set the fixed size of window(not resizable)
main.resizable(0,0)
#title of the window
main.title('YouTube to MP3 Convertor')
#Label displays text that is unmodifable by user
#pack() organizes text into a block
Label(main, text = 'YouTube to MP3', font = 'arial 30 bold').pack()

#Field for entering link

#store the link as a string var
link = StringVar()
Label(main, text = 'Paste Link Here:', font = 'arial 20 bold').place(x = 150, y = 80)
link_enter = Entry(main, width = 53, textvariable = link).place(x = 85, y = 120)

#Function for entering link

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(main, text = 'DOWNLOADED', font = 'arial 15').place(x = 180, y = 210)

Button(main, text = 'DOWNLOAD', font = 'arial 15 bold', bg = 'pale violet red', padx = 2, command = Downloader).place(x = 180, y = 160)



main.mainloop()