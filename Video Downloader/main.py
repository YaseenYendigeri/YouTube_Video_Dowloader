from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil

root = Tk()


def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def mp3():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print("Downloading")
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    audio = video_clip.audio
    audio.write_audiofile('audio.mp3')
    video_clip.close()
    shutil.move("audio.mp3", file_path)
    print("Downloaded")


def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print("Downloading")
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    video_clip.close()
    shutil.move(mp4, file_path)
    print("Downloaded")


root.title("Video Downloader")
canvas = Canvas(root, width=400, height=300)
canvas.pack()

app_label = Label(root, text="Video_Downloader", fg="blue", font=('arial',20))
canvas.create_window(200,20,window=app_label)

url_label = Label(root, text="Url")
canvas.create_window(200,80,window=url_label)

url_entry = Entry(root)
canvas.create_window(200,100,window=url_entry)

path_label = Label(root, text="Select path")
canvas.create_window(200,150,window=path_label)

path_button = Button(root, text="Select", command=get_path)
canvas.create_window(200,170,window=path_button)

download_button = Button(root, text="Download", command=download)
canvas.create_window(300,250,window=download_button)

download_Mp3 = Button(root, text="Download Mp3", command=mp3)
canvas.create_window(100,250,window=download_Mp3)

root.mainloop()



