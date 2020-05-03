from pytube import *
from tkinter.filedialog import *
from tkinter.messagebox import showinfo, showerror
from threading import *

file_size = 0

def progress(stream=None, chunk=None, remaining=None):
    file_downloaded = (file_size - remaining)
    per = (file_downloaded / file_size)*100
    DownloadBtn.config(text=f"{per:.0f} % download")

def startDownload():
    global file_size
    try:
        # get Url
        url = urlField.get()
        print(url)
        # Config Download Button text and disable
        DownloadBtn.config(text='Please wait...')
        DownloadBtn.config(state=DISABLED)
        # Get Directory
        path_to_save = askdirectory()
        print(path_to_save)

        if(path_to_save is None):
            return

        obj = YouTube(url, on_progress_callback=progress)
        strm = obj.streams.first()

        file_size = strm.filesize
        print(file_size)
        vTitle.config(text=strm.title)

        strm.download(path_to_save)
        print('Done...')
        DownloadBtn.config(text='Start Download')
        DownloadBtn.config(state=NORMAL)
        showinfo("Downloaded Finished", "Downloaded Successfully!")
        urlField.delete(0, END)
        vTitle.config(text="Download Link Paste Below !")

    except Exception as e:
        print(e)
        showerror("Download Failed", "Something went Wrong!")
        DownloadBtn.config(text='Start Download')
        DownloadBtn.config(state=NORMAL)
        urlField.delete(0, END)
        vTitle.config(text="Download Link Paste Below !")

def startDownloadThread():
    thread = Thread(target=startDownload)
    thread.start()

from tkinter import *

# UI Start
root = Tk()
root.title("Youtube Downloader !")
root.iconbitmap('./logo/icon.ico')
root.geometry("500x400")
root.maxsize(500,400)
root.minsize(500,400)

file = PhotoImage(file='./logo/bg.png')
headingIcon = Label(root, image=file)
headingIcon.pack()
# Video Title
vTitle = Label(root, text="Download Link Paste Below !", font=('verdana', 14))
vTitle.pack(side=TOP, pady=10)
# Url Field
urlField = Entry(root, font=('verdana', 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, pady=10)
# Button Download
DownloadBtn = Button(root, text="Start Download", font=('verdana', 18), relief=RAISED, command=startDownloadThread)
DownloadBtn.pack(side=TOP, pady=10)

root.mainloop()
