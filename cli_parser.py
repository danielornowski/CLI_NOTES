import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Simple Notes CLI")
    parser.add_argument("--add", type=str, help="Add a new note")
    parser.add_argument("--show", action="store_true", help="Show all notes")
    parser.add_argument("--delete", type=int, help="Delete a note by its number")
    parser.add_argument("--update", nargs="+", help="Update a note by its number")
    args = parser.parse_args()
    return args