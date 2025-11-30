from database import add_note_to_db, get_all_notes, delete_note_db, update_note_db, get_note_by_id
from database import Note
from datetime import datetime

def test_add_note(db_session):
    note = add_note_to_db("hello", db=db_session)

    assert note.id == 1
    assert note.text == "hello"

def test_get_note_by_id(db_session):
    note = add_note_to_db("abc", db=db_session)
    found = get_note_by_id(note.id, db=db_session)

    assert found.text == "abc"

def test_delete_note(db_session):
    note = add_note_to_db("to delete", db=db_session)
    result = delete_note_db(note.id, db=db_session)

    assert result is True
    assert get_note_by_id(note.id, db=db_session) is None

def test_update_note(db_session):
    note = add_note_to_db("old", db=db_session)
    updated = update_note_db(note.id, "new", db=db_session)

    assert updated.id == note.id

