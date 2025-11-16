import os
from app.file_manager import load_notes, save_notes
from app.menu import show_menu
from app.notes_logic import add_note, show_notes, delete_note, add_note_with_text, delete_note_by_index, update_note,update_note_by_index
from cli_parser import get_args
from database import get_all_notes, add_note_to_db


def run_cli():
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    notes_file = os.path.join(data_dir, "notes.json")

    
    notes = load_notes(notes_file)

    note = add_note_to_db("My first note")
    print("Added note: ", note.id, note.text, note.timestamp )

    all_notes = get_all_notes()
    print("all notes in database: ")
    for n in all_notes:
        print(n.id, n.text, n.timestamp)

    
    args = get_args()

    
    if args.add or args.show or args.delete or args.update is not None:
        if args.add:
            add_note_with_text(notes, args.add)
            save_notes(notes, notes_file)
        elif args.show:
            show_notes(notes)
        elif args.delete is not None:
            delete_note_by_index(notes, args.delete)
            save_notes(notes, notes_file)
        elif args.update is not None:
            if len(args.update) == 1:
                index = int(args.update[0])
                update_note_by_index(notes, index)
            else:
                index = int(args.update[0])
                text = " ".join(args.update[1:])
                update_note_by_index(notes, index, text)
            save_notes(notes, notes_file)
            
    else:

        while True:
            show_menu()
            usr_choice = input("Choose your option: ")

            if usr_choice == "1":
                add_note(notes)
                save_notes(notes, notes_file)
            elif usr_choice == "2":
                show_notes(notes)
            elif usr_choice == "3":
                delete_note(notes)
                save_notes(notes, notes_file)
            elif usr_choice =="4":
                update_note(notes)
                save_notes(notes, notes_file)
            elif usr_choice == "5":
                print("Goodbye")
                break
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    run_cli()