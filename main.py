from gtts import gTTS
from tkinter import *
from tkinter import filedialog as fd
import os
from pathlib import Path

filepath = None

window = Tk()
window.title('Text-To-Speech App')
window.geometry('200x100')


def choose_file():
    global filepath
    filepath = fd.askopenfilename(title="Select a file")
    read_content()


def read_content():
    global filepath
    content = get_content()
    try:
        language = 'en'
        tts_obj = gTTS(text=content, lang=language, slow=False)
        filename = f"{Path(filepath).name.split('.')[0]}"
        # print(filename)
        tts_obj.save(f"{filename}.mp3")
        os.system(f"start {filename}.mp3")
    except AssertionError as message:
        button.destroy()
        text = Label(text=message, fg="red")
        text.pack(expand=True)


def get_content():
    global filepath
    # print(filepath)
    content = ""
    try:
        with open(file=f"{filepath}") as file:
            content += file.read()
    except FileNotFoundError:
        pass
    return content


button = Button(text='Select a file', command=choose_file)
button.pack(expand=True)

window.mainloop()
