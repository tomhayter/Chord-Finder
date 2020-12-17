from tkinter import Tk, Canvas, PhotoImage, Button, messagebox, Label, StringVar, OptionMenu

def setup_window(width, height):
    window = Tk()
    window.title("Chord Finder")
    window.configure(background="black")
    window.geometry(str(width) + "x" + str(height))
    return window

width = 400
height = 400
window = setup_window(width, height)
window.minsize(width, height)
window.mainloop()
