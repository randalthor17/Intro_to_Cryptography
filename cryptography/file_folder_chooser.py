from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

def file_chooser():
    Tk().withdraw()
    filename = askopenfilename()
    return filename

def folder_chooser():
    Tk().withdraw()
    foldername = askdirectory()
    return foldername