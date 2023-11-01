from gtts import gTTS
import os
from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=300)
canvas.pack()


def input_to_speech():
    text = entry.get()
    output = gTTS(text=text, lang='en', slow=False)
    output.save('audio.mp3')
    os.system('start audio.mp3')


entry = Entry(root)
canvas.create_window(200, 180, window=entry)
btn = Button(text="record", command=input_to_speech)
canvas.create_window(200, 230, window=btn)

root.mainloop()
