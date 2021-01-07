chords = []
valid_input = ["x", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
               "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]

def readFile():
    f = open("chords.txt", "r")
    global chords
    chords = []
    for chord in f:
        chord = (chord.strip("\n")).split("|")
        chords.append(chord)
    f.close()
    writeFile()

def writeFile():
    f = open("chords.txt", "w")
    global chords
    chords.sort(key= lambda chords: chords[6])
    for chord in chords:
        text =chord[0] + "|" + chord[1] + "|" + chord[2] + "|" + chord[3] + "|" + chord[4] + "|" + chord[5] + "|" + chord[6]
        f.write(text + "\n")
    f.close()

def inputChord(chord, name):
    my_chord = (chord[0] + "|" + chord[1] + "|" + chord[2] + "|"+ chord[3] + "|" + chord[4] + "|"+ chord[5] + "|" + name)
    add = open("chords.txt","a")
    add.write(my_chord + "\n")
    add.close()

def checkChords(myChord):
    readFile()
    possibilities = [["", 0]]
    for chord in chords:
        score = 0
        i = 0
        for string in myChord:
            if string == chord[i]:
                score += 1
            i += 1
        if score == 6:
            return True, chord[6]
            break
        elif score > possibilities[0][1]:
            possibilities = [[chord[6], score]]
        elif score == possibilities[0][1]:
            possibilities.append([chord[6], score])
    return False, possibilities


def displayChord(query):
    readFile()
    shapes = []
    for chord in chords:
        if chord[6] == query:
            shapes.append(chord)
    if shapes == []:
        print("Sorry, we couldn't find that chord.")
    else:
        for chord in shapes:
            print("\ne|--" + chord[5] + "--")
            print("B|--" + chord[4] + "--")
            print("G|--" + chord[3] + "--")
            print("D|--" + chord[2] + "--")
            print("A|--" + chord[1] + "--")
            print("E|--" + chord[0] + "--\n")


