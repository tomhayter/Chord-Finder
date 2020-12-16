chords = []
valid_input = ["x", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
               "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]

def read_file():
    f = open("chords.txt", "r")
    global chords
    chords = []
    for chord in f:
        chord = (chord.strip("\n")).split("|")
        chords.append(chord)
    f.close()
    write_file()

def write_file():
    f = open("chords.txt", "w")
    global chords
    chords.sort(key= lambda chords: chords[6])
    for chord in chords:
        text =chord[0] + "|" + chord[1] + "|" + chord[2] + "|" + chord[3] + "|" + chord[4] + "|" + chord[5] + "|" + chord[6]
        f.write(text + "\n")
    f.close()


def menu():
    print("\nMENU\n")
    print("1. Find a chord.")
    print("2. Input a chord into the databse.")
    print("3. How to play a chord.")
    print("4. Exit.")
    choice = 0
    while choice not in ["1", "2", "3", "4"]:
        choice = input("\nEnter 1, 2, 3 or 4: ")
    if choice == "1":
        get_chord()
    elif choice == "2":
        input_chord()
    elif choice == "3":
        display_chord()
    elif choice == "4":
        pass


def input_chord():
    e = a = d = g = b = high_e = ""
    while e not in valid_input:
        e = input("E: ")
    while a not in valid_input:
        a = input("A: ")
    while d not in valid_input:
        d = input("D: ")
    while g not in valid_input:
        g = input("G: ")
    while b not in valid_input:
        b = input("B: ")
    while high_e not in valid_input:
        high_e = input("e: ")
    name = input("Name: ")

    my_chord = (e + "|" + a + "|" + d + "|"+ g + "|" + b + "|"+ high_e + "|" + name)
    add = open("chords.txt","a")
    add.write(my_chord + "\n")
    add.close()
    menu()


def get_chord():
    e = a = d = g = b = high_e = ""
    while e not in valid_input:
        e = input("E: ")
    while a not in valid_input:
        a = input("A: ")
    while d not in valid_input:
        d = input("D: ")
    while g not in valid_input:
        g = input("G: ")
    while b not in valid_input:
        b = input("B: ")
    while high_e not in valid_input:
        high_e = input("e: ")

    my_chord = [e, a, d, g, b, high_e]
    matching_chord, possibilities = check_chords(my_chord)
    if not matching_chord:
        print("\nThis chord does not match a chord in our dictionary. Our closest matches are: ")
        for chord in possibilities:
            print(chord[0])
    else:
        print("\nYour chord is " + matching_chord)
    menu()


def check_chords(my_chord):
    read_file()
    possibilities = [["", 0]]
    for chord in chords:
        score = 0
        i = 0
        for string in my_chord:
            if string == chord[i]:
                score += 1
            i += 1
        if score == 6:
            return chord[6], []
            break
        elif score > possibilities[0][1]:
            possibilities = [[chord[6], score]]
        elif score == possibilities[0][1]:
            possibilities.append([chord[6], score])
    return False, possibilities


def display_chord():
    read_file()
    query = input("Enter the chord you would like to display: ")
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
    menu()

menu()
