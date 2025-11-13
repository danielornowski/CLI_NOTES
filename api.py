from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List 
from app.file_manager import load_notes, save_notes
from app.notes_logic import delete_note, add_note, show_notes,  update_note
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

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    if note_id < 0 or note_id >= len(notes):
        raise HTTPException(status_code=404, detail="Note not found")
    return {"id": note_id, "text": notes[note_id]}

@app.post("/notes")
def add_note_api(note:Note):
    if not note.text.strip():
        raise HTTPException(status_cod=400, detail="Note cannot be empty")
    add_note(notes, note.text)
    save_notes(notes, NOTES_FILE)
    return {"message": "Note added successfully", "note": note.text}

@app.delete("/notes/{note_id}")
def delete_note_api(note_id: int):
    if note_id < 0 or note_id >= len(notes):
        raise HTTPException(status_code=404, detail="Note not found")
    delete_note = delete_note(notes, note_id)
    save_notes(notes, NOTES_FILE)
    return {"message": f"Deleted note: {delete_note}"}
    
@app.put("/notes/{note_id}")
def update_note_api(note_id: int, updated_note: Note):
    if note_id < 0 or note_id >= len(notes):
        raise HTTPException(status_code=400, detail="Note not found")
    if not update_note.text.strip():
        raise HTTPException(status_cod=400, detail="Note cannot be empty")
    update_note(notes, note_id, update_note.text)
    save_notes(notes, NOTES_FILE)
    return {"message": f"Note {note_id} updated successfully", "note": updated_note.text}
