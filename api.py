from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List 
from app.file_manager import load_notes, save_notes
from app.notes_logic import delete_note, add_note, show_notes
import os



class Note(BaseModel):
    text: str

app = FastAPI(title="CLI NOTES API")

DATA_DIR = "data"
NOTES_FILE = os.path.join(DATA_DIR, "notes.json")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

notes = load_notes(NOTES_FILE)

@app.get("/")
def read_root():
    return {"message": "Welcome to your Notes API!"}

@app.get("/notes", response_model=List[str])
def get_all_notes():
    return notes

@app.getO("/notes/{note_id}")
def get_note(note_id: int):
    if note_id < 0 or note_id >= len(notes):
        raise HTTPException(status_code=404, detail="Note not found")
    return {"id": note_id, "text": notes[note_id]}

@app.post("/notes")
def add_note_api(note:dict):
    text = note.get("text")
    if not text:
        return {"error" : "Missing 'text' in request body "}
    add_note(notes, text)
    save_notes(notes, NOTES_FILE)
    return {"message": "Note added"}

@app.delete("/notes/{index}")
def delete_note_api(index: int):
    delete_note(notes, index)
    save_notes(notes, NOTES_FILE)
    return {"message": "Note deleted"}
