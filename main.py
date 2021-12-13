####last thing i left off at was trying to convert downloaded audio file to mp3 extention 


import os
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

#store the link as a string var
link = StringVar()
Label(main, text = 'Paste Link Here:', font = 'arial 20 bold').place(x = 150, y = 80)
link_enter = Entry(main, width = 53, textvariable = link).place(x = 85, y = 120)

#Function for entering link

def Video_Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(main, text = 'DOWNLOADED', font = 'arial 15').place(x = 180, y = 210)

def Audio_Downloader():
    url = YouTube(str(link.get()))
    audio = url.streams.filter(only_audio=True).first()
    downloaded_audio = audio.download()
    base, ext = os.path.splitext(downloaded_audio)
    new_file = base + '.mp3'
    os.rename(downloaded_audio, new_file)
    Label(main, text = 'AUDIO DOWNLOADED', font = 'arial 15').place(x = 180, y = 210)

Button(main, text = 'VIDEO DOWNLOAD', font = 'arial 15 bold', bg = '#FF0000', padx = 2, command = Video_Downloader).place(x = 180, y = 160)
Button(main, text = 'AUDIO DOWNLOAD', font = 'arial 15 bold', bg = '#FF0000', padx = 2, command = Audio_Downloader).place(x = 180, y = 200)



main.mainloop()