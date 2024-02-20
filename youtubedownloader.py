from pytube import YouTube
import tkinter as tk
from typing import List
    
def download(links:str|List[str]) -> None:
    for link in links:
        url = YouTube(link)
        video = url.streams.get_highest_resolution()
        try:
            if video == None:
                raise
            video.download()
        except:
            print("Error!")
    print("Completed!")

def process_text():
    text = inputBox.get("1.0",tk.END).split("\n")
    print(text)
    download(text)


window = tk.Tk()

greeting = tk.Label(text="Enter URL")
greeting.pack()

inputBox = tk.Text()
inputBox.pack()

downloadButton = tk.Button(text="Download",
                     width=10,
                     height=2,
                     bg="red",
                     fg="white",
                     command=process_text)
downloadButton.pack()

window.mainloop()