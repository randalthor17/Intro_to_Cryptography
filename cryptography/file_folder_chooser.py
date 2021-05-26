from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

def file_chooser():
    main_win = Tk()
    main_win.withdraw()
    main_win.overrideredirect(True)
    main_win.geometry('0x0+0+0')
    main_win.deiconify()
    main_win.lift()
    main_win.focus_force()
    filename = askopenfilename()
    main_win.destroy()
    return filename

def folder_chooser():
    main_win = Tk()
    main_win.withdraw()
    main_win.overrideredirect(True)
    main_win.geometry('0x0+0+0')
    main_win.deiconify()
    main_win.lift()
    main_win.focus_force()
    foldername = askdirectory()
    return foldername
