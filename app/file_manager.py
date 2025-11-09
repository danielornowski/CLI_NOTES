import json


def load_notes(notes_file):
    try:
        with open("data/notes.json", "r") as f:
            notes = json.load(f)
            print("Data loaded successfully")
    except FileNotFoundError:
        print("The file was not found. ")
        notes=[]
    except json.JSONDecodeError:
        print("The file contains inavlid JSON. ")
        notes=[]
    return notes

def save_notes(notes, notes_file):
    with open("data/notes.json", "w") as f:
        json.dump(notes, f, indent=4)
        print("Notes saved correctly")
