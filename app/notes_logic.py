from datetime import datetime

def add_note(notes):
    text = input('Type your note: ').strip()
    if not text:
        print("Note cannot be empty! ")
        return
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    note_with_time = f"{text} [{timestamp}]"
    notes.append(note_with_time)
    print("Note added successfully")




def show_notes(notes):
    if not notes:
            print(" NOTES IS EMPTY ")
    else:
        #print(notes)
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note}")


def delete_note(notes):
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}")
    print("Which note you want to delete? ")

    try:
        index = int(input("Type number of note to delete")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            print(f"Deleted note: {removed}")
        else:
            print("Invalid note number")
    except ValueError:
        print("Please enter a valid number")

def update_note(notes):
    if not notes:
        print("No notes to update!")
        return
    
    for i,note in enumerate(notes, start=1):
        print(f"{i}. {note}")

    index = int(input("Type the number of the note to update: ")) - 1
    if index < 0 or index >= len(notes):
        print("Invalid note number!")
        return
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    new_note = input("Type the new note: ")
    if not new_note.strip():
        return
    
    notes[index] = f"{new_note} [{timestamp}]"
    print("Note updated successfully")

#FOR ARGS
 
def delete_note_by_index(notes, index):
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}")
    print("Which note you want to delete? ")
    number = index -1
    try:
        if 0 <= number < len(notes):
            removed = notes.pop(number)
            print(f"Deleted note: {removed}")
        else:
            print("Invalid note number")
    except ValueError:
        print("Please enter a valid number")

 
def add_note_with_text(notes, text):
    if not text:
        print("Note cannot be empty! ")
        return
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    note_with_time = f"{text} [{timestamp}]"
    notes.append(note_with_time)
    print("Note added successfully")

def update_note_by_index(notes, index, text=None):
    
    number = index - 1 
    try: 
        if 0 <= number < len(notes):
            if not text:
                print("Which note you want to update? ")
                text = input("Type the new note: ")
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M")
            notes[number] = f"{text} [{timestamp}]"
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")
        else: 
            print("Invalid note number")
    except ValueError:
        print("Please enter a vailid number")
