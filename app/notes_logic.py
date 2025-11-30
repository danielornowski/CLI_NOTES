from datetime import datetime
from database import add_note_to_db, get_all_notes, delete_note_db, get_note_by_id, update_note_db

def add_note():
    text = input('Type your note: ').strip()
    if not text:
        print("Note cannot be empty! ")
        return
    new_note = add_note_to_db(text) 
    print(f"Note added successfully with id {new_note.id} at {new_note.timestamp} ")


def show_notes():
    notes = get_all_notes()
    if not notes:
            print(" NOTES IS EMPTY ")
            return
    else:
        for note in notes:
            print(f"{note.id}. {note.text} {note.timestamp} ")


def delete_note():

    show_notes()

    print("Which note you want to delete? ")
    try:
        note_id = int(input("Type id of note to delete"))
        result = delete_note_db(note_id)
        if result == True:
            print("Note deleted successfully")
        else:
            print("Note not found")
    except ValueError:
        print("Please enter a valid id")

def update_note():

    show_notes()

    print("Which note you want to update? ")
    try:
        note_id = int(input("Type number of note to update"))
        note = get_note_by_id(note_id)
        if not note:
            print("Note not found")
            return
        new_text = input("Enter new note text").strip()
        if not new_text:
            print("Note cannot be empty")
            return
        updated = update_note_db(note_id, new_text)
        print(f"Updated note {updated.id}: {updated.text} ({updated.timestamp})")
    except ValueError:
        print("Please enter a valid id")


    
    