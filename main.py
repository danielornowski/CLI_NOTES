import os
from app.menu import show_menu
from cli_parser import get_args
from database import get_all_notes, add_note_to_db, get_note_by_id, update_note_db, delete_note_db
from app.notes_logic import add_note, show_notes, update_note, delete_note

def run_cli():
    
    
    
    args = get_args()

    
    if args.add or args.show or args.delete or args.update is not None:
        if args.add:
            new_note = add_note_to_db(args.add)
            print(f"Added note {new_note.id}: {new_note.text}")
        elif args.show:
            all_notes = get_all_notes()
            if not all_notes:
                print("No notes in database")
            else:
                for note in all_notes:
                    print(f"{note.id} {note.text} [{note.timestamp}]")
        elif args.delete:
            result = delete_note_db(args.delete)
            if result:
                print(f"Deleted note {args.delete}")
            else:
                print("Note not found")
        elif args.update:
            note_id = int(args.update[0])
            if len(args.update) > 1:
                new_text =" ".join(args.update[1:])
                updated = update_note_db(note_id, new_text)
                if updated:
                    print(f"Updated note {updated.id}: {updated.text} [{updated.timestamp}]")
                else:
                    print("Note not found")
            else:
                new_text = input("Enter new note text: ")
                updated = update_note_db(note_id, new_text)
                if updated:
                    print(f"Updated note {updated.id}: {updated.text} [{updated.timestamp}]")
                else: 
                    print("Note not found")
            
            
    else:

        while True:
            show_menu()
            usr_choice = input("Choose your option: ")

            if usr_choice == "1":
                add_note()
            elif usr_choice == "2":
                all_notes = get_all_notes()
                if not all_notes:
                    print("No notes in database.")
                else:
                    for note in all_notes:
                        print(F"{note.id}. {note.text} [{note.timestamp}]")
            elif usr_choice == "3":
                delete_note()
            elif usr_choice =="4":
                update_note()
            elif usr_choice == "5":
                print("Goodbye")
                break
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    run_cli()