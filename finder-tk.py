from tkinter import Tk, Button, messagebox, Label, StringVar, OptionMenu, Frame, Entry, Message
import finderFunctionality as func

def setupWindow(width, height):
    window = Tk()
    window.title("Chord Finder")
    window.configure(background="black")
    window.geometry(str(width) + "x" + str(height))
    return window

def clearScreen():
    for widget in window.winfo_children():
        widget.pack_forget()

def menuButtonStyle(widget, size):
    widget.configure(bg="black", fg="white", font="Courier " +
                     str(size) + " bold")
    widget.configure(activebackground="white", activeforeground="black")
    return widget

def menuInputFret(noteValue):
    frets = ["x"]
    for i in range(0,22):
        frets.append(i)

    noteFrame = Frame(bg="black")
    initialNote = StringVar(window)
    initialNote.set("0")
    note = Label(noteFrame, text=noteValue, bg="black", fg="white",
              font="Courier 20 bold")
    note.pack(side="left")
    noteMenu = OptionMenu(noteFrame, initialNote, *frets)
    noteMenu["menu"] = menuButtonStyle(noteMenu['menu'], 10)
    noteMenu = menuButtonStyle(noteMenu, 10)
    noteMenu.pack(side="right", padx=10)
    return initialNote, noteFrame

def mainMenu():
    clearScreen()
    title = Label(window, text="Chord Finder", bg="black", fg="white",
                  font="Courier 40 bold")
    title.pack(pady=20)
    findChordButton = Button(window, text="Find a Chord", width="17", height="2",
                       command=lambda: findChord())
    findChordButton = menuButtonStyle(findChordButton, 20)
    findChordButton.pack(pady=10)
    addChordButton = Button(window, text="Add a Chord", width="17", height="2",
                       command=lambda: addChord())
    addChordButton = menuButtonStyle(addChordButton, 20)
    addChordButton.pack(pady=10)
    learnChordButton = Button(window, text="Learn a Chord", width="17", height="2",
                       command=lambda: learnChord())
    learnChordButton = menuButtonStyle(learnChordButton, 20)
    learnChordButton.pack(pady=10)
    quitButton = Button(window, text="Quit", width="17", height="2",
                       command=lambda: quitSure())
    quitButton = menuButtonStyle(quitButton, 20)
    quitButton.pack(pady=10)

def find(chord):
    clearScreen()
    match, possibilities = func.checkChords(chord)
    title = Label(window, text="Find a Chord", bg="black", fg="white",
                  font="Courier 40 bold")
    title.pack(pady=20)
    if match:
        result = Label(window, text="Your chord is "+ possibilities[0], bg="black", fg="white",
                       font="Courier 20 bold")
    else:
        names = ""
        for chrd in possibilities:
            names = names + chrd[0] + " "
        names = names + "."
        result = Message(window, text="We could not find your chord in our dictionary. Our closest matches are: " + names,
                         bg="black", fg="white", font="Courier 20 bold")
    result.pack(pady=10)
    backButton = Button(window, text="Back", width="12", height="1",
                        command=lambda: mainMenu())
    backButton = menuButtonStyle(backButton, 10)
    backButton.pack(pady=10)

def findChord():
    clearScreen()
    title = Label(window, text="Find a Chord", bg="black", fg="white",
                  font="Courier 40 bold")
    title.pack(pady=20)
    instruction = Label(window, text="Please enter a chord:", bg="black", fg="white",
                        font="Courier 20 bold")
    instruction.pack(pady=5)
    frets = list(range(0,22))

    bigEVal, bigEFrame = menuInputFret("E")
    bigEFrame.pack(pady=5)
    aVal, aFrame = menuInputFret("A")
    aFrame.pack(pady=5)
    dVal, dFrame = menuInputFret("D")
    dFrame.pack(pady=5)
    gVal, gFrame = menuInputFret("G")
    gFrame.pack(pady=5)      
    bVal, bFrame = menuInputFret("B")
    bFrame.pack(pady=5)
    eVal, eFrame = menuInputFret("e")
    eFrame.pack(pady=5)

    findButton = Button(window, text="Find Chord", width="12", height="1",
                        command=lambda: find([bigEVal.get(), aVal.get(), dVal.get(), gVal.get(), bVal.get(), eVal.get()]))
    findButton = menuButtonStyle(findButton, 10)
    findButton.pack(pady=10)
    
    backButton = Button(window, text="Back", width="12", height="1",
                        command=lambda: mainMenu())
    backButton = menuButtonStyle(backButton, 10)
    backButton.pack(pady=10)

def add(chord, name):
    clearScreen()
    func.inputChord(chord, name)
    title = Label(window, text="Chord Added", bg="black", fg="white",
                  font="Courier 40 bold")
    title.pack(pady=20)
    backButton = Button(window, text="Back", width="12", height="1",
                       command=lambda: mainMenu())
    backButton = menuButtonStyle(backButton, 10)
    backButton.pack(pady=10)
    

def addChord():
    clearScreen()
    title = Label(window, text="Add a Chord", bg="black", fg="white",
                  font="Courier 40 bold")
    title.pack(pady=20)
    instruction = Label(window, text="Please enter a chord:", bg="black", fg="white",
                        font="Courier 20 bold")
    instruction.pack(pady=5)
    
    bigEVal, bigEFrame = menuInputFret("E")
    bigEFrame.pack(pady=5)
    aVal, aFrame = menuInputFret("A")
    aFrame.pack(pady=5)
    dVal, dFrame = menuInputFret("D")
    dFrame.pack(pady=5)
    gVal, gFrame = menuInputFret("G")
    gFrame.pack(pady=5)      
    bVal, bFrame = menuInputFret("B")
    bFrame.pack(pady=5)
    eVal, eFrame = menuInputFret("e")
    eFrame.pack(pady=5)

    nameFrame = Frame(bg="black")
    nameLabel = Label(nameFrame, text="Name", bg="black", fg="white",
                      font="Courier 20 bold")
    nameLabel.pack(side="left")
    name = Entry(nameFrame)
    name.pack(side="right", padx=10)
    nameFrame.pack(pady=5)
    
    addButton = Button(window, text="Add Chord", width="12", height="1",
                       command=lambda: add([bigEVal.get(), aVal.get(), dVal.get(), gVal.get(), bVal.get(), eVal.get()], name.get()))
    addButton = menuButtonStyle(addButton, 10)
    addButton.pack(pady=10)
    
    backButton = Button(window, text="Back", width="12", height="1",
                       command=lambda: mainMenu())
    backButton = menuButtonStyle(backButton, 10)
    backButton.pack(pady=10)   

def learn(name):
    clearScreen()
    shapes = func.getChord(name)
    title = Label(window, text="Learn a Chord", bg="black", fg="white",
                  font="Courier 40 bold")
    title.pack(pady=20)
    if shapes == []:
        notFound = Message(window, text="Sorry, we could not find that chord.",
                           bg="black", fg="white", font="Courier 20 bold")
        notFound.pack(pady=10)
    else:
        chd = Label(window, text=name+":", bg="black", fg="white",
                    font="Courier 20 bold")
        chd.pack(pady=10)
        strings = ["E|---","A|--","D|--","G|--","B|--","e|--"]
        for i in range(6):
            for chord in shapes:
                strings[i] = strings[i] + chord[i] + "---"
            label = Label(window, text=strings[i], bg="black", fg="white",
                          font="Courier 15 bold")
            label.pack(pady=5)
    backButton = Button(window, text="Back", width="12", height="1",
                       command=lambda: mainMenu())
    backButton = menuButtonStyle(backButton, 10)
    backButton.pack(pady=10)

def learnChord():
    clearScreen()
    title = Label(window, text="Learn a Chord", bg="black", fg="white",
                  font="Courier 40 bold")
    title.pack(pady=20)
    instruction = Label(window, text="Please enter a chord:", bg="black", fg="white",
                        font="Courier 20 bold")
    instruction.pack(pady=5)

    chordInput = Entry(window)
    chordInput.pack(pady=10)

    submitButton = Button(window, text="Learn", width="12", height="1",
                       command=lambda: learn(chordInput.get()))
    submitButton = menuButtonStyle(submitButton, 10)
    submitButton.pack(pady=10) 
    
    backButton = Button(window, text="Back", width="12", height="1",
                       command=lambda: mainMenu())
    backButton = menuButtonStyle(backButton, 10)
    backButton.pack(pady=10)

def quitSure():
    sure = messagebox.askyesno("Are you sure?",
                               "Are you sure you want to quit?")
    if sure:
        window.destroy()

width = 450
height = 580
window = setupWindow(width, height)
window.minsize(width, height)
mainMenu()
window.mainloop()
