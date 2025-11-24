from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List 
from database import get_all_notes, add_note_to_db, delete_note_db, update_note_db, get_note_by_id
import os



class NoteResponse(BaseModel):
    id: int
    text: str
    timestamp: str
    class Config:
        from_attributes = True

class NoteCreate(BaseModel):
    text: str

app = FastAPI(title="CLI NOTES API")


@app.get("/")
def read_root():
    return {"message": "Welcome to your Notes API!"}

@app.get("/notes", response_model=List[NoteResponse])
def api_get_all_notes():
    notes = get_all_notes()
    return notes

@app.get("/notes/{note_id}", response_model=NoteResponse)
def api_get_note(note_id: int):
    note = get_note_by_id(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.post("/notes", response_model=NoteResponse)
def api_add_note(note: NoteCreate):
    
    if not note.text.strip():
        raise HTTPException(status_code=400, detail="Note cannot be empty")
    new_note = add_note_to_db(note.text)
    if new_note is None:
        raise HTTPException(status_code=500, detail="Database error")
    return new_note

@app.delete("/notes/{note_id}")
def api_delete_note(note_id: int):
    result = delete_note_db(note_id)
    if result == False:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}
    
    
@app.put("/notes/{note_id}", response_model=NoteResponse)
def api_update_note(note_id: int, updated_note: NoteCreate):
    note = get_note_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    if not updated_note.text.strip():
        raise HTTPException(status_code=400, detail="Note text cannot be empty")
    updated = update_note_db(note_id, updated_note.text)
    return updated

