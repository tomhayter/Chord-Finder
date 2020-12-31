from tkinter import Tk, Button, messagebox, Label, StringVar, OptionMenu, Frame

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

def findChord():
    clearScreen()
    title = Label(window, text="Find a Chord", bg="black", fg="white",
                  font="Courier 40 bold")
    title.pack(pady=20)
    instruction = Label(window, text="Please enter a chord:", bg="black", fg="white",
                        font="Courier 20 bold")
    instruction.pack(pady=5)
    frets = list(range(0,22))

    bigEFrame = Frame(bg="black")
    initialBigE = StringVar(window)
    initialBigE.set("0")
    bigE = Label(bigEFrame, text="E", bg="black", fg="white",
              font="Courier 20 bold")
    bigE.pack(side="left")
    bigEMenu = OptionMenu(bigEFrame, initialBigE, *frets)
    bigEMenu["menu"] = menuButtonStyle(bigEMenu['menu'], 10)
    bigEMenu = menuButtonStyle(bigEMenu, 10)
    bigEMenu.pack(side="right", padx=10)
    bigEFrame.pack(pady=5)

    aFrame = Frame(bg="black")
    initialA = StringVar(window)
    initialA.set("0")
    a = Label(aFrame, text="A", bg="black", fg="white",
              font="Courier 20 bold")
    a.pack(side="left")
    aMenu = OptionMenu(aFrame, initialA, *frets)
    aMenu["menu"] = menuButtonStyle(aMenu['menu'], 10)
    aMenu = menuButtonStyle(aMenu, 10)
    aMenu.pack(side="right", padx=10)
    aFrame.pack(pady=5)

    dFrame = Frame(bg="black")
    initialD = StringVar(window)
    initialD.set("0")
    d = Label(dFrame, text="D", bg="black", fg="white",
              font="Courier 20 bold")
    d.pack(side="left")
    dMenu = OptionMenu(dFrame, initialD, *frets)
    dMenu["menu"] = menuButtonStyle(dMenu['menu'], 10)
    dMenu = menuButtonStyle(dMenu, 10)
    dMenu.pack(side="right", padx=10)
    dFrame.pack(pady=5)

    gFrame = Frame(bg="black")
    initialG = StringVar(window)
    initialG.set("0")
    g = Label(gFrame, text="G", bg="black", fg="white",
              font="Courier 20 bold")
    g.pack(side="left")
    gMenu = OptionMenu(gFrame, initialG, *frets)
    gMenu["menu"] = menuButtonStyle(gMenu['menu'], 10)
    gMenu = menuButtonStyle(gMenu, 10)
    gMenu.pack(side="right", padx=10)
    gFrame.pack(pady=5)
                   
    bFrame = Frame(bg="black")
    initialB = StringVar(window)
    initialB.set("0")
    b = Label(bFrame, text="B", bg="black", fg="white",
              font="Courier 20 bold")
    b.pack(side="left")
    bMenu = OptionMenu(bFrame, initialB, *frets)
    bMenu["menu"] = menuButtonStyle(bMenu['menu'], 10)
    bMenu = menuButtonStyle(bMenu, 10)
    bMenu.pack(side="right", padx=10)
    bFrame.pack(pady=5)

    eFrame = Frame(bg="black")
    initialE = StringVar(window)
    initialE.set("0")
    e = Label(eFrame, text="e", bg="black", fg="white",
              font="Courier 20 bold")
    e.pack(side="left")
    eMenu = OptionMenu(eFrame, initialE, *frets)
    eMenu["menu"] = menuButtonStyle(eMenu['menu'], 10)
    eMenu = menuButtonStyle(eMenu, 10)
    eMenu.pack(side="left", padx=10)
    eFrame.pack(pady=5)

    findButton = Button(window, text="Find Chord", width="12", height="1",
                        command=lambda: findFunction())
    findButton = menuButtonStyle(findButton, 10)
    findButton.pack(pady=10)
    
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
    frets = list(range(0,22))

    bigEFrame = Frame(bg="black")
    initialBigE = StringVar(window)
    initialBigE.set("0")
    bigE = Label(bigEFrame, text="E", bg="black", fg="white",
                 font="Courier 20 bold")
    bigE.pack(side="left")
    bigEMenu = OptionMenu(bigEFrame, initialBigE, *frets)
    bigEMenu["menu"] = menuButtonStyle(bigEMenu['menu'], 10)
    bigEMenu = menuButtonStyle(bigEMenu, 10)
    bigEMenu.pack(side="right", padx=10)
    bigEFrame.pack(pady=5)

    aFrame = Frame(bg="black")
    initialA = StringVar(window)
    initialA.set("0")
    a = Label(aFrame, text="A", bg="black", fg="white",
              font="Courier 20 bold")
    a.pack(side="left")
    aMenu = OptionMenu(aFrame, initialA, *frets)
    aMenu["menu"] = menuButtonStyle(aMenu['menu'], 10)
    aMenu = menuButtonStyle(aMenu, 10)
    aMenu.pack(side="right", padx=10)
    aFrame.pack(pady=5)

    dFrame = Frame(bg="black")
    initialD = StringVar(window)
    initialD.set("0")
    d = Label(dFrame, text="D", bg="black", fg="white",
              font="Courier 20 bold")
    d.pack(side="left")
    dMenu = OptionMenu(dFrame, initialD, *frets)
    dMenu["menu"] = menuButtonStyle(dMenu['menu'], 10)
    dMenu = menuButtonStyle(dMenu, 10)
    dMenu.pack(side="right", padx=10)
    dFrame.pack(pady=5)

    gFrame = Frame(bg="black")
    initialG = StringVar(window)
    initialG.set("0")
    g = Label(gFrame, text="G", bg="black", fg="white",
              font="Courier 20 bold")
    g.pack(side="left")
    gMenu = OptionMenu(gFrame, initialG, *frets)
    gMenu["menu"] = menuButtonStyle(gMenu['menu'], 10)
    gMenu = menuButtonStyle(gMenu, 10)
    gMenu.pack(side="right", padx=10)
    gFrame.pack(pady=5)
                   
    bFrame = Frame(bg="black")
    initialB = StringVar(window)
    initialB.set("0")
    b = Label(bFrame, text="B", bg="black", fg="white",
              font="Courier 20 bold")
    b.pack(side="left")
    bMenu = OptionMenu(bFrame, initialB, *frets)
    bMenu["menu"] = menuButtonStyle(bMenu['menu'], 10)
    bMenu = menuButtonStyle(bMenu, 10)
    bMenu.pack(side="right", padx=10)
    bFrame.pack(pady=5)

    eFrame = Frame(bg="black")
    initialE = StringVar(window)
    initialE.set("0")
    e = Label(eFrame, text="e", bg="black", fg="white",
              font="Courier 20 bold")
    e.pack(side="left")
    eMenu = OptionMenu(eFrame, initialE, *frets)
    eMenu["menu"] = menuButtonStyle(eMenu['menu'], 10)
    eMenu = menuButtonStyle(eMenu, 10)
    eMenu.pack(side="left", padx=10)
    eFrame.pack(pady=5)

    addButton = Button(window, text="Add Chord", width="12", height="1",
                       command=lambda: addFunction())
    addButton = menuButtonStyle(addButton, 10)
    addButton.pack(pady=10)
    
    backButton = Button(window, text="Back", width="12", height="1",
                       command=lambda: mainMenu())
    backButton = menuButtonStyle(backButton, 10)
    backButton.pack(pady=10)   
    

width = 400
height = 560
window = setupWindow(width, height)
window.minsize(width, height)
mainMenu()
window.mainloop()
