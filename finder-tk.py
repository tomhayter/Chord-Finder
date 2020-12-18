from tkinter import Tk, Canvas, PhotoImage, Button, messagebox, Label, StringVar, OptionMenu

def setup_window(width, height):
    window = Tk()
    window.title("Chord Finder")
    window.configure(background="black")
    window.geometry(str(width) + "x" + str(height))
    return window

def menu_button_style(widget, size):
    widget.configure(bg="black", fg="white", font="Courier " +
                     str(size) + " bold")
    widget.configure(activebackground="white", activeforeground="black")
    return widget

def main_menu():
    title = Label(window, text="Chord Finder", bg="black", fg="white",
                  font="Courier 40 bold")
    title.pack(pady=20)
    findChordButton = Button(window, text="Find a Chord", width="17", height="2",
                       command=lambda: findChord())
    findChordButton = menu_button_style(findChordButton, 20)
    findChordButton.pack(pady=10)
    addChordButton = Button(window, text="Add a Chord", width="17", height="2",
                       command=lambda: addChord())
    addChordButton = menu_button_style(addChordButton, 20)
    addChordButton.pack(pady=10)
    learnChordButton = Button(window, text="Learn a Chord", width="17", height="2",
                       command=lambda: learnChord())
    learnChordButton = menu_button_style(learnChordButton, 20)
    learnChordButton.pack(pady=10)
    quitButton = Button(window, text="Quit", width="17", height="2",
                       command=lambda: quit_sure())
    quitButton = menu_button_style(quitButton, 20)
    quitButton.pack(pady=10)
    
    

width = 400
height = 560
window = setup_window(width, height)
window.minsize(width, height)
main_menu()
window.mainloop()
